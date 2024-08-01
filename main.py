import asyncio
from aiogram import Dispatcher


from app.configs import bot
from app.handlears import router
from app.payment import router1

async def main():
  dp = Dispatcher()
  dp.include_router(router)
  dp.include_router(router1)
  await dp.start_polling(bot)



if __name__ == '__main__':
  try:
    print('Бот запущен!')
    asyncio.run(main())
  except KeyboardInterrupt:
    print('Бот выключен!')
