from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def echo(msg: Message):
    await msg.answer(msg.text)
