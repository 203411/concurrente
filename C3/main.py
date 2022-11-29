import pygame
from random import choice
pygame.init()
#color
BG = (201,194,190)
BLACK = (51,48,33)
WHITE = (255,255,255)
W = 1280
H = 720
fps = 16
# fps = 64
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Tower Defense")

font = pygame.font.Font("./assets/font/upheavtt.ttf",40)

clock = pygame.time.Clock()

class Troop(object):
    def __init__(self,x,y,type_troop,team):
        self.x = x
        self.y = y
        self.type = type_troop
        self.team = team
        self.ruta = './assets/sprites/'
        self.width = 64
        self.height = 64
        if self.type == "archer":
            self.hp_base = 6
            self.cost = 3
            self.damage = 4
            self.drop = 3
            self.walk_images = [
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/archer_walk1.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/archer_walk2.png'),(self.width,self.height)),
            ]
            self.attack_images = [
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/archer_attack1.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/archer_attack2.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/archer_attack3.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/archer_attack4.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/archer_attack5.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/archer_attack6.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/archer_attack7.png'),(self.width,self.height)),
            ]
            self.death_images = [
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/archer_death1.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/archer_death2.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/archer_death3.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/archer_death4.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/archer_death5.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/archer_death6.png'),(self.width,self.height))
            ]
        if self.type == "knight":
            self.hp_base = 9
            self.cost = 4
            self.damage = 3
            self.drop = 4
            self.walk_images = [
                pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/knight_walk1.png'),(self.width,self.height)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/knight_walk2.png'),(self.width,self.height)),True,False),
            ]
            self.attack_images = [
                pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/knight_attack1.png'),(self.width,self.height)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/knight_attack2.png'),(self.width,self.height)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/knight_attack3.png'),(self.width,self.height)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/knight_attack4.png'),(self.width,self.height)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/knight_attack5.png'),(self.width,self.height)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/knight_attack6.png'),(self.width,self.height)),True,False),
            ]
            self.death_images = [
                pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/knight_death1.png'),(self.width,self.height)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/knight_death2.png'),(self.width,self.height)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/knight_death3.png'),(self.width,self.height)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/knight_death4.png'),(self.width,self.height)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/knight_death5.png'),(self.width,self.height)),True,False),
            ]
        if self.type == "lancer":
            self.hp_base = 15
            self.cost = 5
            self.damage = 3
            self.drop = 8
            self.walk_images = [
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/lancer_walk1.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/lancer_walk2.png'),(self.width,self.height)),
            ]
            self.attack_images = [
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/lancer_attack1.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/lancer_attack2.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/lancer_attack3.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/lancer_attack4.png'),(self.width,self.height)),
            ]
            self.death_images = [
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/lancer_death1.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/lancer_death2.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/lancer_death3.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/lancer_death4.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/lancer_death5.png'),(self.width,self.height)),
            ]
        if self.type == "dragon":
            self.width = 128
            self.height = 128
            self.hp_base = 50
            self.cost = 50
            self.damage = 12
            self.drop = 50
            self.idle_images = [
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_idle1.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_idle2.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_idle3.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_idle4.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_idle5.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_idle6.png'),(self.width,self.height)),
            ]
            self.walk_images = [
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_run1.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_run2.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_run3.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_run4.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_run5.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_run6.png'),(self.width,self.height)),
            ]
            self.attack_images = [
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_attack1.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_attack2.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_attack3.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_attack4.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_attack5.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_attack6.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_attack7.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_attack8.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_attack9.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_attack10.png'),(self.width,self.height)),
            ]
            self.death_images = [
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_death1.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_death2.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_death3.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_death4.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_death5.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_death6.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_death7.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_death8.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_death9.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_death10.png'),(self.width,self.height)),
                pygame.transform.scale(pygame.image.load(self.ruta+self.type+'/'+self.team+'/dragon_death11.png'),(self.width,self.height)),
            ]
        self.speed = 4
        self.index = 0
        self.image = self.walk_images[self.index]
        self.hp = self.hp_base
        self.damage_taken = 0
        self.hitbox = (self.x+12,self.y+30,32,34)
    
    def draw(self):
        if self.team == "red":
            #visualizar barra de vida
            if self.type == "dragon":
                pygame.draw.rect(screen,BLACK,(self.x+37,self.y+10,60,10)) #Barra de vida, vacía
                pygame.draw.rect(screen,WHITE,(self.x+38,self.y+11,int((self.hp * 58)/self.hp_base),8)) #Barra de vida, salud
                #visualizar hitbox
                self.hitbox = (self.x,self.y+30,120,70)
                pygame.draw.rect(screen,(255,0,0), self.hitbox,2)
            else:
                pygame.draw.rect(screen,BLACK,(self.x+4,self.y+10,48,10)) #Barra de vida, vacía
                pygame.draw.rect(screen,WHITE,(self.x+5,self.y+11,int((self.hp * 46)/self.hp_base),8)) #Barra de vida, salud
                #visualizar la hitbox
                self.hitbox = (self.x,self.y+30,58,34)
                pygame.draw.rect(screen,(255,0,0), self.hitbox,2)
        else:
            #visualizar barra de vida
            if self.type == "dragon":
                pygame.draw.rect(screen,BLACK,(self.x+35,self.y+10,60,10)) #Barra de vida, vacía
                pygame.draw.rect(screen,WHITE,(self.x+36,self.y+11,int((self.hp * 58)/self.hp_base),8)) #Barra de vida, salud
                #visualizar hitbox
                self.hitbox = (self.x+6,self.y+30,120,70)
                pygame.draw.rect(screen,(0,255,0), self.hitbox,2)
            else:
                pygame.draw.rect(screen,BLACK,(self.x+15,self.y+10,48,10)) #Barra de vida, vacía
                pygame.draw.rect(screen,WHITE,(self.x+16,self.y+11,int((self.hp * 46)/self.hp_base),8)) #Barra de vida, salud
                #visualizar hitbox
                self.hitbox = (self.x+6,self.y+30,58,34)
                pygame.draw.rect(screen,(0,255,0), self.hitbox,2)
        screen.blit(pygame.transform.flip(self.image,self.team == "blue",False),(self.x,self.y))

    def move(self):
        if self.team == "red":
            self.x -= self.speed
        else:
            self.x += self.speed

    def anim(self,images):
        self.index += 1
        if self.index > len(images)-1:
            self.index = 0

        self.image = images[self.index]
    
    def colision(self,any_object):
        #Lados de la hitbox de nuestro objeto
        r1_down = self.hitbox[1] + self.hitbox[3]
        r1_up = self.hitbox[1]
        r1_left = self.hitbox[0]
        r1_right = self.hitbox[0] + self.hitbox[2]
        #Lados de la hitbox de con quien chocó nuestro objeto
        r2_down = any_object.hitbox[1] + any_object.hitbox[3]
        r2_up = any_object.hitbox[1]
        r2_left = any_object.hitbox[0]
        r2_right = any_object.hitbox[0] + any_object.hitbox[2]

        return r1_right > r2_left and r1_left < r2_right and r1_up < r2_down and r1_down > r2_up
    
    def attack(self):
        self.hp -= self.damage_taken

