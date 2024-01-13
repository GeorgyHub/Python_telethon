# Подключаем библиотеку telethon
from telethon import TelegamClient

# Подставляем собственные значения из 'my.telethon.org'
api_id = 27662919
api_hash = 'f3065d29712e006e64ea1703d577f9c5'

#
with TelegamClient('test', api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))