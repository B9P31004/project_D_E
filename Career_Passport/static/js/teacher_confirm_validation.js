$(function(){
    $(".alert").hide();
    $(document).on('click',"button[name=button_input]",function(){
        var sendflag=true;
        if(!$("#confirm_text[name=confirm_comment]").val()){
            $(".alert[name=teacher_comment_area]").show();
            sendflag=false;
        }else{
            $(".alert[name=teacher_comment_area]").hide();
        }
        if(sendflag==false){
            return false
        }
    });
});