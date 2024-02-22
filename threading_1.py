import threading
import random
import time
import sys
import os
import re

received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")


def ping(suffix) -> None:
    ip = "192.168.178." + str(suffix)
    ping_out = os.popen("ping -q -c2 " + ip, "r")  # получение вердикта
    print("... pinging ", ip)
    while True:
        line = ping_out.readline()
        if not line:
            break
        n_received = received_packages.findall(line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])

start = time.time()
threads = [threading.Thread(target=ping, args=[suffix, ]) for suffix in range(20, 30)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(time.time() - start)