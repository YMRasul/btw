import logging

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
#from aiogram.utils import executor

from aiogram.utils.executor import start_webhook


API_TOKEN = '5240442552:AAGQtUhRoxZAiKBSvHgg1nNdr1U43Vp8LkQ'

# webhook settings
WEBHOOK_HOST = '185.217.131.87'
WEBHOOK_PATH = 'root/btw/to/5240442552:AAGQtUhRoxZAiKBSvHgg1nNdr1U43Vp8LkQ'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = '120.0.0.1'  #'localhost'  # or ip
WEBAPP_PORT = 3001

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format=u'%(levelname)-8s [%(asctime)s] %(message)s'
)
'''
logging.basicConfig(
    level=logging.INFO,filename='oylikbot.log',
    format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
)
'''

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler()
async def echo(message: types.Message):
    # Regular request
    await bot.send_message(message.chat.id, message.text)
    # or reply INTO webhook
    return SendMessage(message.chat.id, message.text)


async def on_startup(dp):
    logger.info(">>>>>>> Start Bot oylik")
    logger.info(">>>>>>> Connecting dbase_sqlite.db")
    logger.info('>>>>>>> Bot oylik in online')
    await bot.set_webhook(WEBHOOK_URL)
    # insert code here to run it after start


async def on_shutdown(dp):
    logging.warning('Shutting down..')

    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    #await bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning('Bye!')

'''
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)

'''
if __name__ == '__main__':
    print(WEBHOOK_PATH)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )