from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import Hipo, PersonForm
from .models import Person
import math


def hipo(request):
    form = Hipo(request.GET)
    if form.is_valid():
        cat1 = form.cleaned_data.get('cathetus1')
        cat2 = form.cleaned_data.get('cathetus2')
        hipotenuza = (cat1**2) + (cat2**2)
        if hipotenuza:
            return render(request, 'triangle.html', {"form": form, "summary": round(math.sqrt(hipotenuza), 2)})
    return render(request, 'triangle.html', {"form": form})


def create_person(request):

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            return render(request, 'person.html', {"form": form, "first_name": first_name})
    else:
        form = PersonForm()
    return render(request, 'person.html', {"form": form})


def update_person(request, pk):
    obj = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            return render(request, 'final_page.html', {"form": form, "first_name": first_name})
    else:
        form = PersonForm(instance=obj)
    return render(request, "update_person.html", {'form': form, "obj": obj})