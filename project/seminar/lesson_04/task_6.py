# Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# Используйте асинхронность.

import os
import asyncio
import aiofiles
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


async def get_words_count(filename: str):
    file_path = os.path.join(BASE_DIR, filename)
    
    async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
        words = 0
        
        for line in await f.readlines():
            words += len(line.strip().split())
        
        print(f'File: {filename}, words: {words}')


async def main():
    tasks = []
    
    for el in os.listdir(BASE_DIR):
        if os.path.isfile(os.path.join(BASE_DIR, el)):
            task = asyncio.ensure_future(get_words_count(el))
            tasks.append(task)
    
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    # loop = asyncio.new_event_loop()
    # loop.run_until_complete(main())
    asyncio.run(main())
