from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import  InlineKeyboardBuilder

from app.database.requests import get_students, get_subjects

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Что я умею?')],
                                     [KeyboardButton(text='Студенты')]],
                           resize_keyboard=True, input_field_placeholder='Выберите пункт ниже')

async def back():
    back_kb = InlineKeyboardBuilder()
    back_kb.add(InlineKeyboardButton(text='К выбору предмета:', callback_data="back_to_subject"))

async def students():
    students_kb = InlineKeyboardBuilder()
    students = await get_students()
    for student in students:
        students_kb.add(InlineKeyboardButton(text=student.name, callback_data=f'student_{student.id}'))
    return students_kb.adjust(2).as_markup()

async def subjects(student_id):
    subjects_kb = InlineKeyboardBuilder()
    subjects = await get_subjects(student_id)
    for subject in subjects:
        subjects_kb.add(InlineKeyboardButton(text=subject.name, callback_data=f'subject_{subject.id}'))
    return subjects_kb.adjust(2).as_markup()

