from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

days_of_week = {
    "monday": "Pienso, luego existo",
    "tuesday": "La vida es un sueño",
    "wednesday": "El conocimiento es poder",
    "thursday": "Se el cambio que quieres ver en el mundo",
    "friday": "Solo se que no se nada",
    "saturday": "Vive como si fuera el ultimo dia", 
    "sunday": "Da un poquito mas todo los dias"
    
}

def days_week_with_number(request, day):
    days = list(days_of_week.keys())
    if day > len(days):
        return HttpResponseNotFound("<h1>El dia no existe</h1>")
    redirect_day = days[day - 1]
    
    redirect_path = reverse("day-quote", args=[redirect_day])
    return HttpResponseRedirect(redirect_path)

def index(request):
    list_items = ""
    days = list(days_of_week.keys()) #[monday, tuesday, wednesday, thursday, friday, saturday, sunday]
    
    for day in days:
        day_path = reverse("day-quote", args=[day])
        list_items += f"<li><a href=\"{day_path}\">{day}</a></li>"
        
    response_html = f"<ul>{list_items}</ul>"
    
    return HttpResponse(response_html)
    

def days_week(request, day):
    
    try:
        quote_text = days_of_week[day]
        return HttpResponse(quote_text)
    except KeyError:
        return HttpResponseNotFound("Este dia no existe")
        
    
        