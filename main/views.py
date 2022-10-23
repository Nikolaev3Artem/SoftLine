from django.shortcuts import render
from django.http import HttpResponse

from .forms import RequestForm

def index(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'main/index.html', {"form": form})


def about(request):
    return render(request, 'main/about.html')