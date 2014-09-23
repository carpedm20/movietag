$('#search').submit(function() {
  location.href="http://minsky.unist.ac.kr:8002/m/search/" + $("#search-text")[0].value;
  return false;
});

$( document ).ready(function() {
  var $container = $('.content');

  $container.imagesLoaded( function() {
    $container.masonry({
      itemSelector        : '.poster',
      columnWidth         : '.poster',
      transitionDuration  : 0
    });
  });

  $(this).find(".poster a.frame").twipsy({delayIn:1500,offset:1});

  $('.raty').raty({
    path: '/static',
    score: function() {
      return $(this).attr('data-score');
    }
  });
});
