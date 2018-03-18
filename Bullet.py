import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # 构造方法：颜值、位置、速度
    # position = 机头位置
    def __init__(self):
        super().__init__()

        # 颜值
        self.mSurface = pygame.image.load("./images/bullet1.png").convert_alpha()
        self.rect = self.mSurface.get_rect()

        # 将子弹的顶部中央对齐机头位置
        # self.reset(position)
        self.isAlive = False

        # 子弹速度
        self.speed = 15

        # 添加碰撞检测遮罩
        self.mask = pygame.mask.from_surface(self.mSurface)

    # 重置子弹位置和生命
    def reset(self, position):
        self.rect.left = position[0] - self.rect.width // 2
        self.rect.bottom = position[1]
        self.isAlive = True

    # 飞行方法
    def move(self):
        if self.rect.bottom > 0:
            self.rect.top -= self.speed
        else:
            self.isAlive = False

