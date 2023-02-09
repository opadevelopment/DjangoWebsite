from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('hello/<str:name>/', views.hello, name='hello'),
    path('testi_sivu/', views.testi_sivu, name='testi_sivu')
]