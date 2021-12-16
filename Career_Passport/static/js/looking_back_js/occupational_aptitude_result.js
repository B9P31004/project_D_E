$(function(){
    var flag;
    $('svg.n_272').html('<rect id="n_272" rx="0" ry="0" x="0" y="0" width="1024" height="1700"></rect>')
    $('span#n_11__text').text('職業適性検査');
    $('div#n_11__').css("left","79px");
    $('div#n_11__').css("width","357px");
    $('div#n_15').hide();
    if (flag==1) {}
    else{
        flag=occupational_aptitude();
    }
    console.log('a');
});

function occupational_aptitude(){
    var url=$('#occupational_aptitude_url').html();
    var height=880;
    var list=[];
    $.ajax({
        url:url,
        method:'GET',
        timeout:10000,
        dataType:"json",
    }).done(function(response,status,xhr){
        $("#error_text_c").html('');
        var occupational_aptitude_e=response.empty;
        if(occupational_aptitude_e==1){
            var occupational_aptitude_q=response.question;
            var occupational_aptitude_r=response.result;
            var occupational_aptitude_a=response.analize;
            var html='';
            for (var i=0; i<occupational_aptitude_q.length;i++){
                html+='<h6 id="label">'+occupational_aptitude_q[i]+':</h6><textarea id="area" readonly>'+occupational_aptitude_r[i]+'</textarea><p>'+occupational_aptitude_a[i][0]+' /スコア:'+occupational_aptitude_a[i][2]+'</p>';
                height+=153;
                list[i]=occupational_aptitude_a[i][1];
            }
            height+=30;
            $("#occupational_aptitude").html(html);
            console.log(list);
        }
        else{
            height+=120;
            $("#occupational_aptitude").html('');
            $("#error_text_c").html('<p id="error_text_c">データが登録されていません。</p>');
            list=[0,0,0,0,0,0];
        }
        $('svg.n_272').html('<rect id="n_272" rx="0" ry="0" x="0" y="0" width="1024" height="'+height+'"></rect>');
        $('#index').css('height',String(height)+'px');
        drawChart(list);
        return 1;
    }).fail(function(response){
        $("#error_text_c").html('<p>通信エラー</p>');
        list=[0,0,0,0,0,0];
        drawChart(list);
        return 1;
    });
};

function drawChart(data){
    var ctx=document.getElementById('occupational_aptitude_chart');
    var occupational_aptitude_Chart=new Chart(ctx,{
        type:'radar',
        data:{
            labels:['現実的','研究的','芸術的','社会的','企業的','慣習'],
            datasets:[{
                    label:'タイプ',
                    data:data,
                    borderColor:'blue',
                    borderWidth:3,
            }],
        },
        options:{
            r:{
                min:0,
                max:5,
                backgroundColor:'lightblue',
                grid:{
                    color:'darkblue',
                },
                angleLines:{
                    color:'aqua',
                },
                pointLabels:{
                    color:'darkblue',
                    backdropColor:'lightgreen',
                    backdropPadding:5,
                    padding:20,
                },
            },
        },
    });
    return occupational_aptitude_Chart;
};