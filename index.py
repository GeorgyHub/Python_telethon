# Подключаем библиотеку telethon
from telethon import TelegamClient

# Подставляем собственные значения из 'my.telethon.org'
api_id = 27662919
api_hash = 'f3065d29712e006e64ea1703d577f9c5'
bot_token = '27662919:f3065d29712e006e64ea1703d577f9c5'

# если нам нужен явный токен бота, 
# то нужно вручную вызвать `TelegramClient.start()`.
bot = TelegamClient('bot', api_id, api_hash).start(bot_token=bot_token)

# Тогда можем использовать экземпляр клиента как обычно.
with bot as bot_client:
    proxy = ("85312", '127.0.0.1', 4444)
    TelegamClient('bot', api_id, api_hash, proxy=proxy)