import random

import pygame
from pygame.sprite import Sprite


# 敌机类
class SmallEnemy(Sprite):
    # 构造方法：确定颜值、确定初始位置、引擎功率
    def __init__(self, winWidth, winHeight):
        Sprite.__init__(self)
        self.winWidth = winWidth
        self.winHeight = winHeight

        # 外形
        self.mSurface = pygame.image.load("./images/enemy1.png").convert_alpha()

        # 爆炸
        self.dSurface1 = pygame.image.load("./images/enemy1_down1.png").convert_alpha()
        self.dSurface2 = pygame.image.load("./images/enemy1_down2.png").convert_alpha()
        self.dSurface3 = pygame.image.load("./images/enemy1_down3.png").convert_alpha()
        self.dSurface4 = pygame.image.load("./images/enemy1_down4.png").convert_alpha()
        self.dList = [self.dSurface1, self.dSurface2, self.dSurface3, self.dSurface4]
        self.dIndex = 0

        # 确定敌机位置
        self.rect = self.mSurface.get_rect()
        self.reset()

        # 敌机飞行速度
        self.speed = 5

        # 添加碰撞检测遮罩
        self.mask = pygame.mask.from_surface(self.mSurface)

    # 重置敌机位置和生命
    def reset(self):
        self.rect.left = random.randint(0, self.winWidth - self.rect.width)
        self.rect.top = 0 - random.randint(0, 1000)
        self.isAlive = True
        self.dIndex = 0

    # 机械地向下飞行
    def move(self):
        if self.rect.top < self.winHeight:
            self.rect.bottom += self.speed
        else:
            self.isAlive = False
            self.reset()

    # fCount=当前第几帧
    def destroy(self, fCount, winSurface,dSound):
        winSurface.blit(self.dList[self.dIndex],self.rect)

        if fCount % 3 == 0:
            # 切下一副面孔
            self.dIndex += 1

        if self.dIndex == 4:
            dSound.play()
            self.reset()

