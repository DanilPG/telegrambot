from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import CallbackQuery


import app.keyboards as kb
from app.database.requests import get_subject

router = Router()

@router.message(CommandStart()) #Приветсвие, ответ на /start
async def handle_start(message: types.Message):
    await message.answer(text=f"Привет, {message.from_user.full_name}", reply_markup=kb.main)
    await message.answer(text=f"Чтобы узнать свою успеваемость, нажми на кнопку <b>студенты</b>.", reply_markup=kb.main)

@router.message(Command("help")) #Ответ на help
async def hanle_hepl(message: types.message):
    await message.answer(text="Привет, я студенческий бот. С помощью меня ты можешь узнать свою успеваемость.\n")

@router.message(F.text == 'Что я умею?')
async def fun1(message: types.message):
    await message.answer(text="Дорогой студент, с помощью меня ты можешь узнать свою успеваемость и баллы по выбранным предметам. Для этого выбери свою группу.")

@router.message(F.text == 'Студенты')
async def student(message: types.message):
    await message.answer(text="Выберите студента из списка.", reply_markup=await kb.students())


@router.callback_query(F.data.startswith('student_'))
async def student_selected(callback: CallbackQuery):
    student_id = callback.data.split('_')[1]
    await callback.message.answer(f'Вы выбрали студента {student_id}.\n\n')
    await callback.message.answer(f'<b>Выберите предмет:</b>', reply_markup=await kb.subjects(student_id))
    await callback.answer('')


@router.callback_query(F.data.startswith('subject_'))
async def subject_selected(callback: CallbackQuery):
    subject_id = callback.data.split('_')[1]
    subject = await get_subject(subject_id=subject_id)

    if subject.point < 20:
        message = 'Пора потрудиться!'
    else:
        message = 'Ты молодец!'
    # Отправляем информацию о предмете
    await callback.message.answer(
        f'Предмет: <b>{subject.name} 📚</b>\n\nБалл: <b>{subject.point} 💯- {message}</b>\n\nПосещаемость: <b>{subject.attendance}% 🔥</b>')
    await callback.answer('')

@router.callback_query(F.data.startswith('back_to_subject'))
async def back_to_subject(callback: CallbackQuery):
    student_id = callback.message.text.split()[2]  # Получение student_id из текста сообщения через разделение текста
    await callback.message.answer('<b>Выберите предмет:</b>', reply_markup=await kb.subjects(student_id))
    await callback.answer('')








