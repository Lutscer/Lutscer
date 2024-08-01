from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

catolog = ReplyKeyboardMarkup(keyboard=[
  [KeyboardButton(text='Сгенерировать анекдот')],
 [KeyboardButton(text='Поддержать')]])
   
next = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Сгенерировать ещё один анекдот', callback_data='next joke')],
  [InlineKeyboardButton(text='Поддержать', callback_data='next_payment')]])