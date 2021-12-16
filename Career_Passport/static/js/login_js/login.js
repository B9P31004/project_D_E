$(document).ready(function(){
    $("input[name='username']").attr('placeholder','ユーザIDを入力');
    $("input[name='password']").attr('placeholder','パスワードを入力');
    if($('p#error_text').length){
        $('div#n_20').css('top','531px');
        $('input[name="username"]').val('');
        $('input[name="username"]').css('border','solid 1px rgba(255,56,56,1)');
        $('input[name="password"]').css('border','solid 1px rgba(255,56,56,1)');
    }
    $('input[name="username"],input[name="password"]').focus(function(){
        $('div#n_20').css('top','510px');
        $('input[name="username"]').css('border','none');
        $('input[name="password"]').css('border','none');
        $('p#error_text').hide();
        $('p#error_text2').hide();
    });
    $('button#Text_').click(function(){
        if(isNaN($('input[name="username"]').val())){
            $('p#error_text2').removeAttr('style');
            $('div#n_20').css('top','531px');
            $('input[name="username"]').val('');
            $('input[name="password"]').val('');
            $('input[name="username"]').css('border','solid 1px rgba(255,56,56,1)');
            $('input[name="password"]').css('border','solid 1px rgba(255,56,56,1)');
            return false;
        }
    });
});