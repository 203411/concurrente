import pygame
from random import choice
from threading import Thread, Lock

pygame.init()
pygame.mixer.init()
#paleta de colores
BG = (201,194,190)
BLACK = (51,48,33)
WHITE = (255,255,255)
BLUE = (50,131,172)
RED = (172,50,50)
# variables para el juego
W = 1280
H = 720
fps = 8*4

screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Tower Defense")
ruta_fuente = "./assets/font/upheavtt.ttf"
font = pygame.font.Font(ruta_fuente,40)

clock = pygame.time.Clock()

coin = [
    pygame.transform.scale(pygame.image.load('./assets/sprites/coin/coin_1.png'),(48,48)),
    pygame.transform.scale(pygame.image.load('./assets/sprites/coin/coin_2.png'),(48,48)),
    pygame.transform.scale(pygame.image.load('./assets/sprites/coin/coin_3.png'),(48,48)),
    pygame.transform.scale(pygame.image.load('./assets/sprites/coin/coin_4.png'),(48,48))
]
index_coin = 0
guia = pygame.image.load('./assets/sprites/guia.png')

red_team = []
blue_team = []

class Game(Thread):
    def __init__(self,player1,player2):
        Thread.__init__(self)
        self.player1 = player1
        self.player2 = player2
        self.mutex = Lock()
        self.mutex.acquire()

    def give_coins(self):
        with self.mutex:
            if self.player1.monedas+2 <= 50:
                self.player1.monedas += 2 
            if self.player2.monedas+2 <= 50:
                self.player2.monedas += 2 

    def run(self):
        if player_blue.castle_hp <=0 or player_red.castle_hp <= 0:
            self.mutex.acquire()
        else:
            self.mutex.release()

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
            self.hp_base = 12
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
            self.hp_base = 30
            self.cost = 40
            self.damage = 12
            self.drop = 40
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
        self.is_attack = False
        self.is_death = False
    
    def draw(self):
        if self.team == "red":
            #visualizar barra de vida
            if self.type == "dragon":
                pygame.draw.rect(screen,BLACK,(self.x+37,self.y+10,60,10)) #Barra de vida, vacía
                pygame.draw.rect(screen,WHITE,(self.x+38,self.y+11,int((self.hp * 58)/self.hp_base),8)) #Barra de vida, salud
                #visualizar hitbox
                self.hitbox = (self.x,self.y+30,120,70)
                # pygame.draw.rect(screen,(255,0,0), self.hitbox,2)
            else:
                pygame.draw.rect(screen,BLACK,(self.x+4,self.y+10,48,10)) #Barra de vida, vacía
                pygame.draw.rect(screen,WHITE,(self.x+5,self.y+11,int((self.hp * 46)/self.hp_base),8)) #Barra de vida, salud
                #visualizar la hitbox
                self.hitbox = (self.x,self.y+30,58,34)
                # pygame.draw.rect(screen,(255,0,0), self.hitbox,2)
        else:
            #visualizar barra de vida
            if self.type == "dragon":
                pygame.draw.rect(screen,BLACK,(self.x+35,self.y+10,60,10)) #Barra de vida, vacía
                pygame.draw.rect(screen,WHITE,(self.x+36,self.y+11,int((self.hp * 58)/self.hp_base),8)) #Barra de vida, salud
                #visualizar hitbox
                self.hitbox = (self.x+6,self.y+30,120,70)
                # pygame.draw.rect(screen,(0,255,0), self.hitbox,2)
            else:
                pygame.draw.rect(screen,BLACK,(self.x+15,self.y+10,48,10)) #Barra de vida, vacía
                pygame.draw.rect(screen,WHITE,(self.x+16,self.y+11,int((self.hp * 46)/self.hp_base),8)) #Barra de vida, salud
                #visualizar hitbox
                self.hitbox = (self.x+6,self.y+30,58,34)
                # pygame.draw.rect(screen,(0,255,0), self.hitbox,2)
        screen.blit(pygame.transform.flip(self.image,self.team == "blue",False),(self.x,self.y))

    def move(self):
        self.anim(self.walk_images)
        if self.team == "red":
            self.x -= self.speed
        else:
            self.x += self.speed

    def anim(self,images):
        self.index += 1
        if self.index > len(images)-1:
            self.index = 0
        self.image = images[self.index]
        self.draw()
    
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
    
    def idle(self):
        if self.type == "dragon":
            self.anim(self.idle_images)
        else:
            self.anim(self.walk_images)
    
    def attack(self):
        self.anim(self.attack_images)
        if self.index == len(self.attack_images)-1:
            self.hp -= self.damage_taken
    
    def death(self):
        self.anim(self.death_images)
        if self.index == len(self.death_images)-1:
            return True

