from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("commands"))
async def commands_handl(msg: Message):
    await msg.answer(
        (
            "Вот что я умею:\n"
            "/commands - посмотреть список команд\n"
            "/reg - пройти небольшую регистрацию\n"
        )
    )
