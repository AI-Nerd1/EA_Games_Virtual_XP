
import pygame
import random
import os

from pygame.compat import geterror
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.display.set_caption("Space Invader")
# jet_pic = pygame.image.load("jet2.png")
# cloud_pic = pygame.image.load("cloud1.png")
# bullet_pic =pygame.image.load('bullet1.png')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
       # self.surf = jet_pic.convert()
        # self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((255, 140, 0))
        self.rect = self.surf.get_rect()



# Player movement
    def update(self, pressed_keys):
        if pressed_keys [K_UP]:
            self.rect.move_ip(0, -2)
        if pressed_keys [K_DOWN]:
            self.rect.move_ip(0, 2)
        if pressed_keys [K_LEFT]:
            self.rect.move_ip(-2, 0)
        if pressed_keys [K_RIGHT]:
            self.rect.move_ip(2, 0)

# Player limit to screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        #self.surf = bullet_pic.convert()
        # self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(0, 4)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        # self.surf = cloud_pic
        self.surf = pygame.Surface((30, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(0, 2)

    def update(self):
        self.rect.move_ip(-3, 0)
        if self.rect.right < 0:
            self.kill()


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1200)
player = Player()
enemies = pygame.sprite.Group()
cloud = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


running = True
while running:
    screen.fill((135, 206, 235))
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False

        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            cloud.add(new_cloud)
            all_sprites.add(new_cloud)

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()
    cloud.update()

    surf = pygame.Surface((50, 50))       # Rectangle size

   # surf_center =\
     #   (
     #       (SCREEN_WIDTH - surf.get_width())/2,
     #       (SCREEN_HEIGHT - surf.get_height())/2
     #   )
    # screen.fill((135, 206, 235))                      # Screen color
    # surf.fill((225, 255, 255))                 # Player color
    # screen.blit(surf, surf_center)           # Coordinates for rectangle
    # screen.blit(player.surf, player.rect)

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False

    rect = surf.get_rect()

    
    # pygame.display.flip()

    # Flip the display
    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(200)

pygame.quit()