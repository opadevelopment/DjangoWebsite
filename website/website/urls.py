from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello, name='hello'),
    path('hello/<str:name>/', views.hello, name='hello'),
    path('testi_sivu/', views.testi_sivu, name='testi_sivu'),
    path('opiskelija_sivu/',views.opiskelija_sivu, name='opiskelija_sivu'),
    path('muutto_sivu/',views.muutto_sivu, name='muutto_sivu'),
    path('tyoasia_sivu/',views.tyoasia_sivu, name='tyoasia_sivu'),
    path('talous_sivu/',views.talous_sivu, name='talous_sivu'),
    path('yhteydenotto_sivu/', views.yhteydenotto_sivu, name='yhteydenotto_sivu'),


]