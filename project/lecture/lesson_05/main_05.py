import logging
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработал PUT запрос для item id = {item_id}.')
    return {"item_id": item_id, "item": item}


"""
🔥 Внимание! Код выше не будет работать, так как мы не определили объект
Item. Речь о модуле pydantic позволяющем создать класс Item будет позже
в рамках курса.
"""