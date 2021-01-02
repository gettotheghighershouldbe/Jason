import pygame

Hello_Rect = pygame.Rect(100, 120, 60, 70)

print("坐标原点 %d %d" % (Hello_Rect.x, Hello_Rect.y))
print("宽度是 %d 高度是 %d" % (Hello_Rect.width, Hello_Rect.height))
print("size是 %d %d" % Hello_Rect.size)


print(Hello_Rect)