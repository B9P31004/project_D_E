$(function(){
    $(".alert").hide();
    var loop=$("input[name=length]").val();
    $("button[name=button_input]").click(function(){
        var sendflag=true;
        for (var i=0;i<loop;i++){
            if(!$("#cp_text[name='"+i+"']").val()){
                $(".alert[name='"+i+"']").show();
                sendflag=false;
            }else{
                $(".alert[name='"+i+"']").hide();
            }
        }
        if(sendflag==false){
            return false;
        }
    });
});