red_team = []
blue_team = []

class Player():
    def __init__(self,auto,team,monedas):
        self.automatico = auto
        self.color = team
        self.monedas = monedas
        self.castle_hp = 50
        if self.color == "red":
            self.controles = [pygame.K_u, pygame.K_i, pygame.K_o, pygame.K_p]
        else:
            self.controles = [pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r]

    def summon_troop(self, key):
        types_troops = ["archer","knight","lancer","dragon"]
        troop = ""
        pos_x = 32
        pos_y = 354
        if self.automatico:
            key = choice(self.controles)
            if self.monedas >= 50 and choice([True,False]):
                key = self.controles[3] #escoger dragon
            else:
                key = choice(self.controles[0:4]) #escoge cualquiera menos dragon
        for t in types_troops:
            if key == self.controles[types_troops.index(t)]:
                if self.color == "red":
                    pos_x = 1149
                if types_troops[types_troops.index(t)] == "dragon":
                    pos_y = 320 
                troop = Troop(pos_x,pos_y,types_troops[types_troops.index(t)],self.color)
                if self.monedas - troop.cost >= 0:
                    self.monedas -= troop.cost
                    if self.color == "red":
                        if len(red_team) < 9:
                            red_team.append(troop)
                        elif len(blue_team) < 9:
                            blue_team.append(troop)

def calc_damage(any_red, any_blue): 
    #jerarquia de daño
    types = ["archer","lancer","knight","archer"] # archer -> lancer -> knight -> archer
    damage = (any_blue.damage,any_red.damage)
    print(any_blue.type,any_blue.team,"-",any_red.type,any_red.team)
    if any_red.type != "dragon" and any_blue.type != "dragon" :
        if types.index(any_red.type)+1 == types.index(any_blue.type):
            damage = (any_blue.damage,any_red.damage * 2) #si red counter blue, entonces red.damage*2
        elif types.index(any_blue.type)+1 == types.index(any_red.type):
            damage = (any_blue.damage * 2 ,any_red.damage) #si blue counter red, entonces blue.damage*2
    return damage

