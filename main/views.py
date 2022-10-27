from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Request
from .forms import RequestForm, ConsForm
from telethon.sync import TelegramClient
import asyncio
from telethon import types

api_id = 24481658
api_hash = 'd5a648db67ecc0034337f1c3d5e3bba2'



def send_message_to_request(request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with  TelegramClient('anon', api_id, api_hash, loop=loop) as client:
        client.loop.run_until_complete(client.send_message(types.PeerChannel(-1001894057703),
                                                            f"Ім'я: {request.first_name}\n"
                                                            f"Прізвище: {request.last_name}\n" 
                                                            f"Телефон: {request.phone}\n"
                                                            f"E-mail: {request.email}\n"
                                                            f"Час: {request.time}\n"
                                                            f"Курс: {request.course}\n"
                                                            f"Комментарий: {request.comment}\n"))
    return

def index(request):
    try:
        course_left_top = Course.objects.get(id=1)
    except Course.DoesNotExist:
        course_left_top = None
    try:
        course_right_top = Course.objects.get(id=2)
    except Course.DoesNotExist:
        course_right_top = None
    try:
        course_left_bottom = Course.objects.get(id=3)
    except Course.DoesNotExist:
        course_left_bottom = None
    try:        
        course_right_bottom = Course.objects.get(id=4)
    except Course.DoesNotExist:
        course_right_bottom = None
    request_form = RequestForm()
    cons_form = ConsForm()
    if request.method == 'POST':
        if "request_submit" in request.POST:
            form = RequestForm(request.POST)
            if form.is_valid():
                form.save()    
                last_request = Request.objects.all().last()
                import threading
                t = threading.Thread(target=send_message_to_request, args=(last_request,), kwargs={})
                t.setDaemon(True)
                t.start()
        if "cons_submit" in request.POST:
            form = ConsForm(request.POST)
            if form.is_valid():
                form.save()    
                last_request = Request.objects.all().last()
                import threading
                t = threading.Thread(target=send_message_to_request, args=(last_request,), kwargs={})
                t.setDaemon(True)
                t.start()

    context = {"request_form": request_form,
               "cons_form": cons_form,
               "course_left_top": course_left_top,
               "course_left_bottom": course_left_bottom,
               "course_right_top": course_right_top,
               "course_right_bottom": course_right_bottom,}
    return render(request, 'main/index.html', context=context)


def about(request):
    return render(request, 'main/about.html')

def error(request):
    return render(request,'main/error.html')