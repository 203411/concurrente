import pygame

W = 600

class Troop(pygame.sprite.Sprite):
    def __init__(self,type_troop,team):
        super().__init__()
        self.type = type_troop
        self.team = team
        #Spawnpoint
        if self.team == "red":
            self.rect = pygame.Rect(0,136,64,64)
        else:
            self.rect = pygame.Rect(540,136,64,64)

        if self.type == "archer":
            self.images = [
                pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_walk1.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_walk2.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_attack1.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_attack2.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_attack3.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_attack4.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_attack5.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_attack6.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_attack7.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_death1.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_death2.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_death3.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_death4.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_death5.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/archer/'+self.team+'/archer_death6.png'),(64,64))
            ]
            self.walk_anim = (0,2)
            self.attack_anim = (2,9)
            self.death_anim = (9,14)
            self.hp = 6
        if self.type == "knight":
            self.images = [
                pygame.transform.flip(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_walk1.png'),(64,64)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_walk2.png'),(64,64)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_attack1.png'),(64,64)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_attack2.png'),(64,64)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_attack3.png'),(64,64)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_attack4.png'),(64,64)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_attack5.png'),(64,64)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_attack6.png'),(64,64)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_death1.png'),(64,64)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_death2.png'),(64,64)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_death3.png'),(64,64)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_death4.png'),(64,64)),True,False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load('./assets/sprites/knight/'+self.team+'/knight_death5.png'),(64,64)),True,False),
            ]
            self.walk_anim = (0,2)
            self.attack_anim = (2,8)
            self.death_anim = (8,13)
            self.hp = 9
        if self.type == "lancer":
            self.images = [
                pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_walk1.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_walk2.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_attack1.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_attack2.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_attack3.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_attack4.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_death1.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_death2.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_death3.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_death4.png'),(64,64)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/lancer/'+self.team+'/lancer_death5.png'),(64,64)),
            ]
            self.walk_anim = (0,2)
            self.attack_anim = (2,6)
            self.death_anim = (6,11)
            self.hp = 12
        if self.type == "dragon":
            self.images = [
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_run1.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_run2.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_run3.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_run4.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_run5.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_run6.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_attack1.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_attack2.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_attack3.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_attack4.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_attack5.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_attack6.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_attack7.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_attack8.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_attack9.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_attack10.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death1.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death2.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death3.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death4.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death5.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death6.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death7.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death8.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death9.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death10.png'),(128,128)),
                pygame.transform.scale(pygame.image.load('./assets/sprites/dragon/'+self.team+'/dragon_death11.png'),(128,128)),
            ]
            self.walk_anim = (0,6)
            self.attack_anim = (6,16)
            self.death_anim = (16,27)
            self.hp = 50
            if self.team == "red":
                self.rect = pygame.Rect(0,102,128,128)
            else:
                self.rect = pygame.Rect(500,102,128,128)
        self.aux = 1000
        self.conta = 0
        self.index = 0
        self.image = self.images[self.index]
        self.speed = 4
        self.damage_taken = 0
        self.attacking = False

    def walk(self):
        self.anim(self.walk_anim)
        if self.rect.x > W-64:
            self.speed = -self.speed
        if self.rect.x <= 0:
            self.speed = 4

        self.rect.x += self.speed

    def attack(self):
        self.anim(self.attack_anim)
        if pygame.time.get_ticks()/self.aux >= 1:
            self.conta += 1
            self.aux += 1000
        if self.conta >= 5:
            self.speed = self.speed_initial
            self.conta = 0

    def death(self):
        self.index += 1
        if self.index >= self.death_anim[1]:
            self.index = self.death_anim[0]
            self.kill()
        self.image = pygame.transform.flip(self.images[self.index],self.speed_initial > 0,False)

    def anim(self,limits):
        self.index += 1
        if self.index >= limits[1]:
            self.index = limits[0]
            if self.attacking:
                # print(self.type,self.team," hp: ",self.hp)
                self.hp -= self.damage_taken
                # print("despues del ataque ")
                # print(self.type,self.team," hp: ",self.hp)
        self.image = pygame.transform.flip(self.images[self.index],self.speed_initial > 0,False)

    def update(self):
        if self.hp <= 0:
            self.death()
        else:
            if self.speed != 0: 
                self.speed_initial = self.speed
                self.walk()
                self.attacking = False
            else:
                if self.attacking == False:
                    self.anim(self.walk_anim)
                else:
                    # self.attacking = True
                    self.attack()
