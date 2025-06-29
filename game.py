from pygame import * 
window = display.set_mode((700,500))
game = True
finish = False
from random import *
clock = time.Clock()
speed_x = 3
speed_y = 3
mixer.init()
font.init()
background = transform.scale(image.load('задний фон.jpg'),(700,500))
font1 = font.Font(None,35)
lose1 = font1.render('PLAYER 1 LOSE', True,(180,0,0))
lose2 = font1.render('PLAYER 2 LOSE', True,(180,0,0))

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_speed,player_x,player_y,scale_w,scale_h):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(scale_w,scale_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
            finish = False
player1 = Player('platform.png',4,30,200,50,150)
player2 = Player('platform.png',4,620,200,50,150)
ball = GameSprite('ball.png',4,350,250,50,50)
while game == True:
    for even in event.get():
        if even.type == QUIT:
            game = False
    if finish == False:
        window.blit(background,(0,0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200,200))
        if ball.rect.x > 650:
            finish = True
            window.blit(lose2,(200,200))
        player1.update1()
        player1.reset()
        player2.update2()
        player2.reset()
        ball.reset()
        display.update()
    clock.tick(60)
