from sqlalchemy import select

from models import new_session, FileTable
from schemas import SchemaFileAdd


class FileRepository:
    @classmethod
    async def file_add(cls, file: SchemaFileAdd) -> int:
        async with new_session() as session:
            file_dict = file.model_dump()
            file = FileTable(**file_dict)
            session.add(file)

            await session.flush()
            await session.commit()
            return file.id

    @classmethod
    async def file_get(self, uuid):
        async with new_session() as session:
            query = select(FileTable).where(FileTable.uuid==uuid)
            result = await session.execute(query)
            files = result.scalars().all()
            return files
