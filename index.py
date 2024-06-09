# Подключаем библиотеку telethon
from telethon.sync import TelegramClient, events

# Подставляем собственные значения из 'my.telethon.org'
api_id = 27662919
api_hash = 'f3065d29712e006e64ea1703d577f9c5'
api_token = '7268393537:AAE4CvloPV1JqEbW0q6y1n4RHYNfc0rmoZg'

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=api_token)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hello')

def main():
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()