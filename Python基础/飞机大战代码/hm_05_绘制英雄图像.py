import pygame

pygame.init()

# 创建游戏主窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1> 加载图像数据
bg = pygame.image.load("./Images/background.png")
# 2> blit 绘制图像
screen.blit(bg, (0, 0))
# 3> update 更新屏幕的显示
pygame.display.update()

# 英雄的飞机
hero = pygame.image.load("./Images/me1.png")
screen.blit(hero, (150, 500))
pygame.display.update()

# 游戏循环
while True:
    pass

pygame.quit()
