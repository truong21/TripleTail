$('.btn-clear').on('click', () => {
  if ($('body').hasClass('black'))
  {
    $('body').removeClass('black');
    $('body').addClass('blue');
  }
  else
  {
    $('body').removeClass('blue');
    $('body').addClass('black');
  }
});

