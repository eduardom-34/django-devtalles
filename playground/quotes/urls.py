from django.urls import path
from . import views

urlpatterns = [
    path("<int:day>", views.days_week_with_number), #quotes/friday
    path("<str:day>", views.days_week, name="day-quote") #quotes/friday
]