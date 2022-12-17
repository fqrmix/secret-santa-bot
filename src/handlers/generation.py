from aiogram import Router
from aiogram.types import Message
import random


router = Router()

@router.message(commands="random")
async def generate_message(message: Message):
    folder = random.randrange(1,4)
    file = random.randrange(1,10)
    with open(f'src/handlers/anectode/{folder}/{file}.txt', 'r') as f:
        text = f.read()
    await message.answer(text)
