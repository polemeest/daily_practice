import threading
import urllib.request
import time

start = time.time()

urls = [
    'https://www.yandex.ru', 'https://www.google.com',
    'https://habrahabr.ru', 'https://www.python.org',
    'https://isocpp.org',
]


def read_url(url):
    with urllib.request.urlopen(url) as u:
        return u.read()


threads = []
for url in urls:
    threads.append(threading.Thread(target=read_url, args=[url]))

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()






print(time.time() - start)
