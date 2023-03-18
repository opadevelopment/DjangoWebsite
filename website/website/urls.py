from django.urls import path
from .import views
from django.contrib import admin
from django.conf import settings
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello, name='hello'),
    path('hello/<str:name>/', views.hello, name='hello'),
    path('testi/', views.testi, name='testi'),
    path('opiskelija/',views.opiskelija, name='opiskelija'),
    path('muutto/',views.muutto, name='muutto'),
    path('tyoasia/',views.tyoasia, name='tyoasia'),
    path('talous/',views.talous, name='talous'),
    path('palaute/', views.palautelomake, name='palaute'),
    path('success/',views.success, name='success'),


]