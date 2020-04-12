$(function() {


  setTimeout(function() {

    $('#bg-color').fadeIn('slow');
    $('#welcome').fadeIn('slow');
    $('#scroll1').fadeIn('slow');

  }, 2000);


  $('#scroll1').click(function() {

    $('html, body').animate({
      scrollTop: $(this).offset().top + $(this).height()
      // scrollTop: '750vh'  // なぜ770vh？
    }, 'slow', 'easeOutQuart');

  });


  $('.scroll').click(function() {

    $('html, body').animate({
      scrollTop: $(this).offset().top + $(this).outerHeight(true)
    }, 'slow', 'easeOutQuart');

  });


});
