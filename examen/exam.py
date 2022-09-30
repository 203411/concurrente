import threading
import time

chopsticks = [threading.Lock(),threading.Lock(),threading.Lock(),threading.Lock(),threading.Lock(),threading.Lock(),threading.Lock(),threading.Lock()]

mutex = threading.Lock()

def use_chopsticks(id):
    left = chopsticks[id]
    right = chopsticks[(id+1)%8] 
    if right.acquire(blocking=False):
        return True
    else: 
        if left.acquire(blocking=False):
            left.release()
            return False

def leave_chopsticks(id):
    left = chopsticks[id]
    right = chopsticks[(id+1)%8]
    
    if left.locked():
        left.release()
    else:
        if right.locked():
            right.release()
        
def critical(id):
    marker = False
    while marker == False:
        eating = use_chopsticks(id)
        if eating:
            print(f"Person {id+1} is eating")
            print(f"Person {id+1} is using the chopsticks {id+1} and {(((id+1)%8)+1)}")
            time.sleep(5)
            leave_chopsticks(id)
            print(f"Person {id+1} finished eating")
            marker=True
    

class Person(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        mutex.acquire(blocking = True, timeout = 50)
        critical(self.id)
        mutex.release()

if __name__ == '__main__':
    threads = [Person(0), Person(1), Person(2), Person(3), Person(4), Person(5), Person(6), Person(7)]
    for t in threads:
        t.start()