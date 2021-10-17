import random
import time
import string
from threading import Thread, Semaphore


BUFFER_SIZE = random.randint(5, 10)

buffer = [None] * BUFFER_SIZE


def produce():
    item = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    print(f"Produced: {item}")
    return item


def consume(item):
    print(buffer)
    print(f"Consumed: {item}")


def producent():
    while True:
        time.sleep(random.randint(0, 4))


def consumer():
    while True:
        time.sleep(random.randint(0, 4))

    

producent_thread = Thread(target=producent)
consumer_thread = Thread(target=consumer)

producent_thread.start()
consumer_thread.start()

producent_thread.join()
consumer_thread.join()