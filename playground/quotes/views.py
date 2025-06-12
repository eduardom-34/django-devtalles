from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
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
    return HttpResponse(f"{day}")


def days_week(request, day):
    
    try:
        quote_text = days_of_week[day]
        return HttpResponse(quote_text)
    except:
        return HttpResponseNotFound("Este dia no existe")
        
    
        