class Player():
    def __init__(self,auto,team,monedas, castle_hp):
        self.automatico = auto
        self.color = team
        self.monedas = monedas
        self.hp_base = castle_hp
        self.castle_hp = castle_hp
        if self.color == "red":
            self.controles = [pygame.K_u, pygame.K_i, pygame.K_o, pygame.K_p]
        else:
            self.controles = [pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r]
        self.ruta = "./assets/sprites/castle/castle_"
        self.img_castle = [
            pygame.transform.scale(pygame.image.load(self.ruta+self.color+"1.png"),(336,336)),
            pygame.transform.scale(pygame.image.load(self.ruta+self.color+"2.png"),(336,336)),
            pygame.transform.scale(pygame.image.load(self.ruta+self.color+"3.png"),(336,336)),
            pygame.transform.scale(pygame.image.load(self.ruta+self.color+"4.png"),(336,336)),
            pygame.transform.scale(pygame.image.load(self.ruta+self.color+"5.png"),(336,336)),
            pygame.transform.scale(pygame.image.load(self.ruta+self.color+"6.png"),(336,336)),
            pygame.transform.scale(pygame.image.load(self.ruta+self.color+"7.png"),(336,336)),
            pygame.transform.scale(pygame.image.load(self.ruta+self.color+"8.png"),(336,336)),
            pygame.transform.scale(pygame.image.load(self.ruta+self.color+"9.png"),(336,336)),
            pygame.transform.scale(pygame.image.load(self.ruta+self.color+"10.png"),(336,336)),
            pygame.transform.scale(pygame.image.load(self.ruta+self.color+"11.png"),(336,336)),
            pygame.transform.scale(pygame.image.load(self.ruta+self.color+"12.png"),(336,336)),
            pygame.transform.scale(pygame.image.load(self.ruta+self.color+"13.png"),(336,336))
        ]
        self.index = 0
        self.castle_img = self.img_castle[self.index]

    def anim_castle(self,pos_x,pos_y):
        self.index+=1
        if self.index == 12:
            self.index = 0
        self.castle_img = self.img_castle[self.index]
        screen.blit(self.castle_img,(pos_x,pos_y))

    def show_hp_castle(self,pos_x,pos_y,color_team):
        pygame.draw.rect(screen,BLACK,(pos_x + 95,pos_y*3,150,20))
        pygame.draw.rect(screen,color_team,(pos_x + 96,pos_y*3+1,(148*self.castle_hp)/self.hp_base,18))

    def summon_troop(self, key):
        types_troops = ["archer","knight","lancer","dragon"]
        troop = ""
        pos_x = 32
        pos_y = 354
        if self.automatico:
            key = choice(self.controles)
            if self.monedas >= 40 and choice([True,False]):
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
    # print(any_blue.type,any_blue.team,"-",any_red.type,any_red.team)
    if any_red.type != "dragon" and any_blue.type != "dragon" :
        if types.index(any_red.type)+1 == types.index(any_blue.type):
            damage = (any_blue.damage,any_red.damage * 2) #si red counter blue, entonces red.damage*2
        elif types.index(any_blue.type)+1 == types.index(any_red.type):
            damage = (any_blue.damage * 2 ,any_red.damage) #si blue counter red, entonces blue.damage*2
    return damage

