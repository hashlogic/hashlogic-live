    new WOW().init();

(function ($) {

   'use strict';

    /*
     * ----------------------------------------------------------------------------------------
     *  SMOTH SCROOL JS
     * ----------------------------------------------------------------------------------------
     */

    $('a.smoth-scroll').on('click', function (e) {
        var anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $(anchor.attr('href')).offset().top - 50
        }, 1000);
        e.preventDefault();
    });

	  

    /* ==========================================================================
      COUNTER UP details.open = true
 ========================================================================== */

    $('.counter').counterUp({
        delay: 10,
        time: 1000
    });

    $('.carousel').carousel({
      interval: 8000
    });
    
    /* Closes the Responsive Menu on Menu Item Click*/
    $('.navbar-collapse .navbar-nav a').on('click', function () {
        $('.navbar-toggler:visible').click();
    });
    /*END MENU JS*/

    
    /* ----------------------------------------------------------- */
    /*  Fixed header
    /* ----------------------------------------------------------- */


    $(window).on('scroll', function () {
        if ($(window).scrollTop() > 70) {
            $('.site-navigation,.trans-navigation').addClass('header-white');
        } else {
            $('.site-navigation,.trans-navigation').removeClass('header-white');
        }



    });


    /* ==========================================================================
      SCROLL SPY
 ========================================================================== */

    $('body').scrollspy({
        target: '.navbar-collapse',
        offset: 195
    });






          /*START GOOGLE MAP*/
          function initialize() {
            var mapOptions = {
              zoom: 15,
              scrollwheel: false,
              center: new google.maps.LatLng(40.7127837, -74.00594130000002)
            };
            var map = new google.maps.Map(document.getElementById('map'),
                mapOptions);
            var marker = new google.maps.Marker({
              position: map.getCenter(),
              icon: 'assets/img/map_pin.png',
              map: map
            });
          }
          google.maps.event.addDomListener(window, 'load', initialize);	
          /*END GOOGLE MAP*/	


})(window.jQuery);

/* ==========================================================================
      My code
	  
	  
	  
	  $("#test").on("mouseover", function () {
					document.getElementById("test").open = true
    }).on("mouseout", function () {
				  document.getElementById("test").open = false
					
	})
	
	function drop(){
	img_id = $(this).attr('id');
	img_id.open = true
}
function pick(){
	img_id = $(this).attr('id');
	img_id.open = false
}


const cbox = document.querySelectorAll(".box");

 for (let i = 0; i < cbox.length; i++) {
     cbox[i].addEventListener("click", function() {
       cbox[i].classList.toggle("red");
     });
 }
 
 document.querySelectorAll("details").on("mouseover", function () {
					img_id = $(this).attr('id');
					console.log(img_id);
    })
	
	const cbox = document.querySelectorAll("details");

 for (let i = 0; i < cbox.length; i++) {
     cbox[i].addEventListener("mouseover", function() {
		 var id = $(cbox[i]).attr("ID");
		 document.getElementById(id).open = true
       console.log("over");
	   console.log(id);
	   
     });
	 cbox[i].addEventListener("mouseout", function() {
		 var id = $(cbox[i]).attr("ID");
         document.getElementById(id).open = false
		 console.log("out");
	   console.log(id);
     });
 }
 
 ========================================================================== */
