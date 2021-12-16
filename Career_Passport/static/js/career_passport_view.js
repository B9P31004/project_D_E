$(function(){
    var year=$('select.year_select option:selected').val();
    var semester=1;
    var se='s';
    var career_passport_select=String(year)+String(semester)+se;
    career_passport(career_passport_select);
    $('select.year_select').change(function(){
        year=$('select.year_select option:selected').val();
    });
    $(document).on('click',function(e) {
        if($(e.target).closest('#n_6__1').length) {
            semester=1;
            se='s';
            career_passport_select=String(year)+String(semester)+se;
            career_passport(career_passport_select);
        }
        else if($(e.target).closest('#n_7__1').length) {
            semester=1;
            se='e';
            career_passport_select=String(year)+String(semester)+se;
            career_passport(career_passport_select);
        }
        else if($(e.target).closest('#n_8__1').length) {
            semester=2;
            se='s';
            career_passport_select=String(year)+String(semester)+se;
            career_passport(career_passport_select);
        }
        else if($(e.target).closest('#n_9__1').length) {
            semester=2;
            se='e';
            career_passport_select=String(year)+String(semester)+se;
            career_passport(career_passport_select);
        }
        else if($(e.target).closest('#n_10__1').length) {
            semester=3;
            se='s';
            career_passport_select=String(year)+String(semester)+se;
            career_passport(career_passport_select);
        }
        else if($(e.target).closest('#n_11__1').length) {
            semester=3;
            se='e';
            career_passport_select=String(year)+String(semester)+se;
            career_passport(career_passport_select);
        }
    });
});

function career_passport(career_passport_select){
    var url=$('#career_passport_url').html();
    var height=880;
    $.ajax({
        url:url,
        method:'POST',
        data:{'select':career_passport_select},
        timeout:10000,
        dataType:"json",
    }).done(function(response,status,xhr){
        $("#error_text_c").html('');
        var career_passport_e=response.empty;
        if(career_passport_e==1){
            var career_passport_q=response.question;
            var career_passport_r=response.result;
            var html='';
            for (var i=0; i<career_passport_q.length;i++){
                html+='<h6 id="label">'+career_passport_q[i]+':</h6><textarea id="area" readonly>'+career_passport_r[i]+'</textarea>';
                height+=153;
            }
            height+=30;
            $("#career_passport").html(html);
            if ('comment' in response){
                html='';
                html+="<h6 id='label'>先生のコメント:</h6>";
                var career_passport_c=response.comment;
                html+='<textarea id="area" readonly>'+career_passport_c+'</textarea>';
                height+=183;
                $("#teacher_comment").html(html);
            }
            else{
                $("#teacher_comment").html('');
            }
        }
        else{
            height+=120;
            $("#career_passport").html('');
            $("#teacher_comment").html('');
            $("#error_text_c").html('<p id="error_text_c">データが登録されていません。</p>');
        }
        $('svg.n_272').html('<rect id="n_272" rx="0" ry="0" x="0" y="0" width="1024" height="'+height+'"></rect>');
        $('#index').css('height',String(height)+'px');
        
    }).fail(function(response){
        $("#error_text_c").html('<p>通信エラー</p>');
    });
};