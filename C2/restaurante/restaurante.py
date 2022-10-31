import threading
import time
import random

CAPACIDAD = 100
MESEROS = round(CAPACIDAD * 0.1)
COCINEROS = round(CAPACIDAD * 0.1)
RESERVACION_MAX = round(CAPACIDAD * 0.2)

mutex = threading.Lock()
comensal = threading.Condition(mutex)

restaurant = []
cola_espera = []
ordenes = []
comidas = []
'''
RECEPCIÓN
- Los comensales llegan de forma individual o en grupo
- La recepción solo puede atender de forma individual o en grupo

RESERVACIONES
- Se pueden hacer reservaciones de manera aleatoria para un máximo del 20% de la capacidad
- Los hilos con reservación pasan a este proceso, se bloquean, tras cierto tiempo se desbloquean y llegan al restaurante
- Cuando un hilo trate de hacer una reservación y no haya espacio se va a la cola del restaurante

COMENSAL
- Llama a un mesero una vez entra al restaurante
- Cambia la orden a EN PROCESO
- Tardan un tiempo específico comiendo y al terminar se retiran y despiertan a los comensales en espera

MESERO
- Solo puede atender a un comensal simultaneamente
- Genera una ORDEN que tiene 2 estados
    EN PROCESO: el comensal bloquea al mesero y el mesero añade la orden a un buffer de ordenes infinito
    LISTO: el cocinero desbloquea al mesero y añade a un buffer de comidas
- Si no hay comensales todos los meseros descansan

COCINERO
- Esta en reposo si no hay ordenes en el buffer
- Cocina, cambia la orden a LISTO y añade al buffer de comidas
'''
class Comensales(threading.Thread):
    reservacion = []
    conta = 0
    def __init__(self, reserva):
        super(Comensales, self).__init__()
        self.id = Comensales.conta
        Comensales.conta += 1
        self.reserva = reserva
        Comensales.reservacion.append(threading.Lock())

    def ordenar(self):
        Comensales.reservacion[self.id].acquire()
        print(f'Comensal {self.id} is {Comensales.reservacion[self.id].locked()}')
        Comensales.reservacion[self.id].release()
        print(f'Comensal {self.id} is {Comensales.reservacion[self.id].locked()}')
        #Cuando ordena al mesero, este puede atender a un solo comensal

    def comer(self):
        pass
        #tiempo de espera en lo que come y al final sale de la cola
    
    def reservar(self):
        Comensales.reservacion[self.id].acquire()
        print(f'Comensal {self.id} is {Comensales.reservacion[self.id].locked()}')
        time.sleep(random.random())
        self.ordenar()
        #se bloquean x tiempo y despues se desbloquean 
    
    def run(self):
        if self.reserva == 0:
            self.ordenar()
        else:
            self.reservar()
        #acciones a realizar al ejecutar .start

class Mesero(threading.Thread):
    
    def atender(self):
        pass
    def generar_orden(self):
        pass
    def descansar(self):
        pass
    def run(self):
        pass

class Cocineros(threading.Thread):
    def cocinar(self):
        pass
    def descansar(self):
        pass
    def run(self):
        pass
    
def main():
    while True:
        en_espera = 0
        if len(restaurant) < CAPACIDAD:
            reserva = random.randint(0,1) #0 - sin reservacion, 1 - con reservacion
            cantidad = random.randint(1,RESERVACION_MAX)
            aux = len(restaurant)+cantidad
            if aux > CAPACIDAD:
                comensales = CAPACIDAD - len(restaurant)
                en_espera = cantidad-comensales
            else:
                comensales = cantidad
            for _ in range(comensales):
                restaurant.append(Comensales(reserva))
            if en_espera > 0:
                for _ in range(en_espera):
                    cola_espera.append(Comensales(reserva))
            # print(f"Cantidad: {cantidad}\tRestaurant: {len(restaurant)}\tCola de espera: {len(cola_espera)}", end="\r")
            time.sleep(0.5)
        # if len(restaurant) == CAPACIDAD:
        #     for c in restaurant:
        #         c.start()

if __name__ == '__main__':
    main()
