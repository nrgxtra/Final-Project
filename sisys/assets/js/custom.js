(function($) {
    'use strict';

    // Mean Menu JS
    jQuery('.mean-menu').meanmenu({ 
        meanScreenWidth: "991"
    });

    // Navbar Area
    $(window).on('scroll', function() {
        if ($(this).scrollTop() >150){  
            $('.navbar-area').addClass("is-sticky");
        }
        else{
            $('.navbar-area').removeClass("is-sticky");
        }
    });

    // Banner Slider
	$('.banner-slider').owlCarousel({
		loop:true,
		margin: 30,
		nav: true,
		mouseDrag: true,
        items:1,
		dots: false,
		autoHeight: true,
		autoplay: false,
		smartSpeed:1500,
        autoplayHoverPause: true,
        navText: [
            "<i class='flaticon-arrow-pointing-to-left'></i>",
            "<i class='flaticon-arrow-pointing-to-right'></i>"
        ],
    });

    // About Slider
	$('.about-slider').owlCarousel({
		loop:true,
		margin: 30,
		nav: false,
		mouseDrag: true,
        items:1,
		dots: true,
		autoHeight: true,
		autoplay: false,
		smartSpeed:1500,
        autoplayHoverPause: true,
    });

    // Testimonial Slider
	$('.testimonial-slider').owlCarousel({
		loop:true,
		margin: 30,
		nav: false,
		mouseDrag: true,
        items: 1,
		dots: false,
		autoHeight: true,
		autoplay: false,
		smartSpeed:1500,
        autoplayHoverPause: true,
        responsive:{
            0:{
                items: 1,
                center: false,
            },
            576:{
                items: 2,
                center: false,
            },
            1000:{
                items: 3,
                center:  true,
            }
        },
    });

    // Testimonial Slider Two
	$('.testimonial-slider-two').owlCarousel({
		loop:true,
		margin: 30,
		nav: false,
		mouseDrag: true,
		dots: false,
		autoHeight: true,
		autoplay: false,
		smartSpeed:1500,
        autoplayHoverPause: true,
        responsive:{
            0:{
                items: 1,
            },
            1000:{
                items: 2,
            }
        },
    });

    // Testimonial Slider Two
	$('.testimonial-slider-three').owlCarousel({
		loop:true,
		margin: 30,
		nav: true,
		mouseDrag: true,
		dots: false,
		autoHeight: true,
		autoplay: false,
		smartSpeed:1500,
        autoplayHoverPause: true,
        responsive:{
            0:{
                items: 1,
            },
            1000:{
                items: 2,
                center: true,
            }
        },
        navText: [
            "<i class='flaticon-arrow-pointing-to-left'></i>",
            "<i class='flaticon-arrow-pointing-to-right'></i>"
        ],
    });

    // Services Slider
	$('.services-slider').owlCarousel({
		loop:true,
		margin: 30,
		nav: true,
		mouseDrag: true,
		dots: false,
		autoHeight: true,
		autoplay: false,
		smartSpeed:1500,
        autoplayHoverPause: true,
        responsive:{
            0:{
                items: 1,
                center: false,
            },
            576:{
                items: 2,
                center: false,
            },
            1000:{
                items: 3,
                center:  true,
            }
        },
        navText: [
            "<i class='flaticon-arrow-pointing-to-left'></i>",
            "<i class='flaticon-arrow-pointing-to-right'></i>"
        ],
    });

    // Blog Preview Slider
	$('.blog-preview-slider').owlCarousel({
		loop:true,
		margin: 30,
		nav: true,
		mouseDrag: true,
		dots: false,
        items: 1,
		autoHeight: true,
		autoplay: false,
		smartSpeed:1500,
        autoplayHoverPause: true,
        navText: [
            "<i class='flaticon-arrow-pointing-to-left'></i>",
            "<i class='flaticon-arrow-pointing-to-right'></i>"
        ],
    });

    // Range Slider

    // Tabs Single Page
    $('.tab ul.tabs').addClass('active').find('> li:eq(0)').addClass('current');
    $('.tab ul.tabs li').on('click', function (g) {
        var tab = $(this).closest('.tab'), 
        index = $(this).closest('li').index();
        tab.find('ul.tabs > li').removeClass('current');
        $(this).closest('li').addClass('current');
        tab.find('.tab_content').find('div.tabs_item').not('div.tabs_item:eq(' + index + ')').slideUp();
        tab.find('.tab_content').find('div.tabs_item:eq(' + index + ')').slideDown();
        g.preventDefault();
    });

    // FAQ Accordion JS
	$('.accordion').find('.accordion-title').on('click', function(){
		// Adds Active Class
		$(this).toggleClass('active');
		// Expand or Collapse This Panel
		$(this).next().slideToggle('fast');
		// Hide The Other Panels
		$('.accordion-content').not($(this).next()).slideUp('fast');
		// Removes Active Class From Other Titles
		$('.accordion-title').not($(this)).removeClass('active');		
    });

    // Datetimepicker
    $('#datetimepicker').datepicker();

    // Datetimepicker
    $('#datetimepicker2').datepicker();

     // Newsletter modal

    // Popup Video 
    $('.play-btn').magnificPopup({
        disableOn: 0,
        type: 'iframe',
        mainClass: 'mfp-fade',
        removalDelay: 160,
        preloader: false,
        fixedContentPos: false
    });

    // Input Plus & Minus Number JS
    $('.input-counter').each(function() {
        var spinner = jQuery(this),
        input = spinner.find('input[type="text"]'),
        btnUp = spinner.find('.plus-btn'),
        btnDown = spinner.find('.minus-btn'),
        min = input.attr('min'),
        max = input.attr('max');
        
        btnUp.on('click', function() {
            var oldValue = parseFloat(input.val());
            if (oldValue >= max) {
                var newVal = oldValue;
            } else {
                var newVal = oldValue + 1;
            }
            spinner.find("input").val(newVal);
            spinner.find("input").trigger("change");
        });

        btnDown.on('click', function() {
            var oldValue = parseFloat(input.val());
            if (oldValue <= min) {
                var newVal = oldValue;
            } else {
                var newVal = oldValue - 1;
            }
            spinner.find("input").val(newVal);
            spinner.find("input").trigger("change");
        });
    }); 

    // Count Time JS

    // Back To Top
    $('body').append("<div class='go-top'><i class='flaticon-navigate-up-arrow'></i></div>");
    $(window).on('scroll', function() {
        var scrolled = $(window).scrollTop();
        if (scrolled > 600) $('.go-top').addClass('active');
        if (scrolled < 600) $('.go-top').removeClass('active');
    });
    $('.go-top').on('click', function() {
        $('html, body').animate({
            scrollTop: '0',
        }, 500 );
    });

    // Preloader
    $(window).on("load", function() {
        var preLoder = $(".loader-wrapper");
        preLoder.delay(700).fadeOut(500);
        $("body").addClass("loaded");
    });

    // AOS JS
	AOS.init();

    // TweenMax JS
	$('.banner-area').mousemove(function(e){
		var wx = $(window).width();
		var wy = $(window).height();
		var x = e.pageX - this.offsetLeft;
		var y = e.pageY - this.offsetTop;
		var newx = x - wx/2;
		var newy = y - wy/2;
		$('.banner-img').each(function(){
			var speed = $(this).attr('data-speed');
			if($(this).attr('data-revert')) speed *= -.4;
			TweenMax.to($(this), 1, {x: (1 - newx*speed), y: (1 - newy*speed)});
		});
	});

    // TweenMax JS
	$('.banner-area-two').mousemove(function(e){
		var wx = $(window).width();
		var wy = $(window).height();
		var x = e.pageX - this.offsetLeft;
		var y = e.pageY - this.offsetTop;
		var newx = x - wx/2;
		var newy = y - wy/2;
		$('.banner-img-two, .banner-vector').each(function(){
			var speed = $(this).attr('data-speed');
			if($(this).attr('data-revert')) speed *= -.4;
			TweenMax.to($(this), 1, {x: (1 - newx*speed), y: (1 - newy*speed)});
		});
	});

    // TweenMax JS
	$('.intro-video-bg').mousemove(function(e){
		var wx = $(window).width();
		var wy = $(window).height();
		var x = e.pageX - this.offsetLeft;
		var y = e.pageY - this.offsetTop;
		var newx = x - wx/2;
		var newy = y - wy/2;
		$('.video-content-two').each(function(){
			var speed = $(this).attr('data-speed');
			if($(this).attr('data-revert')) speed *= -.4;
			TweenMax.to($(this), 1, {x: (1 - newx*speed), y: (1 - newy*speed)});
		});
	});

   
    // Switch Btn
    $('body').append("<div class='switch-box'><label id='switch' class='switch'><input type='checkbox' onchange='toggleTheme()' id='slider'><span class='slider round'></span></label></div>");

})(jQuery);

// function to set a given theme/color-scheme
function setTheme(themeName) {
    localStorage.setItem('naon_theme', themeName);
    document.documentElement.className = themeName;
}

// function to toggle between light and dark theme
function toggleTheme() {
    if (localStorage.getItem('naon_theme') === 'theme-dark') {
        setTheme('theme-light');
    } else {
        setTheme('theme-dark');
    }
}

// Immediately invoked function to set the theme on initial load
(function () {
    if (localStorage.getItem('naon_theme') === 'theme-dark') {
        setTheme('theme-dark');
        document.getElementById('slider').checked = false;
    } else {
        setTheme('theme-light');
      document.getElementById('slider').checked = true;
    }
})();
