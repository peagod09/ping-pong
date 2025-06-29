from pygame import * 
window = display.set_mode((700,500))
game = True
finish = False
from random import *
clock = time.Clock()
mixer.init()
font.init()
background = transform.scale(image.load('задний фон.jpg'),(700,500))

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
        player1.update1()
        player1.reset()
        player2.update2()
        player2.reset()
        ball.reset()
        display.update()
    clock.tick(60)