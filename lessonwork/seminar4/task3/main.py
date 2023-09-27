# Задание 3
#
# - Написать программу, которая считывает список из 10 URL-адресов и одновременно загружает данные с каждого адреса
# - После загрузки данных нужно записать их в отдельные файлы
# - Используйте асинхронный подход


import time
import asyncio
import aiohttp

urls = [
    'https://www.notion.so/4-L-9aae4144cf6840ff9e8cb88238c13346',
    'https://zubtex.ru/books/',
    'https://amdm.ru/akkordi/zhshch/166908/7000000000/',
    'https://amdm.ru/akkordi/valentin_strykalo/100201/deshevie_drami/'
]


async def download(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = 'thread_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(text)
            print(f'{url} скачан за {time.time() - start_time:.2f} секунд')


async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()

if __name__ == '__main__':
    asyncio.run(main())