def show_stats_player():
    monedas_red = str(player.monedas) + " coins"
    monedas_blue = str(player2.monedas) + " coins"

    hp_castle_red = str(player.castle_hp) + " hp"
    hp_castle_blue = str(player2.castle_hp) + " hp"

    txt_monedas_r = font.render(monedas_red,False,BLACK)
    txt_monedas_b = font.render(monedas_blue,False,BLACK)

    txt_hp_castle_r = font.render(hp_castle_red,False,BLACK)
    txt_hp_castle_b = font.render(hp_castle_blue,False,BLACK)

    screen.blit(txt_monedas_r,(980,10))
    screen.blit(txt_monedas_b,(270,10))

    screen.blit(txt_hp_castle_r,(980,50))
    screen.blit(txt_hp_castle_b,(270,50))

def reload_screen():
    screen.fill(BG)
    
    for rt in red_team:
        rt.draw()
        rt.move()
        if len(red_team)>1 and red_team.index(rt)+1 < len(red_team):
            if rt.colision(red_team[red_team.index(rt)+1]):
                red_team[red_team.index(rt)+1].speed = 0
            else:
                red_team[red_team.index(rt)+1].speed = 4

    for bt in blue_team:
        bt.draw()
        bt.move()
        if len(blue_team)>1 and blue_team.index(bt)+1 < len(blue_team):
            if bt.colision(blue_team[blue_team.index(bt)+1]):
                blue_team[blue_team.index(bt)+1].speed = 0
            else:
                blue_team[blue_team.index(bt)+1].speed = 4

    show_stats_player()

    pygame.draw.rect(screen,(255,0,0),(270,0,1,720)) #inicio de zona de juego
    pygame.draw.rect(screen,(255,0,0),(1030,0,1,720)) #limite de zona de juego
    # pygame.draw.rect(screen,(0,0,255),(640,0,1,720)) #medio de zona de juego
    pygame.display.update()

run = True
intervalo = 1000
intervalo2 = 1000
intervalo3 = 1000
player = Player(False, "red",25)
player2 = Player(True, "blue",25)
while run:
    # if player.castle_hp <= 0 or player2.castle_hp <= 0:
    # Pausar el juego y mostrar pantalla de game over
    for evento in pygame.event.get():
        # evento de boton de cierre de ventana
        if evento.type == pygame.QUIT:
            run = False
        #evento de tecla para invocar una tropa
        if player.automatico == False and evento.type == pygame.KEYDOWN and pygame.time.get_ticks()/intervalo >= 1:
            key = evento.key
            player.summon_troop(key)
            intervalo += 1000

        if player2.automatico == False and evento.type == pygame.KEYDOWN and pygame.time.get_ticks()/intervalo2 >= 1:
            key = evento.key
            player2.summon_troop(key)
            intervalo2 += 1000
            
    #modo automatico que genera una tropa enemiga cada cierto tiempo
    if player.automatico and pygame.time.get_ticks()/intervalo >= 1:
        if len(red_team) < 2 or (len(blue_team) >= len(red_team) and len(red_team) < 6):
            player.summon_troop("")
        intervalo += 1000
    if player2.automatico and pygame.time.get_ticks()/intervalo2 >= 1:
        if len(blue_team) < 2 or (len(red_team) >= len(blue_team) and len(blue_team) < 6):
            player2.summon_troop("")
        intervalo2 += 1000
    

    if len(blue_team) > 0:
        if blue_team[0].type == "dragon" and blue_team[0].x < 1030-124:
            blue_team[0].speed = 4
        else:
            if blue_team[0].type != "dragon" and blue_team[0].x < 1030-62:
                blue_team[0].speed = 4
            else:
                blue_team[0].speed = 0
                blue_team[0].drop = 0
                blue_team[0].hp = 0
                player.castle_hp -= blue_team[0].hp_base
    
    if len(red_team) > 0:
        if red_team[0].x > 269:
            red_team[0].speed = 4
        else:
            red_team[0].speed = 0
            red_team[0].drop = 0
            red_team[0].hp = 0
            player2.castle_hp -= red_team[0].hp_base

    if len(blue_team) > 0 and len(red_team) > 0:
        damage = calc_damage(red_team[0],blue_team[0])
        if blue_team[0].colision(red_team[0]) and red_team[0].colision(blue_team[0]):
            blue_team[0].damage_taken = damage[1] #daño que hace red
            red_team[0].damage_taken = damage[0] #daño que hace blue
            blue_team[0].speed = 0
            red_team[0].speed = 0
            if pygame.time.get_ticks()/intervalo3 >= 1:
                blue_team[0].attack()
                red_team[0].attack()
                intervalo3 += 1000
        if blue_team[0].hp <= 0:
            player.monedas += blue_team[0].drop
            blue_team.remove(blue_team[0])
        if red_team[0].hp <= 0:
            player2.monedas += red_team[0].drop
            red_team.remove(red_team[0])

    reload_screen()
    clock.tick(fps)
pygame.quit()