from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Request
from .forms import RequestForm
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
                                                            f"Курс: {request.course}\n"
                                                            f"Комментарий: {request.comment}\n"))
    print('message sent')

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
            last_request = Request.objects.all().last()
            import threading
            t = threading.Thread(target=send_message_to_request, args=(last_request,), kwargs={})
            t.setDaemon(True)
            t.start()

    context = {"form": form,
               "course_left_top": course_left_top,
               "course_left_bottom": course_left_bottom,
               "course_right_top": course_right_top,
               "course_right_bottom": course_right_bottom,}
    return render(request, 'main/index.html', context=context)


def about(request):
    return render(request, 'main/about.html')