from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('second/', views.second, name='second'),
    path('third/', views.third, name='third'),
    path('secondsecond/', views.secondsecond, name='secondsecond'),
]
