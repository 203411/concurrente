from msilib.schema import ControlEvent
import threading
import time
from random import choice, randint

CAPACIDAD = 10
COMENSALES = 15
MESEROS = round(CAPACIDAD * 0.1)
COCINEROS = round(CAPACIDAD * 0.1)
RESERVACION_MAX = round(CAPACIDAD * 0.2)

class Monitor(object):
    def __init__(self,espacio):
        self.espacio = espacio #capacidad del restaurante
        self.mutex = threading.Lock()
        self.reservas = threading.Condition(self.mutex)
        self.clientes = threading.Condition(self.mutex)
        self.mesero = threading.Condition(self.mutex)
        self.cocinero = threading.Condition(self.mutex)
        self.reservaciones = []
        self.num_clientes = [] #numero de clientes dentro del restaurante
        self.cola_espera = [] #clientes en espera para entrar al restaurante
        self.ordenes = []
        self.comida = []
    #Recepcionista
    def puedo_reservar(self):
        with self.mutex:
            if (self.reservaciones < RESERVACION_MAX):
                return True
            else:
                return False

    def reservar(self,comensal):
        with self.mutex:
            if self.puedo_reservar():
                print(f"Cliente {comensal.id} hizo una reservación")
                self.reservaciones.append(comensal)
                time.sleep(1)
                self.entrar(comensal)
            else:
                self.encolar(comensal)

    def encolar(self,comensal):
        with self.mutex:
            self.cola_espera.append(comensal)
            self.entrar(comensal)
            if len(self.num_clientes) < self.espacio:
                print(f"Cliente {comensal.id} llega al restaurante")
                self.entrar(comensal)
            else:
                print(f"Cliente {comensal.id} se formó en la cola")
                time.sleep(3)
    #Comensal
    def entrar(self,comensal):
        self.reservas.acquire()
        if len(self.reservaciones) > 0 or len(self.cola_espera) > 0:
            self.clientes.acquire()
            print(f"Cliente {comensal.id} entra al restaurante")
            if len(self.num_clientes) < self.espacio:
                self.num_clientes.append(comensal)

                self.mesero.acquire()
                self.meseros.notify()
                self.mesero.release()
                self.clientes.release()
            self.reservas.notify()
            self.reservas.release()
        else:
            self.reservas.wait()
    
    def comer(self, comensal):
        print(f"Cliente {comensal.id} está comiendo")
        time.sleep(randint(1,5))
        print(f"Cliente {comensal.id} terminó de comer")

    def salir(self,comensal):
        with self.mutex:
            print(f"\nClientes: {len(self.num_clientes)}\n")
            self.num_clientes.pop()
            print(f"Cliente {comensal.id} ha salido")
            time.sleep(1)
            if len(self.cola_espera) > 0:
                new_comensal = self.cola_espera.pop()
                new_comensal.restaurant.entrar(new_comensal)
            self.clientes.notify()
    #Mesero
    def descansar_mesero(self):
        with self.mutex:
            if len(self.num_clientes) > 0:
                return False
            else:
                return True
    
    def crear_orden(self, mesero):
        with self.mutex:
            plato = Orden()
            print(f"Mesero {mesero} tomo la orden del nuevo cliente que comerá {plato.food}")
            time.sleep(1)
            self.ordenes.append(plato)
            self.cocineros.notify()
    #Cocinero
    def ordenes_pendientes(self):
        with self.mutex:
            if len(self.ordenes) > 0:
                return True
            else:
                return False
    def cocinar(self,id):
        with self.mutex:
            print(f"Cocinero {id} está cocinando")
            orden = self.ordenes.pop()
            time.sleep(1)
            self.comida.append(orden)
            print(f"Cocinero {id} preparó: {orden.food}")
            self.liberar_orden()
    def liberar_orden(self):
        orden = self.comida.pop()
        print(f"El mesero ha servido un platillo de {orden.food}")

class Orden(object):
    foods = ["spaguetti","lasagna","quesadilla","hamburguesa","huevos al gusto","tacos"]
    def __init__(self): 
        self.food = choice(Orden.foods)

class Comensal(threading.Thread):
    def __init__(self,id,monitor):
        threading.Thread.__init__(self)
        self.id = id
        self.restaurant = monitor
    def run(self):
        reserva = randint(0,1)
        if reserva == 1: 
            self.restaurant.reservar(self) 
        if reserva == 0:
            self.restaurant.encolar(self)
        self.restaurant.comer(self)

class Mesero(threading.Thread):
    def __init__(self,id,monitor):
        threading.Thread.__init__(self)
        self.id = id
        self.restaurant = monitor

    def run(self):
        while self.restaurant.descansar_mesero():
            print(f"Mesero {self.id} esta descansando")
        self.restaurant.crear_orden(self.id)

class Cocinero(threading.Thread):
    def __init__(self,id,monitor):
        threading.Thread.__init__(self)
        self.id = id
        self.restaurant = monitor
    
    def run(self):
        while(self.restaurant.ordenes_pendientes()):
            self.restaurant.cocinar(self.id)
        print(f"Cocinero {self.id} esta esperando nuevas ordenes")            

def main():
    threads = []
    restaurant = Monitor(CAPACIDAD)

    for x in range(COMENSALES):
        threads.append(Comensal(x+1,restaurant))

    for x in range(MESEROS):
        threads.append(Mesero(x+1,restaurant))

    for x in range(COCINEROS):
        threads.append(Cocinero(x+1,restaurant))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()