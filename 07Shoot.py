import pygame
import sys

from demos.W3.myplane.Bullet import Bullet
from demos.W3.myplane.Enemy import SmallEnemy
from demos.W3.myplane.Hero import Hero

# 全局初始化
pygame.init()
pygame.mixer.init()

# 设置窗口大小和标题
resolution = width, height = 480, 700
windowSurface = pygame.display.set_mode(resolution)  # 设置分辨率并得到全局的绘图表面
pygame.display.set_caption("飞机大战")

# 加载背景图
bgSurface = pygame.image.load("./images/background.png").convert()

# 加载背景音乐
pygame.mixer.music.load("./sound/game_music.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.4)

# 加载音效
bombSound = pygame.mixer.Sound("./sound/use_bomb.wav")
bulletSound = pygame.mixer.Sound("./sound/bullet.wav")

# 加载字体
textFont = pygame.font.Font("./font/font.ttf", 30)

# 创建时钟对象
clock = pygame.time.Clock()

# 系统常量
ENEMY_NUM = 10
BULLET_NUM = 10

if __name__ == '__main__':

    # 创建英雄实例
    hero = Hero(width, height)

    # 创建敌机Group
    seGroup = pygame.sprite.Group()
    for i in range(ENEMY_NUM):
        se = SmallEnemy(width, height)
        seGroup.add(se)

    # 创建子弹
    bList = []
    bIndex = 0
    for i in range(BULLET_NUM):
        b = Bullet()
        bList.append(b)

    count = 0

    # 开启消息循环
    while True:
        count += 1

        # 处理用户输入
        for event in pygame.event.get():

            # 处理退出事件
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 感应和处理鼠标事件
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("MOUSEBUTTONDOWN @ ", event.pos)
                if hero.rect.collidepoint(event.pos):
                    print("别摸我")

            if event.type == pygame.MOUSEBUTTONUP:
                print("MOUSEBUTTONUP @ ", event.pos)
            if event.type == pygame.MOUSEMOTION:
                # print("MOUSEMOTION @ ", event.pos)
                pass

            # 处理键盘事件
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("开炮!")
                    bombSound.play()

        # 检测当前按下的按钮有哪些
        bools = pygame.key.get_pressed()
        # print(bools)
        if bools[pygame.K_w]:
            hero.moveUp()
        if bools[pygame.K_s]:
            hero.moveDown()
        if bools[pygame.K_a]:
            hero.moveLeft()
        if bools[pygame.K_d]:
            hero.moveRight()

        # 绘制背景
        windowSurface.blit(bgSurface, (0, 0))

        # 绘制英雄
        if count % 3 == 0:
            windowSurface.blit(hero.mSurface1, hero.rect)
        else:
            windowSurface.blit(hero.mSurface2, hero.rect)

        # 绘制敌机
        for se in seGroup:
            windowSurface.blit(se.mSurface, se.rect)

            # 每一帧都让敌机飞行5公里
            se.move()

        # 每10帧在机头射出一颗子弹
        if count % 10 == 0:
            b = bList[bIndex]  # 取出一颗子弹
            b.reset(hero.rect.midtop)  # 立即装载到【当前】机头位置
            # windowSurface.blit(b.mSurface, b.rect)  # 画子弹
            bulletSound.play()#呼啸声

            bIndex = (bIndex + 1) % BULLET_NUM  # 序号递增

        # 每帧都让子弹飞
        for b in bList:
            if b.isAlive:
                windowSurface.blit(b.mSurface, b.rect)  # 画子弹
                b.move()

        # 绘制文字
        textSurface = textFont.render("Score:00000", True, (255, 255, 255))
        windowSurface.blit(textSurface, (10, 10))

        # 精灵碰撞检测

        # 刷新界面
        pygame.display.flip()

        # 时钟停留一帧的时长
        clock.tick(60)
        pass
