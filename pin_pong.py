from pygame import *
from random import randint
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
        if keys[K_w] and self.rect.y > -150:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 75: 
            self.rect.y += self.speed 

    def rocet_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > -150:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 75: 
            self.rect.y += self.speed 

class Ball(sprite.Sprite):
    def __init__(self, player_image, plaer_x, plaer_y, plaer_speed_x, plaer_speed_y, rect_with, rect_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (rect_with, rect_height))
        self.speed_x = plaer_speed_x
        self.speed_y = plaer_speed_y
        self.rect = self.image.get_rect()
        self.rect.x = plaer_x
        self.rect.y = plaer_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y



win_width = 700
win_height = 600
window = display.set_mode((win_width, win_height))
display.set_caption('pin_pong')
background = transform.scale(image.load('sky.jpg'), (win_width, win_height))

z = 10
plaer_left = Rocet('rocket.png', 50, 0, z, 60, 200)
plaer_right = Rocet('rocket.png', (win_width - 110), 0, z, 60, 200)

b = 2
ball = Ball('ball.png', (win_height/2), (win_width/2), b, b, 60, 60)

game = True
finish = False
clock = time.Clock()
FPS = 60

font2 = font.SysFont('Arial', 36)
font1 = font.SysFont('Arial', 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))

x = 1
y = 1
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0 ,0))

    
    plaer_left.rocet_left()
    plaer_right.rocet_right()
    ball.move()

    if sprite.collide_rect(plaer_left, ball) or sprite.collide_rect(plaer_right, ball):
        ball.speed_x *= -1
        ball.speed_y *= 1
    
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        ball.speed_y /= -1

    if ball.rect.x < 0 or ball.rect.x > win_width:
        finish = True
        window.blit(lose, (200, 200))



    plaer_left.reset()
    plaer_right.reset()
    ball.reset()

    
    clock.tick(FPS)
    display.update()