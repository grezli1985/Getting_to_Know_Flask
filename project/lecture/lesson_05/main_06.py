import logging
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f'Отработал DELETE запрос для item id = {item_id}.')
    return {"item_id": item_id}

"""
🔥 Важно! Зачастую операция удаления не удаляет данные из базы данных, а
изменяет специально созданное поле is_deleted на значение Истина. Таким
образов вы сможете восстановить ранее удалённные данные
пользователя, если он передумает спустя время.
"""