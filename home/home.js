$(function() {


  setTimeout(function() {

    $.when(
      $('#welcome').fadeIn('slow')
    ).done(function() {
      $('#scroll1').fadeIn('slow');
    });

  }, 2000);


  $('#scroll1').click(function() {
    $('html, body').animate({
      // scrollTop: $('#q-wrapper').offset().top
      scrollTop: '750vh'  // なぜ770vh？
    }, 'slow');
  });


});
