# Задание 2
#
# - Написать программу, которая считывает список из 10 URL-адресов и одновременно загружает данные с каждого адреса
# - После загрузки данных нужно записать их в отдельные файлы
# - Используйте процессы


import time
import requests
from multiprocessing import Process

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


processes = []
start_time = time.time()

if __name__=='__main__':
    for url in urls:
        process = Process(target=download, args=[url])
        processes.append(process)
        process.start()

    
