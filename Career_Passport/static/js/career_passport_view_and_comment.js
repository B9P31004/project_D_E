$(function(){
    var year=$('select.year_select option:selected').val();
    var semester=1;
    var career_passport_select=year*100+semester*10;
    career_passport_confirm(career_passport_select,year);
    $('select.year_select').change(function(){
        year=$('select.year_select option:selected').val();
    });
    $('#back_flag').ready(function(){
        $(document).on('click',function(e) {
            if($(e.target).closest('#n_6__1').length) {
                semester=1;
                career_passport_select=year*100+semester*10;
                career_passport_confirm(career_passport_select,year);
            }
            else if($(e.target).closest('#n_7__1').length) {
                semester=1;
                career_passport_select=year*100+semester*10+1;
                career_passport_confirm(career_passport_select,year);
            }
            else if($(e.target).closest('#n_8__1').length) {
                semester=2;
                career_passport_select=year*100+semester*10;
                career_passport_confirm(career_passport_select,year);
            }
            else if($(e.target).closest('#n_9__1').length) {
                semester=2;
                career_passport_select=year*100+semester*10+1;
                career_passport_confirm(career_passport_select,year);
            }
            else if($(e.target).closest('#n_10__1').length) {
                semester=3;
                career_passport_select=year*100+semester*10;
                career_passport_confirm(career_passport_select,year);
            }
            else if($(e.target).closest('#n_11__1').length) {
                semester=3;
                career_passport_select=year*100+semester*10+1;
                career_passport_confirm(career_passport_select,year);
            }
        }); 
    });
});

function career_passport_confirm(career_passport_select,year){
    var teacher_year=parseInt($('#teacher_year').html());
    var url=$('#career_passport_url').html();
    var career_passport_select=career_passport_select;
    var comment=$('#send_comment').html();
    var select_number=parseInt($('#select_number').val());
    var height=1000;
    $('p.alert').hide();
    if (select_number){
        career_passport_select=select_number;
        $('#n_6__1').css('top','275px');
        if(select_number-(year*100)==10){
            $('#n_6__1').css('top','278px');
        }
        else if(select_number-(year*100)==11){
            $('#n_7__1').css('top','278px');
        }
        else if(select_number-(year*100)==20){
            $('#n_8__1').css('top','278px');
        }
        else if(select_number-(year*100)==21){
            $('#n_9__1').css('top','278px');
        }
        else if(select_number-(year*100)==30){
            $('#n_10__1').css('top','278px');
        }
        else if(select_number-(year*100)==31){
            $('#n_11__1').css('top','278px');
        }
        $('input#select_number').remove();
        $('p#send_comment').remove();
    }
    $.ajax({
        url:url,
        method:'POST',
        data:{'select':career_passport_select},
        timeout:10000,
        dataType:"json",
    }).done(function(response,status,xhr){
        $("#error_text_c").html('');
        var career_passport_e=response.empty;
        if (career_passport_e==1){
            career_passport_q=response.question;
            career_passport_r=response.result;
            var html='';
            if('analize' in response){
                career_passport_a=response.analize;
                for (var i=0; i<career_passport_q.length;i++){
                    html+='<h6 id="label">'+career_passport_q[i]+':</h6><textarea id="area" readonly>'+career_passport_r[i]+'</textarea><h6>ネガポジ判定：'+career_passport_a[i][0]+'　/スコア:'+career_passport_a[i][1]+'</h6>';
                    height+=155;
                }
            }
            else{
                for (var i=0; i<career_passport_q.length;i++){
                    html+='<h6 id="label">'+career_passport_q[i]+':</h6><textarea id="area" readonly>'+career_passport_r[i]+'</textarea>';
                    height+=153;
                }
            }
            height+=30;
            $("#career_passport").html(html);
            $("#select_value").html('<input type="hidden" name="select_text" value="'+career_passport_select+'">');
            if (teacher_year*1000<career_passport_select&&career_passport_select<=teacher_year*1000+31){
                html='';
                $("#teacher_comment").html(html);
                if (comment){
                    $("#teacher_comment_area").html('<h6 id="label">コメント：</h6><textarea style="width:100%;" id="confirm_text" name="confirm_comment" rows="5" cols="100">'+comment+'</textarea>');
                    height+=153;
                }
                else {
                    if ('comment' in response){
                        $("#teacher_comment_area").html('<h6 id="label">コメント：</h6><textarea style="width:100%;" id="confirm_text" name="confirm_comment" rows="5" cols="100">'+response.comment+'</textarea>');
                        height+=153;
                    }
                    else {
                        $("#teacher_comment_area").html('コメント：<br><textarea style="width:100%;" id="confirm_text" name="confirm_comment" rows="5" cols="100"></textarea>');
                        height+=153;
                    }
                }
                $("#add_button").html('<button type="submit" name="button_input">送信</button>');
                height+=100;
            }
            else{
                $("#teacher_comment_area").html('');
                $("#add_button").html('');
                if ('comment' in response){
                    html='';
                    html+="<h6 id='label'>先生のコメント:</h6>";
                    career_passport_c=response.comment;
                    html+='<textarea id="teacher_comment" readonly>'+career_passport_c+'</textarea>';
                    $("#teacher_comment").html(html);
                    height+=153;
                }
                else{
                    html='';
                    $("#teacher_comment").html(html);
                }
                height+=30;
            }
        }
        else{
            $("#career_passport").html('');
            $("#teacher_comment").html('');
            $("#teacher_comment_area").html('');
            $("#add_button").html('');
            $("#error_text_c").html('<p id="error_text_c">データが登録されていません。登録してください。</p>');
        }
        $('svg.n_272').html('<rect id="n_272" rx="0" ry="0" x="0" y="0" width="1024" height="'+String(height)+'"></rect>')
        $('#index').css('height',String(height)+'px');
    }).fail(function(response){
        $("#error_text_c").html('<p id="error_text_c">通信エラー</p>');
        $('svg.n_272').html('<rect id="n_272" rx="0" ry="0" x="0" y="0" width="1024" height="'+String(height)+'"></rect>')
        $('#index').css('height',String(height)+'px');
    });
}

