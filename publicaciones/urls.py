from django.urls import path
from publicaciones import views

urlpatterns = [
    path('publicaciones/', views.publicacionesView, name = 'publicaciones'),
   
]