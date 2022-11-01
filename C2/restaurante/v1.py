""" 
INTEGRANTES:
    Marisol Solís López - 203411
    Enrique Verdi Cruz - 203433
    Gabriel Ramón Cupil - 203424
"""
#NOTA de preferencia ejecutarlo en el prompt para visualizar los colores correctamente
import threading, time, queue, math
from random import choice, randint
from termcolor import colored

CAPACIDAD = 5
COMENSALES = 10
MESEROS = math.ceil(CAPACIDAD * 0.1) if CAPACIDAD <= 5 else round(CAPACIDAD * 0.1) #Esto es para que la cantidad de meseros siempre sea almenos 1
COCINEROS = MESEROS #Hay 10% de la capacidad y 10% de la capacidad, por lo tanto hay igual cantidad de cocineros que de meseros
RESERVACION_MAX = round(CAPACIDAD * 0.2)

class Monitor(object):
    def __init__(self,espacio):
        #capacidad del restaurante
        self.espacio = espacio 
        self.mutex = threading.Lock()
        self.recepcion = threading.Condition()
        self.clientes = threading.Condition()
        self.mesero = threading.Condition()
        self.cocinero = threading.Condition()
        self.reservaciones = queue.Queue(RESERVACION_MAX)
        self.num_clientes = queue.Queue(self.espacio)
        self.ordenes = queue.Queue()
        self.ordenes_plato = queue.Queue()
        self.comida = queue.Queue()

    def reservar(self,comensal):
        self.recepcion.acquire()
        if self.reservaciones.full():
            self.recepcion.wait()
        else:
            print(colored(f"Comensal {comensal.id} hizo una reservación",color="white",on_color="on_yellow"))
            self.reservaciones.put(comensal)
            time.sleep(1)
        self.mutex.acquire()
        self.entrar(comensal)
        self.reservaciones.get()
        self.recepcion.notify()
        self.recepcion.release()

    def encolar(self,comensal):
        self.recepcion.acquire()
        print(colored(f"Comensal {comensal.id} se formó en la cola","white","on_blue"))
        time.sleep(1)
        self.mutex.acquire()
        self.entrar(comensal)
        self.recepcion.notify()
        self.recepcion.release()

    def entrar(self,comensal):
        self.clientes.acquire()
        if self.num_clientes.full():
            print(colored(f"Comensal {comensal.id} esperando a que haya lugar","red"))
            self.clientes.wait()
        else:
            print(colored(f"Comensal {comensal.id} entra al restaurante","cyan"))
            self.num_clientes.put(comensal)
            print(colored(f"Comensal {comensal.id} se prepara para ordenar","cyan"))
            self.mesero.acquire()
            self.mesero.notify()
            self.mesero.release()
            self.mutex.release()
            self.clientes.release()
    
    def comer(self):
        if not self.comida.empty():
            comensal = self.comida.get()
            comensal_id = list(comensal.keys())[0]
            comensal_plato = list(comensal.values())[0]
            print(colored(f"Comensal {comensal_id} está comiendo {comensal_plato}","white","on_green"))
            time.sleep(randint(1,5))
            print(f"Comensal {comensal_id} terminó de comer")
            print(colored(f"Comensal {comensal_id} ha salido",attrs=["underline"]))

    def crear_orden(self, mesero):
        while True:
            self.mesero.acquire()
            if self.num_clientes.empty():
                self.mesero.wait()
                print(colored(f"Mesero {mesero} esta descansando","white","on_red"))
            else:
                comensal = self.num_clientes.get()
                if comensal.orden == False:
                    plato = Orden()
                    print(colored(f"Mesero {mesero} tomo la orden del cliente {comensal.id} que comerá {plato.food}","yellow"))
                    time.sleep(1)
                    self.ordenes.put({comensal.id : plato.food})
                    self.cocinero.acquire()
                    self.cocinero.notify()
                    self.cocinero.release()
                    comensal.orden = True
                    self.mesero.release()
                else:
                    self.mesero.release()

    def cocinar(self,id):
        while True:
            self.cocinero.acquire()
            if self.ordenes.empty():
                self.cocinero.wait()
                print(colored(f"Cocinero {id} esta descansando","white","on_magenta"))
            else:
                comensal = self.ordenes.get()
                comensal_id = list(comensal.keys())[0]
                comensal_plato = list(comensal.values())[0]
                print(colored(f"Cocinero {id} está cocinando la orden del comensal {comensal_id}: {comensal_plato}",attrs=["bold"]))
                time.sleep(1)
                self.comida.put(comensal)
                self.cocinero.release()
class Orden():
    foods = ["spaguetti","lasagna","quesadilla","hamburguesa","huevos al gusto","tacos"]
    def __init__(self): 
        self.food = choice(self.foods)

class Comensal(threading.Thread):
    def __init__(self,id,monitor):
        threading.Thread.__init__(self)
        self.id = id
        self.orden = False
        self.restaurant = monitor
    def run(self):
        reserva = randint(0,1)
        if reserva == 1: 
            self.restaurant.reservar(self) 
        if reserva == 0:
            self.restaurant.encolar(self)
        self.restaurant.comer()

class Mesero(threading.Thread):
    def __init__(self,id,monitor):
        threading.Thread.__init__(self)
        self.id = id
        self.restaurant = monitor

    def run(self):
        self.restaurant.crear_orden(self.id)

class Cocinero(threading.Thread):
    def __init__(self,id,monitor):
        threading.Thread.__init__(self)
        self.id = id
        self.restaurant = monitor
    
    def run(self):
        self.restaurant.cocinar(self.id)

def main():
    restaurant = Monitor(CAPACIDAD)
    comensales = []
    meseros = []
    cocineros = []

    for x in range(COMENSALES):
        comensales.append(Comensal(x+1,restaurant))
    for comensal in comensales:
        comensal.start()

    for x in range(MESEROS):
        meseros.append(Mesero(x+1,restaurant))
    for mesero in meseros:
        mesero.start()

    for x in range(COCINEROS):
        cocineros.append(Cocinero(x+1,restaurant))
    for cocinero in cocineros:
        cocinero.start()

if __name__ == "__main__":
    main()