/*function career_passport_confirm(career_passport_select){
    var back_flag=parseInt($('#back_flag').val());
    var teacher_year=parseInt($('#teacher_year').html());
    var url=$('#career_passport_url').html();
    var career_passport_select=career_passport_select;
    var comment=$('#send_comment').html();
    if (back_flag==1){
        var comment=$('#send_comment').html();
        var select_number=parseInt($('#select_number').val());
        $('#career_passport_select option[value='+select_number+']').prop('selected',true);
            $.ajax({
                url:url,
                method:'POST',
                data:{'select':select_number},
                timeout:10000,
                dataType:"json",
            }).done(function(response,status,xhr){
                $("#error_text_c").html('');
                career_passport_q=response.question;
                career_passport_r=response.result;
                var html='<hr style="height:20px; background-color:#99FFFF;" noshade="">';
                if('analize' in response){
                    career_passport_a=response.analize;
                    for (var i=0; i<career_passport_q.length;i++){
                        html+='<h6>'+career_passport_q[i]+':'+career_passport_r[i]+'　/ネガポジ判定：'+career_passport_a[i][0]+'　/スコア:'+career_passport_a[i][1]+'</h6>';
                    }
                }
                else{
                    for (var i=0; i<career_passport_q.length;i++){
                        html+='<h6>'+career_passport_q[i]+':'+career_passport_r[i]+'</h6>';
                    }
                }
                html+='<hr style="height:20px; background-color:#99FFFF;" noshade="">';
                $("#career_passport").html(html);
                $("#select_value").html('<input type="hidden" name="select_text" value="'+select_number+'">');
                if (teacher_year*1000<select_number&&select_number<=teacher_year*1000+31){
                    html='';
                    $("#teacher_comment").html(html);
                    console.log(response)
                    if (comment){
                        $("#teacher_comment_area").html('コメント：<br><textarea style="width:100%;" id="confirm_text" name="confirm_comment" rows="5" cols="100">'+comment+'</textarea>');
                    }
                    else {
                        $("#teacher_comment_area").html('コメント：<br><textarea style="width:100%;" id="confirm_text" name="confirm_comment" rows="5" cols="100"></textarea>');
                    }
                    $("#add_button").html('<button type="submit" name="button_input">送信</button>');
                }
                else{
                    $("#teacher_comment_area").html('');
                    $("#add_button").html('');
                    if ('comment' in response){
                        html='';
                        html+="<h6>先生のコメント:";
                        career_passport_c=response.comment;
                        html+=career_passport_c+'</h6>';
                        html+='----------------------------------';
                        $("#teacher_comment").html(html);
                    }
                    else{
                        html='';
                        $("#teacher_comment").html(html);
                    }
                }
            }).fail(function(response){
                $("#error_text_c").html('<p>データが登録されていません。登録してください。</p>');
            });
    }
    else{
        $(".alert").hide();
        $.ajax({
            url:url,
            method:'POST',
            data:{'select':career_passport_select},
            timeout:10000,
            dataType:"json",
        }).done(function(response,status,xhr){
            $("#error_text_c").html('');
            career_passport_q=response.question;
            career_passport_r=response.result;
            var html='<hr style="height:20px; background-color:#99FFFF;" noshade="">';
            if('analize' in response){
                career_passport_a=response.analize;
                console.log("a");
                for (var i=0; i<career_passport_q.length;i++){
                    html+='<h6>'+career_passport_q[i]+':'+career_passport_r[i]+'　/ネガポジ判定：'+career_passport_a[i][0]+'　/スコア:'+career_passport_a[i][1]+'</h6>';
                }
            }
            else{
                for (var i=0; i<career_passport_q.length;i++){
                    html+='<h6>'+career_passport_q[i]+':'+career_passport_r[i]+'</h6>';
                }
            }
            html+='<hr style="height:20px; background-color:#99FFFF;" noshade="">';
            $("#career_passport").html(html);
            $("#select_value").html('<input type="hidden" name="select_text" value="'+career_passport_select+'">');
            if (teacher_year*1000<career_passport_select&&career_passport_select<=teacher_year*1000+31){
                html='';
                $("#teacher_comment").html(html);
                if ('comment' in response){
                    $("#teacher_comment_area").html('コメント：<br><textarea style="width:100%;" id="confirm_text" name="confirm_comment" rows="5" cols="100">'+response.comment+'</textarea>');
                }
                else {
                    $("#teacher_comment_area").html('コメント：<br><textarea style="width:100%;" id="confirm_text" name="confirm_comment" rows="5" cols="100"></textarea>');
                }
                $("#add_button").html('<button type="submit" name="button_input">送信</button>');
            }
            else{
                $("#teacher_comment_area").html('');
                $("#add_button").html('');
                if ('comment' in response){
                    html='';
                    html+="<h6>先生のコメント:";
                    career_passport_c=response.comment;
                    html+=career_passport_c+'</h6>';
                    html+='----------------------------------';
                    $("#teacher_comment").html(html);
                }
                else{
                    html='';
                    $("#teacher_comment").html(html);
                }
            }
        }).fail(function(response){
            $("#error_text_c").html('<p>データが登録されていません。登録してください。</p>');
        });
    }
}*/