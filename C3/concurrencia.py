from threading import Thread,Lock, Condition, Semaphore 
import time
from random import choice, randint

class Monitor():
    def __init__(self):
        #variables de juego
        self.hp_player = 50
        self.hp_cpu = 50
        self.monedas_player = 0
        self.monedas_cpu = 0
        self.tropas_player = []
        self.tropas_desplegadas_player = []
        self.tropas_cpu = []
        self.tropas_desplegadas_cpu = []

    def ganar_monedas(self):
        if self.monedas_player < 50:
            if self.monedas_player+2 > 50:
                self.monedas_player += (50-self.monedas_player)
            else:
                self.monedas_player += 2

        if self.monedas_cpu < 50:
            if self.monedas_cpu+2 > 50:
                self.monedas_cpu += (50-self.monedas_cpu)
            else:
                self.monedas_cpu += 2
        time.sleep(1)

    def gastar_monedas(self,tropa,clave):
        if clave == 0 and self.monedas_cpu-tropa["cost"] >= 0:
            self.monedas_cpu -= tropa["cost"]
            if len(self.tropas_desplegadas_cpu) < 9:
                self.tropas_desplegadas_cpu.append(tropa)
            else:
                self.tropas_cpu.append(tropa)
        elif clave == 1 and self.monedas_player-tropa["cost"] >= 0:
            self.monedas_player -= tropa["cost"]
            if len(self.tropas_desplegadas_player) < 9:
                self.tropas_desplegadas_player.append(tropa)
            else:
                self.tropas_player.append(tropa)
        else:
            print("Dinero suficiente")

class Tropa():
    def asesino(self):
        return {"type":"archer","damage":4,"hp":6,"cost":3,"drop":3,"damage_tower":6}
    def guerrero(self):
        return {"type":"knight","damage":3,"hp":9,"cost":4,"drop":4,"damage_tower":9}
    def paladin(self):
        return {"type":"lancer","damage":3,"hp":12,"cost":5,"drop":8,"damage_tower":12}
    def dragon(self):
        return {"type":"dragon","damage":12,"hp":50,"cost":50,"drop":50,"damage_tower":50}
    def random_trop(self):
        tropas = [self.asesino(),self.guerrero(),self.paladin(),self.dragon()]
        tropa = choice(tropas)
        return tropa

class Game(Thread):
    def __init__(self, monitor):
        Thread.__init__(self)
        self.monitor = monitor

    def run(self):
        while self.monitor.hp_player >= 1 and self.monitor.hp_cpu >= 1:
            self.monitor.ganar_monedas()

class Player(Thread):
    def __init__(self,monitor,automatico):
        Thread.__init__(self)
        self.puntos = 0
        self.monitor = monitor
        self.automatico = automatico

    def desplegar_tropa(self,clave):
        opt = 0
        if clave == 0:
            self.monitor.gastar_monedas(Tropa().random_trop(),clave)
            time.sleep(randint(1,5))
        while (opt<1 or opt>5) and clave==1:
            opt = input("[1]Guerrero\t[2]Asesino\t[3]Paladín\t[4]Dragon\n")
            if opt != "" and opt.isdigit():
                opt = int(opt)
                if(opt == 1):
                    self.monitor.gastar_monedas(Tropa().guerrero(),clave)
                elif(opt == 2):
                    self.monitor.gastar_monedas(Tropa().asesino(),clave)
                elif(opt == 3):
                    self.monitor.gastar_monedas(Tropa().paladin(),clave)
                elif(opt == 4):
                    self.monitor.gastar_monedas(Tropa().dragon(),clave)
                else:
                    print("ignorar")
            else:
                opt = 0

    def run(self):
        self.monitor.ganar_monedas()
        if self.automatico:
            #juega la maquina
            while self.monitor.hp_cpu >= 1:
                if self.monitor.monedas_cpu >=3:
                    self.desplegar_tropa(0)
        else:
            while self.monitor.hp_player >= 1:
                if self.monitor.monedas_player >= 3:
                    self.desplegar_tropa(1)
                else:
                    print("No tienes dinero suficiente")
            print("Perdiste")

def main():
    monitor = Monitor()
    game = Game(monitor)
    player = Player(monitor,True) #false para jugadores, true para la máquina
    game.start()
    player.start()
    
if __name__ == "__main__":
    main()