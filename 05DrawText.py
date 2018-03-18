import pygame
import sys

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
bombSound = pygame.mixer.Sound("./sound/use_bomb.wav")

# 加载字体
textFont = pygame.font.Font("./font/font.ttf",30)

# 创建时钟对象
clock = pygame.time.Clock()

if __name__ == '__main__':

    # 创建英雄实例
    hero = Hero(width, height)
    wingman = Hero(width, height)#僚机
    wingman.move(100,50)

    # 建立待碰撞检测的精灵Group
    mGroup = pygame.sprite.Group()
    mGroup.add(wingman)

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

        if bools[pygame.K_UP]:
            wingman.moveUp()
        if bools[pygame.K_DOWN]:
            wingman.moveDown()
        if bools[pygame.K_LEFT]:
            wingman.moveLeft()
        if bools[pygame.K_RIGHT]:
            wingman.moveRight()

        # 绘制背景
        windowSurface.blit(bgSurface, (0, 0))

        # 绘制飞机
        if count % 3 == 0:
            windowSurface.blit(hero.mSurface1, hero.rect)
        else:
            windowSurface.blit(hero.mSurface2, hero.rect)

        # 绘制僚机
        windowSurface.blit(wingman.mSurface1,wingman.rect)

        # True = 抗锯齿
        # (255,255,255) = 使用白色绘制
        # 返回值textSurface = 返回要绘制的文字表面
        textSurface = textFont.render("Score:00000",True,(255,255,255))

        # 绘制文字在(10,10)位置
        windowSurface.blit(textSurface,(10,10))

        # 精灵碰撞检测
        hitSpriteList = pygame.sprite.spritecollide(hero,mGroup,False,pygame.sprite.collide_mask)
        if len(hitSpriteList) > 0:
            print("Would you please fuck off?!")
            # bombSound.play()

        # 刷新界面
        pygame.display.flip()

        # 时钟停留一帧的时长
        clock.tick(60)
        pass
