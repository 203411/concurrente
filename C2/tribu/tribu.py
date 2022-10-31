import random
import threading
import queue

MISIONEROS = random.randint(1, 100)
olla = queue.Queue(maxsize=MISIONEROS)

mutex = threading.Lock()

class Canibal(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
    def run(self):
        while True:
            if mutex.acquire():
                if olla.empty():
                    print(f"Canibal {self.id} is waiting for food")
                    mutex.release()
                else:
                    item = olla.get()
                    print(f"Canibal {self.id} ate {item}")
                    mutex.release()
                    
class Misionero(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
    def run(self):
        while True:
            if mutex.acquire():
                if olla.full():
                    print(f"Misionero {self.id} is waiting for space")
                    mutex.release()
                else:
                    item = random.randint(0, 100)
                    olla.put(item)
                    print(f"Misionero {self.id} put {item}")
                    mutex.release()

if __name__ == '__main__':
    canibales = []
    misioneros = []z
    for i in range(MISIONEROS):
        canibales.append(Canibal(i))
    for i in range(MISIONEROS):
        misioneros.append(Misionero(i))
    
    for c in canibales:
        c.start()
    for m in misioneros:
        m.start()