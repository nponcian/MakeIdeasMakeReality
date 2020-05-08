$(document).ready(function() {

$("#welcomeMessage").html(welcomeGreeting);
// or
// document.getElementById('welcomeMessage').innerHTML = welcomeGreeting;

$('#welcomeMessage').hover(
    function() {
        languageTracker = languageTracker % welcomeLanguages.length;
        $(this).html(welcomeLanguages[languageTracker]);
        ++languageTracker;
    },
    function() {
        $(this).html(welcomeGreeting);
    });

});

var languageTracker = 0
var welcomeGreeting = "Hey! Surprises are coming when you hover in and out of here!";
var welcomeLanguages = [
// var englishWelcome =
    '\
        <p>\
            Ready to pay nothing? Navigate to the\
            <a href="/service/" class="border-bottom border-top border-warning text-warning">services</a>\
            now!\
        </p>\
    ',
// var espanolWelcome =
    '\
        <p>\
            ¿Estas lista para no pagar nada? Navega a los\
            <a href="/service/" class="border-bottom border-top border-warning text-warning">servicios</a>\
            ahora!\
        </p>\
    ',
// var deutschWelcome =
    '\
        <p>\
            Bist du bereit nichts zu bezahlen? Navigieren Sie jetzt zu den \
            <a href="/service/" class="border-bottom border-top border-warning text-warning">Diensten</a>!\
        </p>\
    '
];
