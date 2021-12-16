$(function(){
    $('div#load').hide();
    $('div#content').show();
    $('svg.n_272').html('<rect id="n_272" rx="0" ry="0" x="0" y="0" width="1024" height="700"></rect>')
    var student_detail=$('div#student_detail').html();
    $('span#n_11__text').text(student_detail);
    $('div#n_11__').css("left","79px");
    $('div#n_11__').css("width","357px");
    $('div#n_15').hide();
});