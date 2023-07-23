import CookieController from "./CookieManager.js";

export default class ChangeThemeClass
{
    constructor(class_name, expire)
    {
        this.class_name = class_name;
        this.expire = expire;
    }

    
    run_changeTheme()
    {

        let Theme_Cookie_Control = new CookieController(this.class_name);
		
		$("#switch").on('click', function () {
			
			if($("#card-index-page1").hasClass("None"))
			{
				$("#card-index-page1").removeClass("None");
				$("#card-index-page2").removeClass("None");
				$("#card-index-page3").removeClass("None");
			}
			

			if ($("body").hasClass("dark")) 
			{
				$("body").removeClass("dark");
				
				if($("#card-index-page1").hasClass("dark"))
				{
					///Add light theme to the cards
					$("#card-index-page1").removeClass("dark");
					$("#card-index-page2").removeClass("dark");
					$("#card-index-page3").removeClass("dark");
				}
				
                $("#switch").removeClass("switched");

				var ok = Theme_Cookie_Control.getCookie();
				if(ok)
				{
					Theme_Cookie_Control.eraseCookie();
				}

				Theme_Cookie_Control.setCookie("light", this.expire);
			}

			else {
				$("body").addClass("dark");

				if(!$("#card-index-page1").hasClass("dark"))
				{
					///Remove light theme from the cards	
					$("#card-index-page1").addClass("dark");
					$("#card-index-page2").addClass("dark");
					$("#card-index-page3").addClass("dark");
				}
				
                $("#switch").addClass("switched");
				
				var ok = Theme_Cookie_Control.getCookie();
				if(ok)
				{
					Theme_Cookie_Control.eraseCookie();
				}

				Theme_Cookie_Control.setCookie("dark", this.expire);
			}
		});  
    }
}