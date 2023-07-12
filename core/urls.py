from django.urls import path, include
from core import views

urlpatterns = [
    path('index/', views.indexView, name = 'index'),
    path('publicaciones/',include('publicaciones.urls')),
    path('sobrenosotros/', views.sobrenosotrosView, name = 'sobrenosotros'),
]
