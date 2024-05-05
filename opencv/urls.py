from django.urls import path
from . import views

#URLCONFIG
urlpatterns = [
    path(route='test/', view= views.main_page)
]