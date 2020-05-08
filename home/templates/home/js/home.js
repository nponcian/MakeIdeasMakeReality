$(document).ready(function() {

$("#welcomeMessage").html(initialWelcome);
// or
// document.getElementById('welcomeMessage').innerHTML = initialWelcome;

$('#welcomeMessage').hover(
    function() {
        greetingsTracker %= greetings.length;

        var htmlContent = greetings[greetingsTracker][0];
        var bgImage = greetings[greetingsTracker][1];
        $(this).html(htmlContent);
        $("#welcomeMessage").css('background-image', 'url("' + bgImage + '")');
        $("#welcomeMessage").css('background-size', 'contain'); // fit flags and repeat
        ++greetingsTracker;

        if (!isInitialWelcomeUpdated && greetingsTracker >= greetings.length)
        {
            initialWelcome =  initialWelcomeUpdated;
            isInitialWelcomeUpdated = true;
        }
    },
    function() {
        $(this).html(initialWelcome);
        $("#welcomeMessage").css('background-image', 'url("")');
    });

});

var initialWelcome = "Hey! Surprises are coming when you hover in and out of here!";
var initialWelcomeUpdated = "No more surprises!";
var isInitialWelcomeUpdated = false;
var greetingsTracker = 0
var greetings = [
    [ // English
        '\
            <p class="bg-secondary p-2">\
                Ready to pay nothing? Navigate to the\
                <a href="/service/" class="border-bottom border-top border-warning text-warning">services</a>\
                now!\
            </p>\
        ',
        "https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg"
    ],
    [ // Espanol
        '\
            <p class="bg-secondary p-2">\
                ¿Estas lista para pagar nada? Obtenga mas informacion sobre el\
                <a href="/about/mimr/" class="border-bottom border-top border-warning text-warning">proyecto</a>!\
            </p>\
        ',
        "https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Flag_of_Spain.svg/1200px-Flag_of_Spain.svg.png"
    ],
    [ // Deutsch
        '\
            <p class="bg-secondary p-2">\
                Bist du bereit nichts zu bezahlen? Erfahren Sie mehr uber\
                <a href="/about/whoami/" class="border-bottom border-top border-warning text-warning">uns</a>!\
            </p>\
        ',
        "https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/1200px-Flag_of_Germany.svg.png"
    ],
    [ // Tagalog
        '\
            <p class="bg-secondary p-2">\
                Handa ka na bang hindi magbayad? Alamin ang\
                <a href="https://github.com/nponcian/makeIdeasMakeReality" class="border-bottom border-top border-warning text-warning">algoritmo</a>\
                sa likod ng pagina!\
            </p>\
        ',
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Flag_of_the_Philippines.svg/1200px-Flag_of_the_Philippines.svg.png"
    ],
];