def show_stats_player():

    global index_coin
    if index_coin == 3:
        index_coin = 0
    else:
        index_coin += 1

    monedas_red = str(player_red.monedas)
    monedas_blue = str(player_blue.monedas)

    txt_monedas_r = font.render(monedas_red,False,BLACK)
    txt_monedas_b = font.render(monedas_blue,False,BLACK)

    screen.blit(txt_monedas_r,(980,10))
    screen.blit(coin[index_coin],(935,6))
    screen.blit(txt_monedas_b,(270,10))
    screen.blit(coin[index_coin],(225,6))

    player_red.show_hp_castle(955,142,RED)
    player_blue.show_hp_castle(-17,142,BLUE)

def troop_controller(troops):
    for troop in troops:
        if troop.is_death:
            if troop.death():
                if troop.team == "red":
                    player_blue.monedas += troop.drop
                else:
                    player_red.monedas += troop.drop
                troops.remove(troop)
        else:
            if troop.speed != 0:
                troop.move()
            elif troop.is_attack:
                troop.attack()
            else:
                troop.idle()
            if len(troops)>1 and troops.index(troop)+1 < len(troops):
                if troop.colision(troops[troops.index(troop)+1]):
                    troops[troops.index(troop)+1].speed = 0
                else:
                    troops[troops.index(troop)+1].speed = 4

def progress_bar():
    font = pygame.font.Font(ruta_fuente,25)
    txt_progress_bar = font.render("PROGRESS BAR",False,BLACK)
    screen.blit(txt_progress_bar,(640-txt_progress_bar.get_size()[0]/2,175))
    pygame.draw.rect(screen,BLACK,(440,200,400,30))
    if len(red_team)>0:
        red_p = (((1030-red_team[0].x)*400)/780)-2
        pygame.draw.rect(screen,RED,(840-red_p,201,red_p,28))
    if len(blue_team) > 0:
        real_x = blue_team[0].x+62
        if blue_team[0].type == "dragon":
            real_x = blue_team[0].x+124
        blue_p = ((real_x-250)*400/780)-1
        pygame.draw.rect(screen,BLUE,(441,201,blue_p,28))

def reload_screen():
    screen.fill(BG)
    player_red.anim_castle(955,142)
    player_blue.anim_castle(-17,142)
    
    troop_controller(red_team)
    troop_controller(blue_team)

    show_stats_player()
    progress_bar()
    
    screen.blit(guia,(W/2-(guia.get_size()[0]/2),450))
    # pygame.draw.rect(screen,(255,0,0),(250,0,1,720)) #inicio de zona de juego
    # pygame.draw.rect(screen,(255,0,0),(1030,0,1,720)) #limite de zona de juego
    # pygame.draw.rect(screen,(0,0,255),(640,0,1,720)) #medio de zona de juego    
    pygame.display.update()

def show_main_menu():
    screen.fill(BG)
    font = pygame.font.Font(ruta_fuente,80)
    tower = font.render("TOWER",False,BLACK)
    defense = font.render("DEFENSE",False,BLACK)
    font = pygame.font.Font(ruta_fuente,30)
    press_key = font.render("Press any key to start",False,BLACK)

    screen.blit(tower,(W/2-(tower.get_size()[0]/2),80))
    screen.blit(defense,(W/2-(defense.get_size()[0]/2),160))
    screen.blit(press_key,(W/2-(press_key.get_size()[0]/2),400))
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(fps)
        for evento in pygame.event.get():
                # evento de boton de cierre de ventana
                if evento.type == pygame.QUIT:
                    pygame.quit()
                if evento.type == pygame.KEYDOWN:
                    waiting = False

run = True
game_over = True

pygame.mixer.music.load("./assets/sound/theme.mp3","mp3")
pygame.mixer.music.play(-1)

inicioJuego = 0

