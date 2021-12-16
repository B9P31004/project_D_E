$(function(){
    var year=$('select.year_select option:selected').val()/10;
    var semester=1;
    var value=0;
    $('select.year_select').change(function(){
        year=$('select.year_select option:selected').val()/10;
    });
    value=10000*year+100*semester;
    var html='<option hidden>選択してください</option><option value="'+value+1+'">'+year+'年'+semester+'学期中間</option>';
    html+='<option value="'+value+2+'">'+year+'年'+semester+'学期期末</option>';
    $('select#grade_select').html(html);
    $(document).on('click',function(e) {
        if($(e.target).closest('#n_6__1').length) {
            $("div#error_text").html('');
            semester=1;
            value=10000*year+100*semester+1;
            var html='<option hidden>選択してください</option><option value="'+value+'">'+year+'年'+semester+'学期中間</option>';
            value+=1
            html+='<option value="'+value+'">'+year+'年'+semester+'学期期末</option>';
            $('select#grade_select').html(html);
        }
        else if($(e.target).closest('#n_7__1').length) {
            $("div#error_text").html('');
            semester=1;
            value=10000*year+100*semester+1;
            var html='<option hidden>選択してください</option><option value="'+value+'">'+year+'年'+semester+'学期中間</option>';
            value+=1
            html+='<option value="'+value+'">'+year+'年'+semester+'学期期末</option>';
            $('select#grade_select').html(html);
        }
        else if($(e.target).closest('#n_8__1').length) {
            $("div#error_text").html('');
            semester=2;
            value=10000*year+100*semester+1;
            var html='<option hidden>選択してください</option><option value="'+value+'">'+year+'年'+semester+'学期中間</option>';
            value+=1
            html+='<option value="'+value+'">'+year+'年'+semester+'学期期末</option>';
            $('select#grade_select').html(html);
        }
        else if($(e.target).closest('#n_9__1').length) {
            $("div#error_text").html('');
            semester=2;
            value=10000*year+100*semester+1;
            var html='<option hidden>選択してください</option><option value="'+value+'">'+year+'年'+semester+'学期中間</option>';
            value+=1
            html+='<option value="'+value+'">'+year+'年'+semester+'学期期末</option>';
            $('select#grade_select').html(html);
        }
        else if($(e.target).closest('#n_10__1').length) {
            $("div#error_text").html('');
            semester=3;
            value=10000*year+100*semester+1;
            var html='<option hidden>選択してください</option><option value="'+value+'">'+year+'年'+semester+'学期中間</option>';
            value+=1
            html+='<option value="'+value+'">'+year+'年'+semester+'学期期末</option>';
            $('select#grade_select').html(html);
        }
        else if($(e.target).closest('#n_11__1').length) {
            $("div#error_text").html('');
            semester=3;
            value=10000*year+100*semester+1;
            var html='<option hidden>選択してください</option><option value="'+value+'">'+year+'年'+semester+'学期中間</option>';
            value+=1
            html+='<option value="'+value+'">'+year+'年'+semester+'学期期末</option>';
            $('select#grade_select').html(html);
        }
    });
    function drawChart(){
        var ctx=document.getElementById('gradechart');
        var gradeChart=new Chart(ctx,{
            type:'radar',
            data:{
                labels:['国語','数学','英語','社会','理科','音楽','美術','技術・家庭科','保健体育'],
                datasets:[{
                        label:'成績',
                        data:grade,
                        borderColor:'blue',
                        borderWidth:3,
                }],
            },
            options:{
                r:{
                    min:0,
                    max:100,
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
        return gradeChart;
    }
    grade=[];
    grade[0]=0;
    grade[1]=0;
    grade[2]=0;
    grade[3]=0;
    grade[4]=0;
    grade[5]=0;
    grade[6]=0;
    grade[7]=0;
    grade[8]=0;
    gradeChart=drawChart();
    $('#grade_select').change(function(){
        var grade_select=$('#grade_select option:selected').val();
        var url=$('#grade_url').html();
        $.ajax({
            url:url,
            method:'POST',
            data:{'select':grade_select},
            timeout:10000,
            dataType:"json",
        }).done(function(response,status,xhr){
            grade_e=response.grade_error_flag
            console.log(grade_e);
            if(grade_e==1){
                $("div#error_text").html('');
                grade=[];
                grade[0]=response.national_language;
                grade[1]=response.math;
                grade[2]=response.english;
                grade[3]=response.social_studies;
                grade[4]=response.science;
                grade[5]=response.music;
                grade[6]=response.art;
                grade[7]=response.technical_arts_and_home_economics;
                grade[8]=response.health_and_physical_education;
                gradeChart.data.datasets[0].data=grade;
            }
            else{
                $("div#error_text").html('<p id="error_text">'+grade_e+'</p>');
                grade=[];
                grade[0]=0;
                grade[1]=0;
                grade[2]=0;
                grade[3]=0;
                grade[4]=0;
                grade[5]=0;
                grade[6]=0;
                grade[7]=0;
                grade[8]=0;
                gradeChart.data.datasets[0].data=grade;
            }
            gradeChart.update();
        }).fail(function(response){
            $("div#error_text").html('<p id="error_text">通信エラー</p>');
            grade=[];
            grade[0]=0;
            grade[1]=0;
            grade[2]=0;
            grade[3]=0;
            grade[4]=0;
            grade[5]=0;
            grade[6]=0;
            grade[7]=0;
            grade[8]=0;
            gradeChart.data.datasets[0].data=grade;
            gradeChart.update();
        });
    });
});