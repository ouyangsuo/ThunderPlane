import pygame
import sys

# 全局初始化
pygame.init()

# 设置窗口大小和标题
resolution = width, height = 480, 700
windowSurface = pygame.display.set_mode(resolution)  # 设置分辨率并得到全局的绘图表面
pygame.display.set_caption("飞机大战")

# 加载背景图
bgSurface = pygame.image.load("./images/background.png").convert()

# 创建时钟对象
clock = pygame.time.Clock()

if __name__ == '__main__':

    # 开启消息循环
    while True:

        # 处理用户事件
        for event in pygame.event.get():
            print(event.type)

            # 处理退出事件
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 感应和处理鼠标事件
            # 在鼠标按下、抬起、移动时打印事件发生的位置
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("MOUSEBUTTONDOWN @ ", event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                print("MOUSEBUTTONUP @ ", event.pos)
            if event.type == pygame.MOUSEMOTION:
                print("MOUSEMOTION @ ", event.pos)
                pass

            # 处理键盘事件
            # 这种键盘监听方式用于一次性地处理键盘按下，例如开炮等
            if event.type == pygame.KEYDOWN:

                # 按下空格时输出开炮
                if event.key == pygame.K_SPACE:
                    print("开炮!")

                # 按下左方向键时输出“左”
                if event.key == pygame.K_LEFT:
                    print("左")

        # 检测当前帧按下的按钮有哪些
        # 返回的是一堆布尔值形成的元组，每一个元素的下标对应的是按键的keycode
        # (0,0,1,1,0...)代表当前帧中2号键和3号键同时被按下
        # 这种键盘监听方式用于持续地处理键盘按下事件，例如持续飞行
        bools = pygame.key.get_pressed()
        print(bools)
        if bools[pygame.K_UP] == 1:
            print("上")
        if bools[pygame.K_DOWN] == 1:
            print("下")
        if bools[pygame.K_LEFT] == 1:
            print("左")
        if bools[pygame.K_RIGHT] == 1:
            print("右")

        # 绘制背景
        windowSurface.blit(bgSurface, (0, 0))

        # 刷新界面
        pygame.display.flip()

        # 时钟停留一帧的时长
        clock.tick(60)
        pass
