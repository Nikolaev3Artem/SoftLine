from telethon import TelegramClient
from .models import Request
import asyncio

api_id = 24481658
api_hash = 'd5a648db67ecc0034337f1c3d5e3bba2'
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

client = TelegramClient('anon', api_id, api_hash, loop=loop)

async def send_message():
    request = Request.objects.all().last()
    await client.send_message(request.phone, 'Hello')
    print('message sended')
    
# def send_message():
#     with client:
#         client.loop.run_until_complete(get_message())