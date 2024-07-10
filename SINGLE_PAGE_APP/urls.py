from django.urls import path
from . import views

app_name = "singlepageapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("sections/<int:num>", views.section, name="section"),
    path("scroll", views.scroll, name="scroll"),
    
]