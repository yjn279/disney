$(function() {

  setTimeout(function() {

      $('#stand-by').fadeOut('fast');

      $('#main-lower').fadeIn(1500).animate({
        height: '40%',
        'border-color': '#fff'
      }, 1500);

    }, 2000);

  });
