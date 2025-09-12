
from django.contrib import admin
from django.urls import path
from api.views import ping
import api.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ping/', ping , name = 'ping'),
    path('api/add' , api.views.add_function , name = "add_function_name")
]
