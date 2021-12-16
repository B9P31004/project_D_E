$(function(){
    var height=500;
    var get_h=$('div#n_54 > a').length;
    for(var i=0;i<get_h;i++){
        height+=36;
    }
    $('svg.n_272').html('<rect id="n_272" rx="0" ry="0" x="0" y="0" width="1024" height="'+height+'"></rect>');
    $('#index').css('height',String(height)+'px');
    $('svg.n_272').html('<rect id="n_272" rx="0" ry="0" x="0" y="0" width="1024" height="2097"></rect>')
    $('span#n_11__text').text("生徒のキャリアパスポート一覧");
    $('div#n_11__').css("left","79px");
    $('div#n_11__').css("width","357px");
    $('div#n_15').hide();
    //$('a').click(function(){
    //    return false;
    //});
});