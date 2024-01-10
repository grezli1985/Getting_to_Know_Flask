import logging
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item


"""
🔥 Внимание! Код выше не будет работать, так как мы не определили объект
Item. Речь о модуле pydantic позволяющем создать класс Item будет позже
в рамках курса.
"""