(function ($) {
 "use strict";	

/*----------------------------

 wow js active

------------------------------ */

 new WOW().init();
 

/*----------------------------

 Practice Area

------------------------------ */  
  $(".practice-section").owlCarousel({

      autoPlay: false, 

	  slideSpeed:2000,

	  pagination:false,

	  navigation:true,	  

      items : 5,

	  /* transitionStyle : "fade", */    /* [This code for animation ] */

	  navigationText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],

      itemsDesktop : [1199,4],

	  itemsDesktopSmall : [980,3],

	  itemsTablet: [768,2],

	  itemsMobile : [479,1],

  }); 

/*----------------------------

 Happy Client Area

------------------------------ */  

  $(".client-section").owlCarousel({

      autoPlay: false, 

	  slideSpeed:2000,

	  pagination:false,

	  navigation:true,	  

      items : 3,

	  /* transitionStyle : "fade", */    /* [This code for animation ] */

	  navigationText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],

      itemsDesktop : [1199,3],

	  itemsDesktopSmall : [980,3],

	  itemsTablet: [768,2],

	  itemsMobile : [479,1],

  }); 

/*----------------------------
Our Attorney
------------------------------ */  

  $(".our-attorney").owlCarousel({

      autoPlay: false, 

	  slideSpeed:2000,

	  pagination:true,

	  navigation:false,	  

      items : 3,

	  /* transitionStyle : "fade", */    /* [This code for animation ] */

	  navigationText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],

      itemsDesktop : [1199,3],

	  itemsDesktopSmall : [980,3],

	  itemsTablet: [768,2],

	  itemsMobile : [479,1],

  });

/*----------------------------

 Partner Logo

------------------------------ */  

  $(".client-logo").owlCarousel({

      autoPlay: false, 

	  slideSpeed:2000,

	  pagination:false,

	  navigation:true,	  

      items : 5,

	  /* transitionStyle : "fade", */    /* [This code for animation ] */

	  navigationText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],

      itemsDesktop : [1199,5],

	  itemsDesktopSmall : [980,3],

	  itemsTablet: [768,2],

	  itemsMobile : [479,1],

  }); 

/*----------------------------

	Service Section Area

------------------------------ */  

  $(".service-section").owlCarousel({

      autoPlay: false, 

	  slideSpeed:2000,

	  pagination:false,

	  navigation:true,	  

      items : 5,

	  /* transitionStyle : "fade", */    /* [This code for animation ] */

	  navigationText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],

      itemsDesktop : [1199,5],

	  itemsDesktopSmall : [980,3],

	  itemsTablet: [768,2],

	  itemsMobile : [479,1],

  });     

/*----------------------------

	Testimonial Section Area

------------------------------ */  

  $(".testimonial").owlCarousel({

      autoPlay: true, 

	  slideSpeed:2000,

	  pagination:true,

	  navigation:false,	  

      items : 1,

	  /* transitionStyle : "fade", */    /* [This code for animation ] */

	  navigationText:["<i class='fa fa-long-arrow-left'></i>","<i class='fa fa-long-arrow-right'></i>"],

      itemsDesktop : [1199,1],

	  itemsDesktopSmall : [980,1],

	  itemsTablet: [768,1],

	  itemsMobile : [479,1],

  });    

    equalHeight();
    $(window).load(equalHeight);
    $(window).resize(equalHeight);

    function equalHeight(){
        var windowWidth = $( window ).width();
        //console.log(windowWidth);
        if( windowWidth >= 768 ){
            var $h = 0;
            $(".lawyer-expert-section-area .single-lawyer-expert").height('auto');
            $(".lawyer-expert-section-area .single-lawyer-expert").each(function(){
                var thisHeight = $(this).outerHeight();
                if(thisHeight > $h){
                    $h = thisHeight;
                }
            });

            $(".lawyer-expert-section-area .single-lawyer-expert").height($h+'px');
        }else{
            $(".lawyer-expert-section-area .single-lawyer-expert").height('auto');
        }
    }

    /*-------------------------------------
    Page Preloader
    -------------------------------------*/
    $('#preloader').fadeOut('slow', function () {
        $(this).remove();
    });
  
  /*--------------------------
   scrollUp
  ---------------------------- */	

	$('.scrollup').on("click",function() {

	    $('html, body').animate({ scrollTop: 0 }, 'slow');

	}); 

	/*-------------------------------------
     jQuery MeanMenu activation code
     --------------------------------------*/
    $('nav#dropdown').meanmenu({
        siteLogo: "<div class='mobile-menu-nav-back'><a class='logo-mobile' href='index.html'><img src='img/logo-mobile.png' alt='logo' class='img-fluid'/></a></div>"
    });

     /*-------------------------------------
     Auto height for product listing
     -------------------------------------*/
    $(window).on('load resize', function() {

        /*--- Mobile Menu Logo --*/
        var wHeight = $(window).height(),
            mLogoH = $('a.logo-mobile').outerHeight();
        wHeight = wHeight - 50;
        $('.mean-nav > ul').css('height', wHeight + 'px');

    });




})(jQuery); 