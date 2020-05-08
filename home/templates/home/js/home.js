$(document).ready(function() {

$("#welcomeMessage").html(initialWelcome);
// or
// document.getElementById('welcomeMessage').innerHTML = initialWelcome;

$('#welcomeMessage').hover(
    function() {
        greetingsTracker %= greetings.length;
        $(this).html(greetings[greetingsTracker]);
        ++greetingsTracker;

        if (!isInitialWelcomeUpdated && greetingsTracker >= greetings.length)
        {
            initialWelcome =  initialWelcomeUpdated;
            isInitialWelcomeUpdated = true;
        }
    },
    function() {
        $(this).html(initialWelcome);
    });

});

var initialWelcome = "Hey! Surprises are coming when you hover in and out of here!";
var initialWelcomeUpdated = "No more surprises!";
var isInitialWelcomeUpdated = false;
var greetingsTracker = 0
var greetings = [
    // English
    '\
        <p>\
            Ready to pay nothing? Navigate to the\
            <a href="/service/" class="border-bottom border-top border-warning text-warning">services</a>\
            now!\
        </p>\
    ',
    // Espanol
    '\
        <p>\
            ¿Estas lista para pagar nada? Obtenga mas informacion sobre el\
            <a href="/about/mimr/" class="border-bottom border-top border-warning text-warning">proyecto</a>!\
        </p>\
    ',
    // Deutsch
    '\
        <p>\
            Bist du bereit nichts zu bezahlen? Erfahren Sie mehr uber\
            <a href="/about/whoami/" class="border-bottom border-top border-warning text-warning">uns</a>!\
        </p>\
    ',
    // Tagalog
    '\
        <p>\
            Handa ka na bang hindi magbayad? Alamin ang\
            <a href="https://github.com/nponcian/makeIdeasMakeReality" class="border-bottom border-top border-warning text-warning">algoritmo</a>\
            sa likod ng pagina na ito!\
        </p>\
    ',
];
