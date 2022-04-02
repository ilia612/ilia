from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y,player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
font.init()
font1 = font.Font(None, 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
display.set_caption("Shooter")
window = display.set_mode((700, 500))
background = transform.scale(image.load('red-among-us-png.jpg'), (700, 500))
plat=GameSprite('red-among-us-png.jpg сбрасывается кнопкой закрытия
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.blit(background,(0,0))
    plat.reset()

    text = font1.render("LETS GO: " , 1, (255, 255, 255))
    window.blit(text, (10, 20))
    display.update()
    time.delay(50)



            