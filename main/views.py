from django.shortcuts import render

#Third-Party libraries

# Create your views here.

Theme_CookieName = "theme"

def index(request):
    Theme_CookieValue = request.COOKIES.get(Theme_CookieName)
    
    context = {Theme_CookieName : Theme_CookieValue}        
    
    return render(request, "ro/index.html", context)

#LEGAL

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


#ABOUT US
def cine_suntem(request):
    Theme_CookieValue = request.COOKIES.get(Theme_CookieName)
    
    context = {Theme_CookieName : Theme_CookieValue}
    
    return render(request, "ro/AboutUs/cine-suntem.html", context)

def ce_facem(request):
    Theme_CookieValue = request.COOKIES.get(Theme_CookieName)
    
    context = {Theme_CookieName : Theme_CookieValue}
    
    return render(request, "ro/AboutUs/ce-facem.html", context)

def comisii(request):
    Theme_CookieValue = request.COOKIES.get(Theme_CookieName)
    
    context = {Theme_CookieName : Theme_CookieValue}
    
    return render(request, "ro/AboutUs/comisii.html", context)

def contact(request):
    Theme_CookieValue = request.COOKIES.get(Theme_CookieName)
    
    context = {Theme_CookieName : Theme_CookieValue}
    
    return render(request, "ro/AboutUs/contact.html", context)

def management(request):
    Theme_CookieValue = request.COOKIES.get(Theme_CookieName)
    
    context = {Theme_CookieName : Theme_CookieValue}
    
    return render(request, "ro/AboutUs/management-si-structura.html", context)

def membri(request):
    Theme_CookieValue = request.COOKIES.get(Theme_CookieName)
    
    context = {Theme_CookieName : Theme_CookieValue}
    
    return render(request, "ro/AboutUs/membri.html", context)

def statut(request):
    Theme_CookieValue = request.COOKIES.get(Theme_CookieName)
    
    context = {Theme_CookieName : Theme_CookieValue}
        
    return render(request, "ro/AboutUs/Statutul-ADPFR.html", context)

