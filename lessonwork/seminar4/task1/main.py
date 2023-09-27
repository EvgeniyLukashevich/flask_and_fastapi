# Задание 1
#
# - Написать программу, которая считывает список из 10 URL-адресов
# и одновременно загружает данные с каждого адреса
# - После загрузки данных нужно записать их в отдельные файлы
# - Используйте потоки


import requests
import threading
import time

urls = [
    'https://www.notion.so/4-L-9aae4144cf6840ff9e8cb88238c13346',
    'https://zubtex.ru/books/',
    'https://amdm.ru/akkordi/zhshch/166908/7000000000/',
    'https://amdm.ru/akkordi/valentin_strykalo/100201/deshevie_drami/'
]


def download(url: str):
    response = requests.get(url)
    filename = 'thread_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(response.text)
    print(f'{url} скачан за {time.time() - start_time:.2f} секунд')


threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download, args=[url, ])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
