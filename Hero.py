import pygame
from pygame.sprite import Sprite

# 继承于精灵类
class Hero(Sprite):

    # 创建英雄对象
    # 传入窗口宽高参数
    def __init__(self,winWidth,winHeight):

        # 调用精灵父类方法
        super().__init__()

        # 记录窗口宽高
        self.winWidth = winWidth
        self.winHeight = winHeight

        # 加载英雄喷火飞行图片的两帧
        # 这里由于英雄图片有透明区域，因此必须使用convert_alpha()来转化为表面对象
        self.mSurface1 = pygame.image.load("./images/me1.png").convert_alpha()
        self.mSurface2 = pygame.image.load("./images/me2.png").convert_alpha()

        # 以第一幅图片为基准获取矩形对象
        self.rect = self.mSurface1.get_rect()

        # 定义飞行速度
        self.speed = 10

        # 计算英雄出现的位置，此处使其出现的位置位于窗口偏底部的正中央
        # 通过矩形的left和top确定矩形区域的位置
        self.rect.left = self.winWidth // 2 - self.rect.width // 2
        self.rect.top = self.winHeight - 50 - self.rect.height

        # 从mSurface1生成非透明区域遮罩，用于做碰撞检测
        self.mask = pygame.mask.from_surface(self.mSurface1)

    # 向左飞行
    def moveLeft(self):

        # 只要矩形区域的左边缘没有越界，就持续更新精灵矩形的位置
        if self.rect.left > 0:
            self.rect.left -= self.speed

    # 向右飞行：只要右侧没有越界就持续更新矩形位置
    def moveRight(self):
        if self.rect.right < self.winWidth:
            self.rect.left += self.speed

    # 向上飞行：只要矩形顶部没有越界就持续更新矩形的位置
    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed

    # 向下飞行：只要矩形底部没有越界就持续更新矩形的位置
    def moveDown(self):
        if self.rect.bottom < self.winHeight:
            self.rect.bottom += self.speed

    # 按指定向量移动矩形位置
    def move(self,dx,dy):
        self.rect.left += dx
        self.rect.top += dy
