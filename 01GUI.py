import pygame
import sys

# 全局初始化
pygame.init()

# 设置窗口的分辨率和标题
resolution = width,height = 480,700 #设置窗口大小和标题
windowSurface = pygame.display.set_mode(resolution) #设置分辨率并得到全局的【绘图表面】
pygame.display.set_caption("飞机大战")#设置标题

#加载背景图，返回的表面可以用于绘制其它对象于其上
bgSurface = pygame.image.load("./images/background.png").convert()

# 创建时钟对象
clock = pygame.time.Clock()

if __name__ == '__main__':

    # 开启消息循环
    while True:

        # 处理用户输入
        for event in pygame.event.get():

            # 处理退出事件
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 将背景图像绘制于窗口表面windowSurface
        windowSurface.blit(bgSurface, (0, 0))

        # 绘制结束，刷新界面
        pygame.display.flip()

        # 时钟停留一帧的时长
        clock.tick(60)