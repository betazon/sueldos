from django.shortcuts import render
from .models import *

# Create your views here.
def liquidaciones_list(request):

    liquidacion=Liquidacion.objects.all()
    values={
       'liquidacion':liquidacion,
    }
    return render(request, 'liquidaciones_list.html', values)