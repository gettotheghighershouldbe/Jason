import pygame

# 游戏初始化
pygame.init()

# 创建游戏主窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./Images/background.png")
screen.blit(bg, (0, 0))
# pygame.display.update()

# 英雄的飞机
hero = pygame.image.load("./Images/me1.png")
screen.blit(hero, (150, 500))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 游戏循环 -> 意味着游戏的正式开始
i = 0

while True:

    # 可以指定循环体内部的代码执行的频率
    clock.tick(1)

    print(i)

    i += 1

    pass

pygame.quit()

