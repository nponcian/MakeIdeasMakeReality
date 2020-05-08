$(document).ready(function() {
    $(function() {
        $('[data-toggle="popover"]').popover();
    });
    $('[data-toggle="popover"][data-timeout]').on('shown.bs.popover', function() {
        this_popover = $(this);
        setTimeout(function() {
            this_popover.popover('hide');
        }, $(this).data("timeout"));
    });
});
