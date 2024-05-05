from django.urls import path
from . import views

#URLCONFIG
urlpatterns = [
    path(route='hola/', view= views.hola_mundo)
]