from django.shortcuts import render
from .models import Qrcode


# Create your views here.
def index(request):
    qrr = Qrcode.objects.all().order_by('-id')
    context = {
        'qrr': qrr,
    }
    return render(request, 'index.html', context)
