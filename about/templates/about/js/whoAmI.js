$(document).ready(function() {
    // $('#moviesCarouselControl #prevMovie').on('click', function(){
    //     $('#moviesCarousel').carousel('prev');
    // });
    // $('#moviesCarouselControl #nextMovie').on('click', function(){
    //     $('#moviesCarousel').carousel('next');
    // });
    $('#moviesCarouselControl').on('click', '.btn', function() {
        var targetOperation = $(this).val();
        $('#moviesCarousel').carousel(targetOperation);
    });

    $('#moviesCarousel').on('slide.bs.carousel', function(event) {
        players[event.from].pauseVideo();
    });
});

// Start: YouTube Player API Reference for iframe Embeds
// 2. This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.
var players = [];
function onYouTubeIframeAPIReady() {
    var allMovieIframes = document.getElementById("moviesCarousel").getElementsByTagName('iframe');
    for (currentIFrame of allMovieIframes)
    {
        players.push(new YT.Player(
            currentIFrame.id,
            { events: { 'onReady': onPlayerReady, 'onStateChange': onPlayerStateChange } }));
    }
}
// 4. The API will call this function when the video player is ready.
function onPlayerReady(event) {
    // event.target.playVideo();
}
// 5. The API calls this function when the player's state changes.
//    The function indicates that when playing a video (state=1),
//    the player should play for six seconds and then stop.
// var done = false;
function onPlayerStateChange(event) {
    // if (event.data == YT.PlayerState.PLAYING && !done) {
    //     setTimeout(stopVideo, 6000);
    //     done = true;
    if (event.data == YT.PlayerState.PLAYING || event.data == YT.PlayerState.BUFFERING) {
        $('#moviesCarousel').carousel('pause');
    }
    else
    {
        $('#moviesCarousel').carousel();
    }
}
function stopVideo() {
    // player.stopVideo();
}
// End: YouTube Player API Reference for iframe Embeds
