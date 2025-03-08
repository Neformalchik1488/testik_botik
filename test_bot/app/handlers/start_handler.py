from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_cmd(msg: Message):
    await msg.answer(
        (
            "Привет!\n"
            "Вот что я умею:\n"
            "/commands - посмотреть список команд\n"
            "/reg - пройти небольшую регистрацию\n"
        )
    )
