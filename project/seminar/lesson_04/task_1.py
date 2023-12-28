# Написать программу, которая считывает список из 10 URLадресов и одновременно
# загружает данные с каждого адреса.
# После загрузки данных нужно записать их в отдельные
# файлы.
# Используйте потоки.

import os
import threading
from pathlib import Path
import requests
import time


BASE_DIR = Path(__file__).resolve().parent
saves_dir = os.path.join(BASE_DIR, 'saves')

if not os.path.exists(saves_dir):
    os.mkdir(saves_dir)

urls = [
    'https://ya.ru',
    'https://github.com/DispenserBro',
    'https://google.com',
    'https://gb.ru',
    'https://mail.ru',
    'https://www.python.org/',
    'https://habr.com/ru/all/',
    'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0',
    'https://news.vtomske.ru/',
    'https://www.1tv.ru/',
]


def download_content(url: str):
    response = requests.get(url)
    filename = (
        url.replace('https://', '').replace('.', '_').replace('/', '-')
        + '.html'
    )
    with open(os.path.join(saves_dir, filename), 'w', encoding='utf-8') as f:
        f.write(response.text)


threads: list[threading.Thread] = []


start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download_content, args=[url])
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

print(f'Completed download in {time.time()- start_time} seconds.')
