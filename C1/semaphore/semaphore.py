from threading import Semaphore, Thread

"""
wait(s) - decrementa el valor de s si este es mayor que cero. Si es igual a cero, el proceso se bloqueara en el semaforo hasta que otro proceso llame a signal().
signal(s) - desbloquea algun proceso bloqueado en s, y en el caso de que no haya ningun proceso bloqueado, incrementa el valor de s.

"""

semaphore = Semaphore(1)

    
def critico(id):
    global x;
    x = x + id
    print("Hilo = " + str(id) + " => " + str(x))
    x = 1

class Hilo(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id = id
    def run(self):
        semaphore.acquire()
        critico(self.id)
        semaphore.release()
        
threads_semaphores = [Hilo(1), Hilo(2), Hilo(3)]
x = 1;
for t in threads_semaphores:
    t.start()