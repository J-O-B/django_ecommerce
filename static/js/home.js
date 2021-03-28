window.onload = function() {
    if(!window.location.hash) {
        window.location = window.location + '#loaded';
        window.location.reload();
    }
}

$(document).ready(function(){

    if($('.brands_slider').length){
        let brandsSlider = $('.brands_slider');

        brandsSlider.owlCarousel({
            loop:true,
            autoplay:true,
            autoplayTimeout:5000,
            nav:false,
            dots:false,
            autoWidth:true,
            items:8,
            margin:42
        });

        if($('.brands_prev').length){
            let prev = $('.brands_prev');
            prev.on('click', function(){
            brandsSlider.trigger('prev.owl.carousel');
            });
        }

        if($('.brands_next').length){
            let next = $('.brands_next');
            next.on('click', function(){
                brandsSlider.trigger('next.owl.carousel');
            });
        }
    }
    // Initial Visibilities
    $('#security').hide();
    $('#prodRange').hide();
    $('#howItWorks').hide();
    $('#page-content').hide();
});

$(window).scroll(function() {
    let top_of_element = ($("#page-content").offset().top) + 500;
    let bottom_of_element = $("#page-content").offset().top + $("#page-content").outerHeight();
    let bottom_of_screen = $(window).scrollTop() + $(window).innerHeight();
    let top_of_screen = $(window).scrollTop();

    if ((bottom_of_screen > top_of_element) && (top_of_screen < bottom_of_element)){
        $('#page-content').fadeIn(1500);
    } else {
        // Pass
    }
});


// Click functions
$('#showabout').click(function(){
    $('#about-us').siblings().hide(900).then($('#about-us').fadeIn(500));    
});
$('#showsecurity').click(function(){
    $('#security').siblings().hide(900).then($('#security').fadeIn(900));
});
$('#showProdRange').click(function(){
    $('#prodRange').siblings().hide(900).then($('#prodRange').fadeIn(900));
});
$('#showHow').click(function(){
    $('#howItWorks').siblings().hide(900).then($('#howItWorks').fadeIn(900));
});
$('.show-how-it-works').click(function(){
    $('#showHow').trigger('click');
});