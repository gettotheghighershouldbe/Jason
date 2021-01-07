import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 60

class GameSpirite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        print(self.rect)
        print("是rect调用了吗?")
        self.speed = speed

    def __createsprites__(self):
        pass

    def update(self):
        # 在屏幕的垂直方向移动
        self.rect.y += self.speed

class Background(GameSpirite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):

        # 1.调用父类方法,实现精灵的创建(image/rect/speed)
        super().__init__("./images/background.png")

        # 2.判断是否是交替图像,如果是,需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 1.调用父类的方法实现
        super().update()
        # 2.判断是否移出屏幕,如果移出屏幕,将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
        # if self.rect.y >= self.rect.height: 也是在做个实验
            self.rect.y = -self.rect.height










































