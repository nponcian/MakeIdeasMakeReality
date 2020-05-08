$(document).ready(function() {
    // Enable popover elements
    $(function() {
        $('[data-toggle="popover"]').popover();
    });

    // Support timeout on popovers
    $('[data-toggle="popover"][data-timeout]').on('shown.bs.popover', function() {
        this_popover = $(this);
        setTimeout(function() {
            this_popover.popover('hide');
        }, $(this).data("timeout"));
    });
});
