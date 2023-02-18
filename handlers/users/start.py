import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot
from aiogram.dispatcher import FSMContext

@dp.message_handler(CommandStart(),state="*")
async def bot_start(message: types.Message,state: FSMContext):
    await state.finish()
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        await message.answer(f"Assalaomu aleykum {name}\n\nBu bot sizga videolarni topish va almashishda yordam beradi. U avtomatik ravishda ishlaydi, uni hech qanday joyga qo'shish shart emas. Shunchaki istalgan chatingizni oching va xabarlar maydoniga @ytsearchbit_bot biror narsa yozing. Keyin yuborish uchun natijani bosing\n\nMasalan, bu yerda <b>@ytsearchbit_bot happy dog</b> ​​so‘zini yozib ko‘ring",parse_mode='HTML')
        # Adminga xabar beramiz
        count = db.count_users()[0]
        if message.from_user.username is not None: 
            msg = f"Bazaga yangi user qo'shildi\n🙎🏻‍♂️ Name: <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n🆔 ID si: <code>{message.from_user.id}</code>\n✉️ Username: @{message.from_user.username}\n\nBazada {count} ta foydalanuvchi bor"
            await bot.send_message(chat_id=ADMINS[0], text=msg,parse_mode='HTML')
        else:
            msg = f"Bazaga yangi user qo'shildi\n🙎🏻‍♂️ Name: <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n🆔 ID si: <code>{message.from_user.id}</code>\n\nBazada {count} ta foydalanuvchi bor."
            await bot.send_message(chat_id=ADMINS[0], text=msg,parse_mode='HTML')

    except sqlite3.IntegrityError as err:
        if message.from_user.username is not None:
            await bot.send_message(chat_id=ADMINS[0], text=f"🙎🏻‍♂️ <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> bazaga oldin qo'shilgan\n✉️ Username: @{message.from_user.username}\n🆔 ID si: <code>{message.from_user.id}</code>",parse_mode='HTML')
        else:
            await bot.send_message(chat_id=ADMINS[0], text=f"🙎🏻‍♂️ <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> bazaga oldin qo'shilgan\n🆔 ID si: <code>{message.from_user.id}</code>",parse_mode='HTML')
        await message.answer(f"Assalaomu aleykum {name}\n\nBu bot sizga videolarni topish va almashishda yordam beradi. U avtomatik ravishda ishlaydi, uni hech qanday joyga qo'shish shart emas. Shunchaki istalgan chatingizni oching va xabarlar maydoniga @ytsearchbit_bot biror narsa yozing. Keyin yuborish uchun natijani bosing\n\nMasalan, bu yerda <b>@ytsearchbit_bot happy dog</b> ​​so‘zini yozib ko‘ring",parse_mode='HTML')
