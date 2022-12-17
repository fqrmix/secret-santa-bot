from aiogram import Router
from aiogram.types import Message, CallbackQuery
from data.users import Answers
from keyboards.pollkeyboard import get_inline_kb


router = Router()
answers = Answers()

@router.message(commands="santa")
async def message_with_text(message: Message):
    info_list = answers.get_info()
    message_text = ''
    for data in info_list:
        message_text += f"{info_list[data]['name']} - {info_list[data]['reply']}\n"
    await message.answer(message_text, reply_markup=get_inline_kb())

@router.callback_query(text="set_answer")
async def send_random_value(callback: CallbackQuery):
    answers.set_reply(str(callback.from_user.id), 'Отправил')
    info_list = answers.get_info()
    message_text = ''
    reply_count = 0
    for data in info_list:
        message_text += f"{info_list[data]['name']} - {info_list[data]['reply']}\n"
        if info_list[data]['reply'] == 'Отправил':
            reply_count += 1
    if reply_count == 6:
        await callback.message.answer('Похоже, что все отправили свои пожелания! Пора запускать шарманку.')
    else:
        await callback.message.answer(message_text, reply_markup=get_inline_kb())
