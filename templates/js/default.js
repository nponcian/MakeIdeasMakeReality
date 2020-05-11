$(document).ready(function() {

// Enable popover elements
$(function() {
    $('[data-toggle="popover"]').popover();
});

// Support timeout on popover elements
$('[data-toggle="popover"][data-timeout]').on('shown.bs.popover', function() {
    this_popover = $(this);
    setTimeout(function() {
        this_popover.popover('hide');
    }, $(this).data("timeout"));
});

// Enable copying of target element contents
$('.mimr-btn-copy').on('click', function() {
    /* Get the text field */
    var toCopy = $(this).data("target");
    var copyText = document.getElementById(toCopy);

    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /*For mobile devices*/

    /* Copy the text inside the text field */
    document.execCommand("copy");

    // Deselect the text
    copyText.blur();

    /* Alert the copied text */
    // alert("Copied the text: " + copyText.value); // I replaced this with popover
});

// Display selected filename when using Bootstrap custom-file-input
// This requires that the order of elements should be custom-file-input then custom-file-label
$('.custom-file-input').on('change', function() {
   let fileName = $(this).val().split('\\').pop();
   $(this).next('.custom-file-label').addClass("selected").html(fileName);
});

$('.serviceForm').on('submit', function(event) {
    event.preventDefault(); // prevent redirecting post request to server
    var formData = new FormData(this); // new FormData($("#serviceForm")[0])
    var urlValue = $(this).data("url"); // "/service/text/commonword/api/"
    var resultObj = $(this).data("result");

    $.ajax({
        url: urlValue,
        type: "post",

        // headers: {'Authorization' : 'JWT sometoken'},
        data: formData,
        // data: $('.serviceForm').serialize(),
        // data: JSON.stringify( { "first-name": $('#first-name').val(), "last-name": $('#last-name').val() } ),

        crossDomain: true,
        processData: false,
        contentType: false, // 'application/json'
        // dataType: 'json',

        beforeSend: function(jqXHR, settings) {
            console.log("Processing request...");
            $(resultObj).text("Currently processing...");
        },
        success: function(data, textStatus, jqXHR){
            console.log("Request successful; textStatus:", textStatus);
            var dataStr = "";

            // $.each(data, function(index, object) {
            //     $.each(object, function(word, count) {
            //         dataStr += word + " : " + count + "\n";
            //     });
            // });
            // or
            for (var index = 0; index < data.length; ++index) {
                for (var key in data[index]) {
                    dataStr += key + " : " + data[index][key] + "\n";
                }
            }

            $(resultObj).text(dataStr);
        },
        error: function(jqXHR, textStatus, errorThrown){
            var msg = "Request error; textStatus: " + textStatus + " ; errorThrown: " + errorThrown;
            console.log(msg);
            $(resultObj).text(msg);
        },
    })
    // would only be called if there are no errors with the HTTP Request
    .done(function(data, textStatus, jqXHR) {
            console.log("Request done; textStatus:", textStatus); // alert("Request processing done");
        })
    // if something went wrong with the HTTP request, like if server has no response, resource does
    // not exist, rejected request, etc.
    .fail(function(jqXHR, textStatus, errorThrown) {
            // error types are timeout, error, abort, parseerror
            console.log("Request failed; textStatus:", textStatus, "; errorThrown:", errorThrown);
        })
    // would be called whether the HTTP Request was successful or not
    .always(function(data) { // data|jqXHR, textStatus, jqXHR|errorThrown
            console.log("Request ended");
        });
    });

});
