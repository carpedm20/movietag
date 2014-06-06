$( document ).ready(function() {
  var $container = $('.content');

  $(this).find(".poster a.frame").twipsy({delayIn:1500,offset:1});

  $('.raty').raty({
    path: '/static',
    score: function() {
      return $(this).attr('data-score');
    }
  });
});
