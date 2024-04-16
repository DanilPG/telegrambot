from app.database.models import async_session
from app.database.models import Student, Subject
from sqlalchemy import select


async def get_students():
    async with async_session() as session:
        result = await session.scalars(select(Student))
        return result


async def get_subjects(student_id):
    async with async_session() as session:
        result = await session.scalars(select(Subject).where(Subject.student_id == student_id))
        return result

async def get_subject(subject_id) -> Subject:
    async with async_session() as session:
        result = await session.scalar(select(Subject).where(Subject.id == subject_id))
        return result