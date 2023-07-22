from django.shortcuts import render

#Third-Party libraries

# Create your views here.

Theme_CookieName = "theme"

def index(request):
    Theme_CookieValue = request.COOKIES.get(Theme_CookieName)
    
    context = {Theme_CookieName : Theme_CookieValue}        
    
    return render(request, "ro/index.html", context)

def licenta_reproducere(request):
    Theme_CookieValue = request.COOKIES.get(Theme_CookieName)
    
    context = {Theme_CookieName : Theme_CookieValue}
    
    return render(request, "ro/Legal/licenta-reproducere.html", context)

def legislatie(request):
    Theme_CookieValue = request.COOKIES.get(Theme_CookieName)
    
    context = {Theme_CookieName : Theme_CookieValue}
    
    return render(request, "ro/Legal/legislatie.html", context)

def privacy_policy(request):
    Theme_CookieValue = request.COOKIES.get(Theme_CookieName)
    
    context = {Theme_CookieName : Theme_CookieValue}
    
    return render(request, "ro/Legal/privacy-policy.html", context)

def terms_and_conditions(request):
    Theme_CookieValue = request.COOKIES.get(Theme_CookieName)
    
    context = {Theme_CookieName : Theme_CookieValue}
    
    return render(request, "ro/Legal/terms-and-conditions.html", context)