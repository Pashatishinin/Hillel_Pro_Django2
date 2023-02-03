from django.shortcuts import render, redirect, reverse
from .forms import Hipo
import math


def hipo(request):
    form = Hipo(request.GET)
    if request.method == 'GET':
        if form.is_valid():
            cat1 = form.cleaned_data.get('cathetus1')
            cat2 = form.cleaned_data.get('cathetus2')
            hipotenuza = (cat1**2) + (cat2**2)
            if hipotenuza:
                return render(request, 'triangle.html', {"form": form, "summary": round(math.sqrt(hipotenuza), 2)})
    return render(request, 'triangle.html', {"form": form})
