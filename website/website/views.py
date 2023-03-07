from django.shortcuts import render
from django.http  import HttpResponseRedirect
from websiteController .forms import PalauteLomake


def hello(request, name='World'):
    return render(request, 'hello.html', {'name': name})

def testi_sivu(request):
    return render(request,'testi_sivu.html')

def opiskelija_sivu(request):
    return render(request, 'opiskelija_sivu.html')

def muutto_sivu(request):
    return render(request,'muutto_sivu.html')

def tyoasia_sivu(request):
    return render(request, 'tyoasia_sivu.html')

def talous_sivu(request):
    return render(request, 'talous_sivu.html')

def yhteydenotto_sivu(request):
    return render(request, 'yhteydenotto_sivu.html')

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
    return render(request, 'yhteydenotto_sivu.html', {'form':form, 'submitted':submitted})