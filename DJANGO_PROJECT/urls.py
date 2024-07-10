from django.urls import path
from . import views

app_name = "hello"
urlpatterns = [
    path("", views.index, name="index"),
    path("count", views.count, name="count"),
    path("greet", views.greet, name="greet"),
    path("colors", views.colors, name="colors"),
    path("select", views.select, name="select"),
    path("tasks", views.tasks, name="tasks"),
    path("currency", views.currency, name="currency"),
    
    
    
    
    
    # path("<str:name>", views.greet, name="greet"),
]