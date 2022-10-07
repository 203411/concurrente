import time
import queue
import random
import threading

PRODUCERS = 5
CONSUMERS = 10

# Creación de la cola
queue = queue.Queue(maxsize=10)
condition = threading.Condition()

class Producer(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
    def run(self):
        while True:
            if condition.acquire():
                if queue.full():
                    condition.wait()
                else:
                    item = random.randint(0, 100)
                    queue.put(item)
                    print(f"Producer {self.id} produced {item}")
                    condition.notify()
                    condition.release()
                    time.sleep(3)

class Consumer(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
    def run(self):
        while True:
            if condition.acquire():
                if queue.empty():
                    condition.wait()
                else:
                    item = queue.get()
                    print(f"Consumer {self.id} consumed {item}")
                    condition.notify()
                    condition.release()
                    time.sleep(3)

if __name__ == '__main__':
    producers = []
    custormers = []
    for i in range(PRODUCERS):
        producers.append(Producer(i))
    for i in range(CONSUMERS):
        custormers.append(Consumer(i))
    
    for p in producers:
        p.start()
    for c in custormers:
        c.start()