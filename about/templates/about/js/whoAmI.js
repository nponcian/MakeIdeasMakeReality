$(document).ready(function () {
    // $('#moviesCarouselControl #prevMovie').on('click', function(){
    //     $('#moviesCarousel').carousel('prev');
    // });
    // $('#moviesCarouselControl #nextMovie').on('click', function(){
    //     $('#moviesCarousel').carousel('next');
    // });
    $('#moviesCarouselControl').on('click', '.btn', function(){
        var targetOperation = $(this).val();
        $('#moviesCarousel').carousel(targetOperation);
    });
});
