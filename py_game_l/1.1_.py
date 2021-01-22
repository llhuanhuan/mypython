# ##游戏
# import sys                                      ##导入sys模块
# import pygame                                   ##导入pygame模块

# pygame.init()                                   ##初始化pygame
# size = widthheight = 320,240                    ##设置窗口
# scream = pygame.display.set_mode(size)          ##显示窗口

# ##执行死循环，确保窗口一直开启
# while True:
#     ##检查事件
#     for event in pygame.event.get():            ##遍历所有事件
#         if event.type == pygame.QUIT:           ##如果单击关闭窗口，则退出
#             sys.exit()

# pygame.quit()                                   ##退出pygame




# ##小球移动游戏
# import sys, pygame                              ##导入sys和pygame模块
# pygame.init()                                   ##初始化pygame模块
    
# size = width, height = 640,480                  ##设置窗口
# screen = pygame.display.set_mode(size)          ##显示窗口

# speed = [2, 2]                  
# black = 0, 0, 0



# ball = pygame.image.load("E:\\pythonstduy\\py_game_l\\xiaoqiu.gif")
# ballrect = ball.get_rect()

# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()

#     ballrect = ballrect.move(speed)
#     if ballrect.left < 0 or ballrect.right > width:
#         speed[0] = -speed[0]
#     if ballrect.top < 0 or ballrect.bottom > height:
#         speed[1] = -speed[1]

#     screen.fill(black)
#     screen.blit(ball, ballrect)
#     pygame.display.flip()



##Example
import sys, pygame                              ##导入sys和pygame模块
pygame.init()                                   ##初始化pygame模块
    
size = width, height = 640,480                  ##设置窗口
screen = pygame.display.set_mode(size)          ##显示窗口
color = (0,0,0)                                 ##设置颜色

ball = pygame.image.load("E:\\pythonstduy\\py_game_l\\ball.png")     ##加载图片,ball值相当于一个Surface对象。
ballrect = ball.get_rect()                                           ##获取矩形区域
speed = [5,5]                                                        ##设置移动的X轴，Y轴距离
clock = pygame.time.Clock()                                          ##设置时钟

##执行死循环，确保窗口一直显示
while True:
    clock.tick(60)                              ##设置每秒执行60次
    ##检查事件
    for event in pygame.event.get():            ##pygame.event.get() 能够获取事件队列
        if event.type == pygame.QUIT:           ##pygame.QUI 表示检测到关闭pygame窗口事件，如果单击关闭窗口，则退出
            sys.exit()

    ballrect = ballrect.move(speed)             ##移动小球
    ##添加碰撞检测，如果不添加碰撞检测的话，小球将会在屏幕中一闪而过
    ##碰到左右边缘
    if ballrect.left < 0 | ballrect.right> width:
        speed [0] = -speed[0]                   ##更改x轴的数据为负值
    ##碰到上下边缘
    if ballrect.top < 0 | ballrect.bottom> height:
        speed [1] = -speed[1]                   ##更改Y轴的数据为负值
    screen.fill(color)                          ##填充颜色
    screen.blit(ball,ballrect)                  ##将图片画到窗口上
    pygame.display.flip()                       ##更新全部显示

pygame.quit()                                   ##退出pygame
