import asyncio, random
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import pyjokes

import app.keyborads as kb
from app.configs import bot
from joker import pack1



router = Router()

#Преветствие при вызове команды /start⬇️
@router.message(CommandStart())
async def cmd_start(message: Message):
  await message.answer('Привет!👋\nЯ бот который генерирует идиотские шутки 😶')
  await message.answer('Чтобы сгенерировать анекдот нажмите на команду /joke или отправте её')
  await message.answer('Буду благодарен если поддержите меня любой суммой)))')


# Отправка анекдота при вызове команды /joke⬇️
@router.message(Command('joke'))
async def get_joke(message: Message):
  await message.answer('Генерируется анекдот♻️')
  await asyncio.sleep(0.5)
  async def  generate_joke():  
    choice = random.choice(pack1) #⬅️Выбирается шутка из списка
    await message.reply(f'{choice}', reply_markup=kb.next) #Отправляется рандомная шутка
  async def checking(): #⬅️Функция для предотвращение ошибки StopIteration
    try:
      await generate_joke() #⬅️Вызыввется функция generate_joke если все ОК
    except StopIteration:
      return checking() #⬅️Если ошибка StopIteration эта функция завново вызыввется пока ошибка StopIteration непройдет
  await checking() 
  await bot.delete_message(chat_id= message.chat.id, message_id= message.message_id + 1) #⬅️Удаляем сообщение: 'Генерируется анекдот♻️'

#Отправка анекдота при колбэке 'next_joke'⬇️
@router.callback_query(F.data == 'next joke')
async def next_joke(callback: CallbackQuery):
  await callback.answer('Ещё один анекдот', show_alert=False)
  async def  generate_callback():
    choice = random.choice(pack1) #⬅️Выбираем шутку из списка
    await callback.message.answer(f'{choice}', reply_markup=kb.next)
  await callback.message.answer('Генерируется анекдот♻️')
  await asyncio.sleep(0.5)
  async def send_generate_callback(): #⬅️Функция для предотвращение ошибки StopIteration
    try:
      await generate_callback() #⬅️Вызыввется функция generate_callback если все ОК
    except StopIteration:
      return send_generate_callback() #⬅️Если ошибка StopIteration эта функция завново вызыввется пока ошибка StopIteration непройдет
  await send_generate_callback()
  await bot.delete_message(chat_id= callback.message.chat.id, message_id= callback.message.message_id + 1) #⬅️Удаляем сообщение: 'Генерируется анекдот♻️'

