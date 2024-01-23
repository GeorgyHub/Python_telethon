# Подключаем библиотеку telethon
from telethon import TelegramClient, events, sync

# Подставляем собственные значения из 'my.telethon.org'
api_id = 27662919
api_hash = 'f3065d29712e006e64ea1703d577f9c5'
#api_token = '27662919:f3065d29712e006e64ea1703d577f9c5'

client = TelegramClient('bot', api_id, api_hash)

async def main():
    me = await client.get_me()

    print(me.stringify())

    username = me.username
    print(username)
    print(me.phone)

    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

client.start()