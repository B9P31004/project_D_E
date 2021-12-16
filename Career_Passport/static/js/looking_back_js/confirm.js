$(function(){
    var height=330;
    var get_h=$('form#confirm').height();
    height+=get_h+50;
    $('svg.n_272').html('<rect id="n_272" rx="0" ry="0" x="0" y="0" width="1024" height="'+height+'"></rect>');
    $('#index').css('height',String(height)+'px');
    $('span#n_11__text').text('キャリアパスポート');
    $('div#n_11__').css("left","79px");
    $('div#n_11__').css("width","357px");
    $('div#n_15').hide();
});