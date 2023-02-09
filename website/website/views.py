from django.shortcuts import render
from django.http  import HttpResponse

def hello(request, name='World'):
    return render(request, 'hello.html', {'name': name})

def testi_sivu(request):
    return render(request,'testi_sivu.html')