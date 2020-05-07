$(document).ready(function() {
    // Slide the carousel upon button click
    //     .carousel('prev') - Cycles to the previous item
    //     .carousel('next') - Cycles to the next item.
    // Reference: https://getbootstrap.com/docs/4.4/components/carousel/#methods
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

    // When a slide occurs, pause the current iframe video that is playing
    // player.pauseVideo():Void - Pauses the currently playing video.
    // Reference: https://developers.google.com/youtube/iframe_api_reference#Playback_controls
    $('#moviesCarousel').on('slide.bs.carousel', function(event) {
        // The variable "players" contain each Youtube Player for each iframe video
        // Reference: https://developers.google.com/youtube/iframe_api_reference#Loading_a_Video_Player
        // event.from - The index of the current video (before the slide occurs)
        //            - It is also the index of the corresponding player for the current video
        // Reference: https://getbootstrap.com/docs/4.4/components/carousel/#events
        players[event.from].pauseVideo();
    });
});

// Start of snippet
//     YouTube Player API Reference for iframe Embeds
//     https://developers.google.com/youtube/iframe_api_reference
// 2. This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.
var players = []; // would contain 1 player for each iframe video
function onYouTubeIframeAPIReady() {
    var allMovieIframes = document.getElementById("moviesCarousel").getElementsByTagName('iframe');
    for (currentIFrame of allMovieIframes)
    {
        players.push(new YT.Player(
            currentIFrame.id, // the target iframe video
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
function onPlayerStateChange(event) { // triggered everytime ANY iframe video player among the "players" list is played, paused, ended, etc.
    // if (event.data == YT.PlayerState.PLAYING && !done) {
    //     setTimeout(stopVideo, 6000);
    //     done = true;
    // Check if any iframe video is being played (or is currently buffering to be played)
    // Reference: https://developers.google.com/youtube/iframe_api_reference#Events
    if (event.data == YT.PlayerState.PLAYING || event.data == YT.PlayerState.BUFFERING) {
        // If any player has been detected to be currently playing or buffering, pause the carousel from sliding
        // .carousel('pause') - Stops the carousel from cycling through items.
        // Reference: https://getbootstrap.com/docs/4.4/components/carousel/#methods
        $('#moviesCarousel').carousel('pause');
    }
    else
    {
        // If there are no currently playing nor buffering videos, resume the sliding of the carousel.
        // This means that once the current video is in a state that is not playing (aside from buffering), either it was:
        //     1. paused intentionally
        //     2. paused as an effect of a slide
        //     3. video has ended
        //     4. wasn't totally played from the start
        //     5. and literally any form where the video timer isn't running ;)
        //     - then the carousel would now resume sliding.
        $('#moviesCarousel').carousel();
    }
}
function stopVideo() {
    // player.stopVideo();
}
// End of snippet from Youtube iframe API
