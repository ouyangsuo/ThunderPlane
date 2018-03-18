import pygame
from pygame.sprite import Sprite


class PauseButton(Sprite):
    def __init__(self,winWidth,winHeight,paused):
        super().__init__()
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.paused = paused

        # 颜值
        self.sPauseNor = pygame.image.load("./images/pause_nor.png").convert_alpha()
        self.sPausePressed = pygame.image.load("./images/pause_pressed.png").convert_alpha()
        self.sResumeNor = pygame.image.load("./images/resume_nor.png").convert_alpha()
        self.sResumePressed = pygame.image.load("./images/resume_pressed.png").convert_alpha()
        self.currentSurface = self.sPauseNor
        self.rect = self.sPauseNor.get_rect()

        # 位置
        self.rect.right = self.winWidth - 10
        self.rect.top = 10

    def onBtnClick(self, paused):
        self.paused = paused
        if self.paused:
            self.currentSurface = self.sResumeNor
            # print("sResumeNor")
        else:
            self.currentSurface = self.sPauseNor
            # print("sPauseNor")

    def onBtnHover(self):
        # print("onBtnHover")
        if self.paused:
            self.currentSurface = self.sResumePressed
            # print("sResumePressed")
        else:
            self.currentSurface = self.sPausePressed
            # print("sPausePressed")

    def onBtnOut(self):
        # print("onBtnOut")
        if self.paused:
            self.currentSurface = self.sResumeNor
            # print("sResumeNor")
        else:
            self.currentSurface = self.sPauseNor
            # print("sPauseNor")
