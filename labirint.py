# Разработай свою игру в этом файле!
from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        super().__init__(picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def move(self):
        if self.x_speed <= 0 and self.rect.x >= 0:   
            self.rect.x += self.x_speed
        elif self.x_speed >= 0 and self.rect.x <= 625:
            self.rect.x += self.x_speed
        if self.y_speed <= 0 and self.rect.y >= 0:   
            self.rect.y += self.y_speed
        elif self.y_speed > 0 and self.rect.y <= 425:
            self.rect.y += self.y_speed
    def fire(self):
        bullet = Bullet('bullet.png', 5, 5, player1.rect.centerx, player1.rect.centery, 0, 0)
        if e.key == K_w:
            bullet.y_speed = -20
        elif e.key == K_s:
            bullet.y_speed = 20
        elif e.key == K_a:
            bullet.x_speed = -20
        elif e.key == K_d:
            bullet.x_speed = 20
        bullets.add(bullet)
class Bullet(GameSprite):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        super().__init__(picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def move(self):   
            self.rect.x += self.x_speed  
            self.rect.y += self.y_speed
            if sprite.collide_rect(self, wall1) or sprite.collide_rect(self, wall2) or sprite.collide_rect(self, wall3):
                self.kill()
            if self.rect.x < 0 or self.rect.x > 700 or self.rect.y < 0 or self.rect.y > 500:
                self.kill()
v = 15
window = display.set_mode((700, 500))
back = (51, 133, 45)
window.fill(back)
picture1 = image.load('space_2.jpg')
picture1 = transform.scale(picture1, (700, 500))
display.set_caption('Pac-Man')
wall1 = GameSprite('wall1.png', 300, 50, 400, 400)
wall2 = GameSprite('wall1.png', 50, 300, 300, 300)
wall3 = GameSprite('wall1.png', 400, 70, 200, 300)
fin = GameSprite('trophy.png', 50, 50, 650, 0)
player1 = Player('pac-1.png', 75, 75, 0, 400, 0, 0)
player2 = Player('pac-2.png', 75, 75, 300, 180, 0, -5)
fin_pic = image.load('thumb_1.jpg')
fin_pic = transform.scale(fin_pic, (700, 500))
bullets = sprite.Group()
display.update()
run = True
finish = False
lose_pic = transform.scale(image.load('fail_1.jpg'), (700, 500))
while run:
    time.delay(50)
    window.blit(picture1, (0, 0))
    wall1.reset()
    wall2.reset()
    wall3.reset()
    bullets.draw(window)
    fin.reset()
    player1.reset()
    player2.reset()
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                player1.y_speed = -v
            elif e.key == K_DOWN:
                player1.y_speed = v
            elif e.key == K_RIGHT:
                player1.x_speed = v
                player1.y_speed = 0
            elif e.key == K_LEFT:
                player1.x_speed = -v
                player1.y_speed = 0
            if e.key in (K_w, K_s, K_a, K_d):
                player1.fire()
        elif e.type == KEYUP:
            if e.key == K_UP:
                player1.y_speed = 0
                player1.x_speed = 0
            elif e.key == K_DOWN:
                player1.y_speed = 0
                player1.x_speed = 0
            elif e.key == K_RIGHT:
                player1.x_speed = 0
                player1.y_speed = 0
            elif e.key == K_LEFT:
                player1.x_speed = 0
                player1.y_speed = 0
    player1.move()
    bullets.update()
    if sprite.collide_rect(player2, wall3):
        player2.y_speed = -player2.y_speed
    if player2.rect.y == 0:
        player2.y_speed = -player2.y_speed
    player2.move()
    if sprite.collide_rect(player1, fin):
        finish = True
        window.blit(fin_pic, (0, 0))
    elif sprite.collide_rect(player1, wall1) or sprite.collide_rect(player1, wall2) or sprite.collide_rect(player1, wall3) or sprite.collide_rect(player1, player2):
        finish = True
        window.blit(lose_pic, (0, 0))
    if sprite.spritecollide(player2, bullets, True):
        player2.kill()
        player2.rect.x = 1000
    display.update()
