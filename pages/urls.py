from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/calculate" ,views.calculate_api , name = "calculate"),
]
