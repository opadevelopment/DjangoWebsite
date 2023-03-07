from django.shortcuts import render
from websiteController .forms import PalauteLomake
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

def palaute(request):
    return render(request, 'palaute.html')

def asiakaspalaute(request):
    submitted = False
    if request.method == 'POST':
        form = PalauteLomake(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/palautelomake?submitted=True')
    else:
        form = PalauteLomake
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'palaute.html', {'form':form, 'submitted':submitted})