#引入外部依赖文件
import pygame
from pygame.locals import *
import time
import random

#所有物品的基类
class Base(object):
    def __init__(self,screenTemp,x,y,imageName):
        self.x=x
        self.y=y
        self.screen=screenTemp
        self.image=pygame.image.load(imageName)
class BasePlane(Base):
    def __init__(self,screenTemp,x,y,imageName):
        Base.__init__(self,screenTemp,x,y,imageName)
        self.bulletList=[];
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bulletList.remove(bullet)
class HeroPlane(BasePlane):
    def __init__(self,screenTemp):
        BasePlane.__init__(self,screenTemp,201,700,'./feiji/hero1.png')
    def moveLeft(self):
        self.x-=5
    def moveRight(self):
        self.x+=5
    def fire(self):
        self.bulletList.append(Bullet(self.screen,self.x,self.y))
class EnemyPlane(BasePlane):
    def __init__(self,screenTemp):
        BasePlane.__init__(self,screenTemp,0,0,'./feiji/enemy0.png')
        self.direction="right"
    def move(self):
        if self.direction=="right":
            self.x+=5;
        elif self.direction=="left":
            self.x-=5
        if self.x>480-50:
            self.direction="left"
        if self.x<0:
            self.direction="right"
    def fire(self):
        randomNum=random.randint(1,100)
        if randomNum==8 or randomNum==20:
            self.bulletList.append(EnemyBullet(self.screen,self.x,self.y))


#子弹类应该先定义
class BaseBullet(Base):
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
#子弹类
class Bullet(BaseBullet):
    def __init__(self,screenTemp,x,y):
        BaseBullet.__init__(self,screenTemp,x,y,"./feiji/bullet.png")
    #子弹移动的方法
    def move(self):
        self.y-=20
    #判断子弹是否越界
    def judge(self):
        if self.y<0:
            return  True
        else:
            return False
class EnemyBullet(BaseBullet):
    def __init__(self,screenTemp,x,y):
        BaseBullet.__init__(self,screenTemp,x+25,y+40,"./feiji/bullet1.png")
    def move(self):
        self.y+=5
    def judge(self):
        if self.y>852:
            return  True
        else:
            return False
def keyControl(heroTemp):
    for event in pygame.event.get():
        if event.type==QUIT:
            print("exit")
            exit()
        elif event.type==KEYDOWN:
            if event.key==K_a or event.key==K_LEFT:
                print("left----")
                heroTemp.moveLeft()
            elif event.key==K_d or event==K_RIGHT:
                print("right---")
                heroTemp.moveRight()
            elif event.key==K_SPACE:
                print("space----")
                heroTemp.fire()
def main():
    screen=pygame.display.set_mode((480,852),0,32)
    backgroud=pygame.image.load("./feiji/background.png")
    hero=HeroPlane(screen)
    enemy=EnemyPlane(screen)
    while True:
        screen.blit(backgroud,(0,0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()
        pygame.display.update()
        keyControl(hero)
        time.sleep(0.01)
if __name__=="__main__":
    main()

