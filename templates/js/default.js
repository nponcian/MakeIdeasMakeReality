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
});
