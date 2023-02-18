from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.dispatcher import FSMContext
from loader import dp


@dp.message_handler(CommandHelp(),state="*")
async def bot_help(message: types.Message,state: FSMContext):
        await state.finish()
        text = ("Shunchaki istalgan chatingizni oching va xabarlar maydoniga @ytsearchbit_bot biror narsa yozing. Keyin yuborish uchun natijani bosing")
        await message.answer_photo(photo="https://ibb.co/MS14NfM",caption=text)
