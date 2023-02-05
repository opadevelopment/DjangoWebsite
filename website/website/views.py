from django.shortcuts import render

def hello(request, name='World'):
    return render(request, 'hello.html', {'name': name})