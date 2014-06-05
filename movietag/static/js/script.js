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
});
