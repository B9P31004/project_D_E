$(function(){
    $('svg.n_272').html('<rect id="n_272" rx="0" ry="0" x="0" y="0" width="1024" height="2097"></rect>')
    $('span#n_11__text').text("行事一覧");
    $('div#n_15').hide();
    $('div#n_11__').css("left","79px");
    $('div#n_11__').css("width","357px");
    var semester=1;
    event_get(semester);
    //$('a').click(function(){
    //    return false;
    //});
    $(document).on('click',function(e) {
        if($(e.target).closest('#n_6__1').length) {
            for(var i=6;i<=8;i++){
                if(i!=6){
                    $('#n_'+String(i)+'__1').css('top','275px');
                }
                else{
                    $('#n_6__1').css('top','278px');
                    $('span#event_01').text('○ 入学式');
                    $('span#event_02').text('○ 1年生歓迎会');
                    $('span#event_03').text('○ 交通教室');
                    semester=1;
                    event_get(semester);
                    console.log(semester);
                }
            }
        }
        else if($(e.target).closest('#n_7__1').length) {
            for(var i=6;i<=8;i++){
                if(i!=7){
                    $('#n_'+String(i)+'__1').css('top','275px');
                }
                else{
                    $('#n_7__1').css('top','278px');
                    $('span#event_01').text('○ 避難訓練');
                    $('span#event_02').text('○ 体育祭');
                    $('span#event_03').text('○ 修学旅行');
                    semester=2;
                    event_get(semester);
                }
            }
        }
        else if($(e.target).closest('#n_8__1').length) {
            for(var i=6;i<=8;i++){
                if(i!=8){
                    $('#n_'+String(i)+'__1').css('top','275px');
                }
                else{
                    $('#n_8__1').css('top','278px');
                    $('span#event_01').text('○ 生徒会選挙');
                    $('span#event_02').text('○ 3年生を送る会');
                    $('span#event_03').text('○ 卒業式');
                    semester=3;
                    event_get(semester);
                }
            }
        }
    });
});

function event_get(semester){
    var url=$('#event_url').html();
    $.ajax({
        url:url,
        method:'GET',
        data:{'semester':semester},
        timeout:10000,
        dataType:"json",
    }).done(function(response,status,xhr){
        $("#error_text_c").html('');
        var event_e=response.empty;
        var img_tag_1=['n_393','n_393_b','n_393_ca','n_393_cb'];
        var img_tag_2=['n_393_cc','n_393_cd','n_393_ce','n_393_cf'];
        var img_tag_3=['n_393_cj','n_393_ck','n_393_cl','n_393_cm'];
        if(event_e==1){
            var event_1=response.event_1;
            var event_2=response.event_2;
            var event_3=response.event_3;
            for (var i=1;i<4;i++){
                if(i==1){
                    var html='';
                    for(var j=0;j<4;j++){
                        if(Array.isArray(event_1)){
                            if(event_1.length>=j+1){
                                html+='<div class="'+img_tag_1[j]+'">';
                                html+='<img id="'+img_tag_1[j]+'" src="'+event_1[j]+'" style="width:183px; height:145px;"></div>';
                            }
                            else{
                                html+='<svg class="'+img_tag_1[j]+'">';
                                html+='<rect id="'+img_tag_1[j]+'" rx="0" ry="0" x="0" y="0" width="183" height="145"></rect></svg>';
                            }
                        }
                        else{
                            html+='<svg class="'+img_tag_1[j]+'">';
                            html+='<rect id="'+img_tag_1[j]+'" rx="0" ry="0" x="0" y="0" width="183" height="145"></rect></svg>';
                        }
                    }
                    $('div#event_1').html(html);
                }
                else if(i==2){
                    var html='';
                    for(var j=0;j<4;j++){
                        if(Array.isArray(event_2)){
                            if(event_2.length>=j+1){
                                html+='<div class="'+img_tag_2[j]+'">';
                                html+='<img id="'+img_tag_2[j]+'" src="'+event_2[j]+'" style="width:183px; height:145px;"></div>';
                            }
                            else{
                                html+='<svg class="'+img_tag_2[j]+'">';
                                html+='<rect id="'+img_tag_2[j]+'" rx="0" ry="0" x="0" y="0" width="183" height="145"></rect></svg>';
                            }
                        }
                        else{
                            html+='<svg class="'+img_tag_2[j]+'">';
                            html+='<rect id="'+img_tag_2[j]+'" rx="0" ry="0" x="0" y="0" width="183" height="145"></rect></svg>';
                        }
                    }
                    $('div#event_2').html(html);
                }
                else if(i==3){
                    var html='';
                    for(var j=0;j<4;j++){
                        if(Array.isArray(event_3)){
                            if(event_3.length>=j+1){
                                html+='<div class="'+img_tag_3[j]+'">';
                                html+='<img id="'+img_tag_3[j]+'" src="'+event_3[j]+'" style="width:183px; height:145px;"></div>';
                            }
                            else{
                                html+='<svg class="'+img_tag_3[j]+'">';
                                html+='<rect id="'+img_tag_3[j]+'" rx="0" ry="0" x="0" y="0" width="183" height="145"></rect></svg>';
                            }
                        }
                        else{
                            html+='<svg class="'+img_tag_3[j]+'">';
                            html+='<rect id="'+img_tag_3[j]+'" rx="0" ry="0" x="0" y="0" width="183" height="145"></rect></svg>';
                        }
                    }
                    $('div#event_3').html(html);
                }
            }
            console.log(event_1);
        }
        else{
            for (var i=1;i<4;i++){
                if(i==1){
                    var html='';
                    for(var j=0;j<4;j++){
                        html+='<svg class="'+img_tag_1[j]+'">';
                        html+='<rect id="'+img_tag_1[j]+'" rx="0" ry="0" x="0" y="0" width="183" height="145"></rect></svg>';
                    }
                    $('div#event_1').html(html);
                }
                else if(i==2){
                    var html='';
                    for(var j=0;j<4;j++){
                        html+='<svg class="'+img_tag_2[j]+'">';
                        html+='<rect id="'+img_tag_2[j]+'" rx="0" ry="0" x="0" y="0" width="183" height="145"></rect></svg>';
                    }
                    $('div#event_2').html(html);
                }
                else if(i==3){
                    var html='';
                    for(var j=0;j<4;j++){
                        html+='<svg class="'+img_tag_3[j]+'">';
                        html+='<rect id="'+img_tag_3[j]+'" rx="0" ry="0" x="0" y="0" width="183" height="145"></rect></svg>';
                    }
                    $('div#event_3').html(html);
                }
            }
        }
    }).fail(function(response){
        $("#error_text_c").html('<p>通信エラー</p>');
    });
};