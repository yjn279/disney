$(function() {


  var questions = 6;

  for (var i = 1; i <= questions; i++) {
    $(`#q${i}`).load(`q${i}.html`);
  }


  setTimeout(function() {

    // $('#bg-color').fadeIn('slow');
    $('#welcome').fadeIn('slow');
    // $('#welcome').css('display', 'inline-block');
    $('#scroll0').fadeIn('slow');

  }, 2000);


  $('.scroll').click(function() {

    var scrollPosition = $(this).offset().top + $(this).height() + $(window).height() * 0.05;

    $('html, body').animate({
      scrollTop: scrollPosition
    }, 'slow', 'easeOutQuart');


  });


});
