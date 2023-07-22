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
			

			if ($("body").hasClass("dark") && !$("#card-index-page1").hasClass("light")) 
			{
				$("body").removeClass("dark");

                ///Add light theme to the cards
				$("#card-index-page1").addClass("light");
				$("#card-index-page2").addClass("light");
				$("#card-index-page3").addClass("light");
				
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

				///Remove light theme from the cards
                $("#card-index-page1").removeClass("light");
				$("#card-index-page2").removeClass("light");
				$("#card-index-page3").removeClass("light");
				
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