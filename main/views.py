from django.shortcuts import render
from django.http import HttpResponse
#from .send_message import send_message

from .models import Course, Request
from .forms import RequestForm

def index(request):
    course_left_top = Course.objects.all().first()
    course_left_bottom = Course.objects.all().last()
    course_right_top = Course.objects.all().last()
    course_right_bottom = Course.objects.all().first()
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            #send_message()
            

    context = {"form": form,
               "course_left_top": course_left_top,
               "course_left_bottom": course_left_bottom,
               "course_right_top": course_right_top,
               "course_right_bottom": course_right_bottom,}
    return render(request, 'main/index.html', context=context)


def about(request):
    return render(request, 'main/about.html')