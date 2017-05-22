$(function() {
    $('.slider').not('.slick-initialized').each(function(i, e) {
        $(e).slick({
            infinite: true,
            speed: 300,
            slidesToShow: 1,
            adaptiveHeight: true,
            dots: false
        });
    });
});