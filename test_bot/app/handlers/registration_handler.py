from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()

class RegistrationStates(StatesGroup):
    name = State()
    age = State()
    gender = State()
    petrsu = State()
    curriculum = State()
    about = State()

@router.message(Command("reg"))
async def reg_handler(msg: Message, state: FSMContext):
    await msg.answer("Введи ФИО!")
    await state.set_state(RegistrationStates.name)

@router.message(RegistrationStates.name)
async def name_handler(msg: Message, state: FSMContext):
    await state.set_data({"name": msg.text})
    await msg.answer("Теперь нужно ввести свой возраст")
    await state.set_state(RegistrationStates.age)

@router.message(RegistrationStates.age)
async def age_handler(msg: Message, state: FSMContext):

    try:
        age = int(msg.text)
    except ValueError:
        await msg.answer("Неправильный формат, введи число")
        return

    await state.update_data({"age": age})
    await msg.answer("Теперь введи свой пол")
    await state.set_state(RegistrationStates.gender)

@router.message(RegistrationStates.gender)
async def gender_handler(msg: Message, state: FSMContext):
    await state.update_data({"gender": msg.text})
    await msg.answer("Из какого ты института?")
    await state.set_state(RegistrationStates.petrsu)

@router.message(RegistrationStates.petrsu)
async def gender_handler(msg: Message, state: FSMContext):
    await state.update_data({"petrsu": msg.text})
    await msg.answer("На каком ты курсе?")
    await state.set_state(RegistrationStates.curriculum)

@router.message(RegistrationStates.curriculum)
async def gender_handler(msg: Message, state: FSMContext):
    try:
        curriculum = int(msg.text)
    except ValueError:
        await msg.answer("Неправильный формат, введи число")
        return
    
    await state.update_data({"curriculum": curriculum})
    await msg.answer("Теперь немного о тебе")
    await state.set_state(RegistrationStates.about)

@router.message(RegistrationStates.about)
async def gender_handler(msg: Message, state: FSMContext):
    await state.update_data({"about": msg.text})
    data = await state.get_data()
    await msg.answer(
        (
            "Готово!\n"
            f"Тебя зовут {data['name']}\n"
            f"Твой возраст: {data['age']}\n"
            f"Твой пол: {data['gender']}\n"
            f"Твой институт: {data['petrsu']}\n"
            f"Ты на {data['curriculum']} курсе\n"
            f"Чуть-чуть о тебе: {data['about']}\n"
        )       
    )
    await state.clear()
    
