import os
from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import dotenv

dotenv.load_dotenv()
# engine = create_async_engine('sqlite+aiosqlite:///messages.db')
print(os.getenv('POSTGRES_HOST'))
engine = create_async_engine(
        f"postgresql+asyncpg://{os.getenv('POSTGRES_LOGIN')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:5432/{os.getenv('POSTGRES_NAME')}"
    )


new_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Model(DeclarativeBase):
    pass

class FileTable(Model):
    __tablename__ = 'files'

    id: Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str]
    extension: Mapped[str]
    uuid: Mapped[str] = mapped_column(unique=True)
    size: Mapped[int]


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)