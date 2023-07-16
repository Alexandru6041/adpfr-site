/* Please ❤ this if you like it! */


import CookieController from "../utils/CookieManager.js";

const cookie_expire = 2913342; ///days
const cookie_changeTheme_name = "theme";

(function($) 
	{ "use strict";

		
		$(function() 
		{
			var header = $(".start-style");
			
			$(window).scroll(function() 
			{    
				var scroll = $(window).scrollTop();
			
				if (scroll >= 10) 
				{
					header.removeClass('start-style').addClass("scroll-on");
				} 
				
				else 
				{
					header.removeClass("scroll-on").addClass('start-style');
				}
			});
		});		
		
		//Animation
		
		$(document).ready(function() 
		{
			$('body.hero-anime').removeClass('hero-anime');
		});

		//Menu On Hover
			
		$('body').on('mouseenter mouseleave','.nav-item',function(e)
		{
			var display_width = $(window).width();	

			if (display_width > 750) 
				{
					var _d=$(e.target).closest('.nav-item');_d.addClass('show');
					setTimeout(function(){_d[_d.is(':hover') ? 'addClass' : 'removeClass']('show');}, 1);
				}
		});	
		
		//Switch light/dark

		let Theme_Cookie_Control = new CookieController(cookie_changeTheme_name);
		console.log(Theme_Cookie_Control)
		
		$("#switch").on('click', function () {
			

			if ($("body").hasClass("dark")) 
			{
				$("body").removeClass("dark");
				$("#switch").removeClass("switched");
				var ok = Theme_Cookie_Control.getCookie();
				if(ok)
				{
					Theme_Cookie_Control.eraseCookie();
				}

				Theme_Cookie_Control.setCookie("light", cookie_expire);
			}

			else {
				$("body").addClass("dark");
				$("#switch").addClass("switched");
				var ok = Theme_Cookie_Control.getCookie();
				if(ok)
				{
					Theme_Cookie_Control.eraseCookie();
				}

				Theme_Cookie_Control.setCookie("dark", cookie_expire)
			}
		});  
	
  })(jQuery);