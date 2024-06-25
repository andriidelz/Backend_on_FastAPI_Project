from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine  # type: ignore
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column  # type: ignore

engine = create_async_engine(
    "sqlite+aiosqlite:///task.db"
)
new_session = async_sessionmaker(  # type: ignore
    engine, expire_on_commit=False)  # type: ignore


class Model(DeclarativeBase):
    pass


class TaskOrm(Model):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]


# class TaskOrm()


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
