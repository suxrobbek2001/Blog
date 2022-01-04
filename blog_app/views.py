from django.shortcuts import render,redirect

from .models import Maqola, Rasm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def maqola(request,son):
    mq = Maqola.objects.get(id=son)
    rm = Rasm.objects.filter(maqola=mq)
    return render(request, 'maqola.html', {'maqola': mq, 'rasm': rm})

def blog(request):
    maqolalar = Maqola.objects.all().order_by('-time')
    return render(request, 'blog.html', {"m": maqolalar})


