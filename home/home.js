$(function() {

  setTimeout(function() {
    $('#welcome').fadeIn('slow');
  }, 2000);

  setTimeout(function() {
    $('#q-wrapper').animate({
      top: '90%'
    }, 'slow');
  }, 3000).scrollTop();
/*
  $('.fa-chevron-down').click(function() {
    $(this).scrollTop('90%');
  });
*/
});
