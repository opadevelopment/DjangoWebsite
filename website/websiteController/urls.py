from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('hello/', views.hello, name='hello'),
    
]