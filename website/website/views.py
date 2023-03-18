from django.shortcuts import render,redirect
from websiteController .forms import Palautelomake
from django.http  import HttpResponseRedirect




def hello(request, name='World'):
    return render(request, 'hello.html', {'name': name})

def testi(request):
    return render(request,'testi.html')

def opiskelija(request):
    return render(request, 'opiskelija.html')

def muutto(request):
    return render(request,'muutto.html')

def tyoasia(request):
    return render(request, 'tyoasia.html')

def talous(request):
    return render(request, 'talous.html')

def success(request):
    return render(request,'success.html')

def palautelomake(request):
    if request.method == "POST":
        form = Palautelomake(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')

    else:
        form = Palautelomake()
    return render(request, 'palaute.html', {'form': form})
