from django.shortcuts import render

#Third-Party libraries

# Create your views here.

def index(request):
    Theme_CookieName = "theme"
    Theme_CookieValue = request.COOKIES.get(Theme_CookieName)
    
    context = {Theme_CookieName : Theme_CookieValue}        
    
    return render(request, "ro/index.html", context)