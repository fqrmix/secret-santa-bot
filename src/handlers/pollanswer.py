from aiogram import Router
from aiogram.types import Message, CallbackQuery
from data.users import Answers
from keyboards.pollkeyboard import get_inline_kb


router = Router()
answers = Answers()

@router.message(commands="santa")
async def message_with_text(message: Message):
    if answers.all_replied():
        await message.answer('🎁 Похоже, что все отправили свои пожелания! Пора запускать шарманку.')
    else:
        info_list = answers.get_info()
        message_text = ''
        for data in info_list:
            message_text += f"{info_list[data]['reply']} - *{info_list[data]['name']}*\n"
        await message.answer(
            message_text, 
            reply_markup=get_inline_kb(), 
            parse_mode='markdown'
        )

@router.callback_query(text="set_answer")
async def send_random_value(callback: CallbackQuery):
    if answers.get_reply(str(callback.from_user.id)) == '🎁 Отправил':
        await callback.answer(
            text="Ты уже отправил пожелания!",
            show_alert=True
        )
    else:
        answers.set_reply(str(callback.from_user.id), '🎁 Отправил')
        info_list = answers.get_info()
        message_text = f"🎁 {info_list[str(callback.from_user.id)]['name']} отправил пожелания!\n\n"
        for data in info_list:
            message_text += f"{info_list[data]['reply']} - *{info_list[data]['name']}*\n"
        await callback.answer(
            text="Ты успешно отправил пожелания!",
            show_alert=True
        )
        if answers.all_replied():
            await callback.message.answer('🎁 Похоже, что все отправили свои пожелания! Пора запускать шарманку.')
        else:
            await callback.message.answer(
                message_text, 
                reply_markup=get_inline_kb(), 
                parse_mode='markdown'
            )
