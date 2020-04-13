$(function() {


  setTimeout(function() {

    $('#bg-color').fadeIn('slow');
    $('#welcome').fadeIn('slow');
    $('#scroll0').fadeIn('slow');

  }, 2000);


  $('.scroll').click(function() {

    var scrollPosition = $(this).offset().top + $(this).height() + $(window).height() * 0.05;

    $('html, body').animate({
      scrollTop: scrollPosition
    }, 'slow', 'easeOutQuart');

  });


});
