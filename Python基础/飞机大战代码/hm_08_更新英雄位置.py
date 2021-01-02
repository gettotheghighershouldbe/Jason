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

# 3.创建时钟对象
clock = pygame.time.Clock()

# 1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 500, 102, 126)

# 游戏循环 -> 意味着游戏的正式开始

while True:

    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)

    # 2. 修改飞机的位置
    hero_rect.y -= 1

    if hero_rect.y <= -126:
        hero_rect.y = 700

    # 3.调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 4.调用update方法显示更新
    pygame.display.update()


pygame.quit()

