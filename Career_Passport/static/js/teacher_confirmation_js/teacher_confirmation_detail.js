$(function(){
    var student_detail=$('div#student_detail').html();
    $('span#n_11__text').text(student_detail);
    $('div#n_11__').css("left","79px");
    $('div#n_11__').css("width","357px");
    $(document).on('click',function(e) {
        if($(e.target).closest('#n_6__1').length) {
            for(var i=6;i<=11;i++){
                if(i!=6){
                    $('#n_'+String(i)+'__1').css('top','275px');
                }
                else{
                    $('#n_6__1').css('top','278px');
                }
            }
        }
        else if($(e.target).closest('#n_7__1').length) {
            for(var i=6;i<=11;i++){
                if(i!=7){
                    $('#n_'+String(i)+'__1').css('top','275px');
                }
                else{
                    $('#n_7__1').css('top','278px');
                }
            }
        }
        else if($(e.target).closest('#n_8__1').length) {
            for(var i=6;i<=11;i++){
                if(i!=8){
                    $('#n_'+String(i)+'__1').css('top','275px');
                }
                else{
                    $('#n_8__1').css('top','278px');
                }
            }
        }
        else if($(e.target).closest('#n_9__1').length) {
            for(var i=6;i<=11;i++){
                if(i!=9){
                    $('#n_'+String(i)+'__1').css('top','275px');
                }
                else{
                    $('#n_9__1').css('top','278px');
                }
            }
        }
        else if($(e.target).closest('#n_10__1').length) {
            for(var i=6;i<=11;i++){
                if(i!=10){
                    $('#n_'+String(i)+'__1').css('top','275px');
                }
                else{
                    $('#n_10__1').css('top','278px');
                }
            }
        }
        else if($(e.target).closest('#n_11__1').length) {
            for(var i=6;i<=11;i++){
                if(i!=11){
                    $('#n_'+String(i)+'__1').css('top','275px');
                }
                else{
                    $('#n_11__1').css('top','278px');
                }
            }
        }
    });
})