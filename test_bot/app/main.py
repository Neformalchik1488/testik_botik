import asyncio
import logging
import config

from handlers import start_handler, echo_handler, registration_handler, command_handler

from aiogram import Dispatcher, Bot
from redis.asyncio import Redis
from aiogram.fsm.storage.redis import RedisStorage

from sqlalchemy.orm import Session, DeclarativeBase
from sqlalchemy import create_engine, Column, Integer, String


async def main():
    logging.basicConfig(format = "%(levelname)s [%(asctime)s] %(message)s", filename="logs.log")  
    bot = Bot(
        token=config.TOKEN,) 

    redis = Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=config.REDIS_DB)
    storage = RedisStorage(redis)

    dp = Dispatcher(storage=storage)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logging.info("start polling")

    dp.include_routers(
        start_handler.router,
        command_handler.router,
        registration_handler.router,
        echo_handler.router
    )

    engine = create_engine(
    f"postgresql+psycopg2://{config.PSQL_USER}:{config.PSQL_PASS}@{config.PSQL_HOST}:{config.PSQL_PORT}/{config.PSQL_NAME}",
    echo=True,
    #pool_size=5,
    #max_overflow=10
    )


    # class Base(DeclarativeBase): pass
    # class Person(Base):
    #     __tablename__ = "people"

    #     id = Column(Integer, primary_key=True, index=True)
    #     name = Column(String)
    #     age = Column(Integer)

    # Base.metadata.create_all(bind=engine)

    # with Session(autoflush=False, bind=engine) as db:
    #     pass
    
    await dp.start_polling(bot)
        

asyncio.run(main())

