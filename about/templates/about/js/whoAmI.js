$(document).ready(function() {
    // $('#moviesCarouselControl #prevMovie').on('click', function(){
    //     $('#moviesCarousel').carousel('prev');
    // });
    // $('#moviesCarouselControl #nextMovie').on('click', function(){
    //     $('#moviesCarousel').carousel('next');
    // });
    $('#moviesCarouselControl').on('click', '.btn', function(){
        var PREV_VAL = "prev";
        var NEXT_VAL = "next";

        var targetOperation = $(this).val();
        $('#moviesCarousel').carousel(targetOperation);

        players[currentPlayer].pauseVideo();
        var firstPlayer = 0;
        var lastPlayer = players.length - 1;
        if (targetOperation == PREV_VAL)
        {
            --currentPlayer;
            if (currentPlayer < firstPlayer) currentPlayer = lastPlayer;
        }
        else if (targetOperation == NEXT_VAL)
        {
            ++currentPlayer;
            if (currentPlayer > lastPlayer) currentPlayer = firstPlayer;
        }
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
var currentPlayer = 0;
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
    // }
}
function stopVideo() {
    // player.stopVideo();
}
// End: YouTube Player API Reference for iframe Embeds
