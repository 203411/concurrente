import pygame, sys, time
from sprites_tropa import Troop
pygame.init()

#color
BG = (201,194,190)
W = 600
H = 400
size = (W,H)
fps = 8
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()

all_sprite_list = pygame.sprite.Group()
red_team = pygame.sprite.Group()
blue_team = pygame.sprite.Group()

def summon_troop(troop_type,team):
    troop = Troop(troop_type,team)
    if team == "red":
        red_team.add(troop)
    else:
        blue_team.add(troop)

intervalo = 1000
run = True
while run:
    screen.fill(BG)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and pygame.time.get_ticks()/intervalo >= 1:
            if event.key == pygame.K_q:
                summon_troop("archer","red")
            if event.key == pygame.K_w:
                summon_troop("knight","red")
            if event.key == pygame.K_e:
                summon_troop("lancer","red")
            if event.key == pygame.K_r:
                summon_troop("dragon","red")
            if event.key == pygame.K_u:
                summon_troop("archer","blue")
            if event.key == pygame.K_i:
                summon_troop("knight","blue")
            if event.key == pygame.K_o:
                summon_troop("lancer","blue")
            if event.key == pygame.K_p:
                summon_troop("dragon","blue")
            intervalo += 1000

    red_team.update()
    blue_team.update()
    red_team.draw(screen)
    blue_team.draw(screen)

    list_red_troops = red_team.sprites()
    #Formarlos en una fila
    for troop_red in red_team:
        if troop_red == red_team.sprites()[0]:
            if troop_red.rect.x == (W/2)-60:
                troop_red.speed = 0

    for troop_blue in blue_team:
        if troop_blue.rect.x == (W/2):
            troop_blue.speed = 0

    hits = pygame.sprite.groupcollide(blue_team,red_team,False,False)
    for hit in hits:
        hit.attacking = True
        hits[hit][0].attacking = True
        #damage done by blue troop
        if hit.hp > 0:
            if hit.type == "archer":
                if hits[hit][0].type == "lancer":
                    hits[hit][0].damage_taken = 8
                else:
                    hits[hit][0].damage_taken = 4
            if hit.type == "knight":
                if hits[hit][0].type == "archer":
                    hits[hit][0].damage_taken = 6
                else:
                    hits[hit][0].damage_taken = 3
            if hit.type == "lancer":
                if hits[hit][0].type == "knight":
                    hits[hit][0].damage_taken = 6
                else:
                    hits[hit][0].damage_taken = 3
            if hit.type == "dragon":    
                hits[hit][0].damage_taken = 12
        else:
            hits[hit][0].damage_taken = 0
            hits[hit][0].speed = hits[hit][0].speed_initial
        #damage done by red troop
        if hits[hit][0].hp > 0:
            if hits[hit][0].type == "archer":
                if hit.type == "lancer":
                    hit.damage_taken = 8
                else:
                    hit.damage_taken = 4
            if hits[hit][0].type == "knight":
                if hit.type == "archer":
                    hit.damage_taken = 6
                else:
                    hit.damage_taken = 3
            if hits[hit][0].type == "lancer":
                if hit.type == "knight":
                    hit.damage_taken = 6
                else:
                    hit.damage_taken = 3
            if hits[hit][0].type == "dragon":    
                hit.damage_taken = 12
        else:
            hit.damage_taken = 0
            hit.speed = hit.speed_initial

    pygame.display.update()
    clock.tick(fps)