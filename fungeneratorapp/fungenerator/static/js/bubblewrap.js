$(function() {
    var bubblewrap_amount = 3;

    function getWrap() {
        if(bubblewrap_amount > 0) {
            bubblewrap_amount --;
            $('#wrap_amount').text(bubblewrap_amount);
        }

        if(bubblewrap_amount == 0) {
            console.log('aa');
            $('#get_wrap').addClass('disabled');
            $('#bubblewrap_alert').fadeIn();
        }
    }

    function loadWrap() {
        bubblewrap_amount = 3;
        $('#wrap_amount').text(bubblewrap_amount);
        $('#get_wrap').removeClass('disabled');
        $('#bubblewrap_alert').fadeOut();
    }

    if(bubblewrap_amount == 0 && $('#bubblewrap_cat').length) {
        $('#bubblewrap_cat').addClass('disabled');
    }

    $('#get_wrap').on('click', getWrap);
    $('#empty_wrap').on('click', loadWrap);
});