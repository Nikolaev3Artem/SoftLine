from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Request
from .forms import RequestForm, ConsForm
from telethon.sync import TelegramClient
import asyncio
from telethon import types
from django.core.mail import send_mail
from SoftLine.settings import DEFAULT_FROM_EMAIL

api_id = 24481658
api_hash = 'd5a648db67ecc0034337f1c3d5e3bba2'



def send_message_to_request(request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        time = request.cleaned_data['time']
    except KeyError:
        time = None
    try:
        course = request.cleaned_data['course']
    except KeyError:
        course = None
    try:
        comment = request.cleaned_data['comment']
    except KeyError:
        comment = None
    with  TelegramClient('anon', api_id, api_hash, loop=loop) as client:
        client.loop.run_until_complete(client.send_message(types.PeerChannel(-1001894057703),
                                                            f"Ім'я: {request.cleaned_data['first_name']}\n"
                                                            f"Прізвище: {request.cleaned_data['last_name']}\n" 
                                                            f"Телефон: {request.cleaned_data['phone']}\n"
                                                            f"E-mail: {request.cleaned_data['email']}\n"
                                                            f"Час: {time}\n"
                                                            f"Курс: {course}\n"
                                                            f"Комментарий: {comment}\n"))
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
                #send_mail(f'SoftLine покупка курса', 'Hi', DEFAULT_FROM_EMAIL, form.cleaned_data['email'])
                import threading
                t = threading.Thread(target=send_message_to_request, args=(form,), kwargs={})
                t.setDaemon(True)
                t.start()
        if "cons_submit" in request.POST:
            form = ConsForm(request.POST)
            if form.is_valid():
                form.save()    
                #send_mail(f'SoftLine консультация', 'Hi', DEFAULT_FROM_EMAIL, [form.cleaned_data['email']])
                import threading
                t = threading.Thread(target=send_message_to_request, args=(form,), kwargs={})
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