while run:
    if game_over:

        show_main_menu()
        pygame.mixer.music.rewind()
        game_over = False

        intervalo = 1000
        intervalo2 = 1000
        intervalo3 = 1000
        aux = 0
        alpha_value = 0
        if inicioJuego == 0:
            inicioJuego = pygame.time.get_ticks()
        red_team = []
        blue_team = []
        player_red = Player(False, "red",25, 50) #(bool automatico,str team,int monedas,int vida)
        player_blue = Player(True, "blue",25, 50)
        game = Game(player_red,player_blue)
        game.start()
        pygame.display.update()
        clock.tick(fps)
    # else:
    if player_blue.castle_hp <= 0 or player_red.castle_hp<=0:
        # Pausar el juego y mostrar pantalla de game over
        for evento in pygame.event.get():
            # evento de boton de cierre de ventana
            if evento.type == pygame.QUIT:
                run = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                inicioJuego=0
                game_over = True
        txt_game_over = font.render("GAME OVER",False,WHITE)
        txt_winner = font.render(player_blue.color+" Team WON", False, BLUE)
        replay_txt = font.render("Press Space to replay...",False,WHITE)
        bg_game_over = pygame.Surface((W,H))
        if player_red.castle_hp > 0:
            txt_winner = font.render(player_red.color+" Team WON", False, RED)
        if alpha_value <= 255:
            bg_game_over.fill(BLACK)
            bg_game_over.set_alpha(alpha_value)
            screen.blit(bg_game_over,(0,0))
            alpha_value += 5
            if alpha_value > 50:
                screen.blit(txt_game_over,(W/2-(txt_game_over.get_size()[0]/2),H/2-(txt_game_over.get_size()[1])))
                screen.blit(txt_winner,(W/2-(txt_winner.get_size()[0]/2),H/2))
                screen.blit(replay_txt,(W/2-(replay_txt.get_size()[0]/2),500))
        pygame.display.update()
        clock.tick(fps)
    else:
        
        if (pygame.time.get_ticks()-inicioJuego)/intervalo3 >= 2:
            game.give_coins()
            intervalo3 += 1000
        for evento in pygame.event.get():
            # evento de boton de cierre de ventana
            if evento.type == pygame.QUIT:
                run = False
            #evento de tecla para invocar una tropa
            if player_red.automatico == False and evento.type == pygame.KEYDOWN and (pygame.time.get_ticks()-inicioJuego)/intervalo >= 1:
                key = evento.key
                player_red.summon_troop(key)
                intervalo += 1000

            if player_blue.automatico == False and evento.type == pygame.KEYDOWN and (pygame.time.get_ticks()-inicioJuego)/intervalo2 >= 1:
                key = evento.key
                player_blue.summon_troop(key)
                intervalo2 += 1000
                
        #modo automatico que genera una tropa enemiga cada cierto tiempo
        if player_red.automatico and (pygame.time.get_ticks()-inicioJuego)/intervalo >= 1:
            if len(red_team) < 2 or (len(blue_team) >= len(red_team) and len(red_team) < 6):
                player_red.summon_troop("")
            intervalo += 1000
        if player_blue.automatico and (pygame.time.get_ticks()-inicioJuego)/intervalo2 >= 1:
            if len(blue_team) < 2 or (len(red_team) >= len(blue_team) and len(blue_team) < 6):
                player_blue.summon_troop("")
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
                    player_red.castle_hp -= blue_team[0].hp_base
                    blue_team.remove(blue_team[0])
        
        if len(red_team) > 0:
            if red_team[0].x > 249:
                red_team[0].speed = 4
            else:
                red_team[0].speed = 0
                red_team[0].drop = 0
                player_blue.castle_hp -= red_team[0].hp_base
                red_team.remove(red_team[0]) 

        if len(blue_team) > 0 and len(red_team) > 0:
            damage = calc_damage(red_team[0],blue_team[0])
            if blue_team[0].colision(red_team[0]) and red_team[0].colision(blue_team[0]) and blue_team[0].hp > 0 and red_team[0].hp > 0:
                blue_team[0].damage_taken = damage[1] #daño que hace red
                red_team[0].damage_taken = damage[0] #daño que hace blue
                blue_team[0].speed = 0
                red_team[0].speed = 0
                if aux == 0:
                    aux = (pygame.time.get_ticks()-inicioJuego)/1000
                blue_team[0].is_attack = True
                red_team[0].is_attack = True
                if (pygame.time.get_ticks()-inicioJuego)/1000 >= aux+3:
                    blue_team[0].is_attack = False
                    red_team[0].is_attack = False
                    aux = 0
            if blue_team[0].hp <= 0:
                blue_team[0].is_death = True
            if red_team[0].hp <= 0:
                red_team[0].is_death = True
        reload_screen()
    clock.tick(fps)
pygame.quit()