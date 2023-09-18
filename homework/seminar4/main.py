import asyncio
import multiprocessing
import threading
from pathlib import Path
import requests
import time
import argparse
import re

data_images = []

with open('./img/url_list.txt', 'r', encoding='utf-8') as images:
    for image in images.readlines():
        data_images.append(image.strip())

image_path = Path('./img')


def download_image(url):
    start_time = time.time()
    response = requests.get(url, stream=True)
    filename = url
    pattern = r'[^a-zA-Z0-9_]'
    filename = re.sub(pattern, '', str(filename))
    with open(f'img/{filename}.jpg', 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print(f'Файл {filename} загружен за {time.time() - start_time:.2f} секунд')


async def download_image_async(url):
    start_time = time.time()
    response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url, {'stream': True})
    filename = url
    pattern = r'[^a-zA-Z0-9_]'
    filename = re.sub(pattern, '', str(filename))
    with open(f'img/{filename}.jpg', 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print(f'Файл {filename} загружен за {time.time() - start_time:.2f} секунд')


def download_images_threading(urls):
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_image, args=[url])
        thread.start()
        threads.append(thread)
        for thread in threads:
            thread.join()
    print(f'\n### Загрузка завершена за {time.time() - start_time:.2f} секунд ###\n')


def download_images_processing(urls):
    start_time = time.time()
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=download_image, args=[url])
        process.start()
        processes.append(process)
        for process in processes:
            process.join()
    print(f'\n### Загрузка завершена за {time.time() - start_time:.2f} секунд ###\n')


async def download_images_asyncio(urls):
    start_time = time.time()
    tasks = []
    for url in urls:
        task = asyncio.create_task(download_image_async(url))
        tasks.append(task)
    await asyncio.gather(*tasks)
    print(f'\n### Загрузка завершена за {time.time() - start_time:.2f} секунд ###\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Парсим картинки по URL')
    parser.add_argument('--urls', nargs='+', default=data_images, help='Список URL для загрузки')
    args = parser.parse_args()

    urls = args.urls

    print('\n### МНОГОПОТОЧНАЯ ЗАГРУЗКА ИЗОБРАЖЕНИЙ ###\n')
    download_images_threading(urls)

    print('\n### МНОГОПРОЦЕССОРНАЯ ЗАГРУЗКА ИЗОБРАЖЕНИЙ ###\n')
    download_images_processing(urls)

    print('\n### АСИНХРОННАЯ ЗАГРУЗКА ИЗОБРАЖЕНИЙ ###\n')
    asyncio.run(download_images_asyncio(urls))
