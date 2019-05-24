$('.back').css('visibility', 'hidden');

$('#rotatefront').click(() => {
    $('.front').css('visibility', 'hidden');
    $('.back').css('visibility', 'visible');
});

$('#rotateback').click(() => {
    $('.back').css('visibility', 'hidden');
    $('.front').css('visibility', 'visible');
});
