from pygame import *
from random import randint
mixer.init()
font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, plaer_x, plaer_y, plaer_speed, rect_with, rect_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (rect_with, rect_height))
        self.speed = plaer_speed
        self.rect = self.image.get_rect()
        self.rect.x = plaer_x
        self.rect.y = plaer_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Rocet(GameSprite):
    def rocet_left(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed 

    def rocet_right(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed 


    # def fire(self):
    #     bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, -15, 15, 20)
    #     bullets.add(bullet)
    #     global score
    #     score += 1

# class Enemy(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         global lost
#         if self.rect.y > win_height:
#             self.rect.x = randint(80, win_width-80)
#             self.rect.y = 0
#             lost += 1

win_width = 700
win_height = 530
window = display.set_mode((win_width, win_height))
display.set_caption('pin_pong')
background = transform.scale(image.load('sky.jpg'), (win_width, win_height))

z = 10
plaer = Rocet('rocket.png', 100, 435, z, 60, 80)

game = True
finish = False
clock = time.Clock()
FPS = 60

font2 = font.SysFont('Arial', 36)
font1 = font.SysFont('Arial', 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0 ,0))

    plaer.update()
    plaer.reset()

    clock.tick(FPS)
    display.update()