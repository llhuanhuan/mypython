import sys, pygame ,random                             ##导入sys、pygame、random模块

class Bird(object):
    ##定义一个鸟类
    def __init__(self):
        ##定义初始化的方法
        self.birdRect = pygame.Rect(65,50,50,50)       ##鸟的矩形
        ##定义鸟的三种状态
        self.birdStatus = [pygame.image.load("E:\\pythonstduy\\py_game_l\\1.png"),
            pygame.image.load("E:\\pythonstduy\\py_game_l\\2.png"),
            pygame.image.load("E:\\pythonstduy\\py_game_l\\dead.png")]
        self.status = 0                                 ##默认飞行状态
        self.birdX = 120                                ##鸟所在X轴坐标
        self.birdY = 350                                ##鸟所在Y轴坐标
        self.jump = False                               ##默认情况下小鸟自动降落
        self.jumpSpeed = 10                             ##跳跃高度
        self.gravity = 5                                ##重力
        self.dead = False                               ##默认小鸟生命状态为活着

    def birdUpdate(self):
        if self.jump:                                   
            ##小鸟跳跃
            self.jumpSpeed -= 1                         ##速度递减，上升越来越慢
            self.birdY -= self.jumpSpeed                ##鸟Y轴坐标减小，小鸟上升
        else:
            ##小鸟坠落
            self.gravity += 0.2                         ##重力增加，下降越来越快
            self.birdY += self.gravity                  ##鸟Y轴坐标增大，小鸟下降
        self.birdRect[1] = self.birdY                   ##更改Y轴坐标
                

class Pipeline(object):
    ##定义一个管道类
    def __init__(self):
        ##定义初始化的方法
        self.wallx = 400                                ##管道所在X轴坐标
        self.pineUP = pygame.image.load("E:\\pythonstduy\\py_game_l\\pipe2.png")    ##加载上管道图片
        self.pipeDown = pygame.image.load("E:\\pythonstduy\\py_game_l\\pipe1.png")  ##加载下管道图片

    def PipelineUpdate(self):
        ##水平移动
        self.wallx -= 5                                 ##管道轴坐标递减，即管道向左移动
        ##当管道运行到一定位置，即小鸟飞越管道，分数加一，并且重置管道
        if self.wallx <-80:
            global score
            score += 1
            self.wallx = 400

def createMap():
    ##定义创建地图的方法
    screen.fill((255,255,255))                          ##填充颜色
    screen.blit(background,(0,0))                       ##填入到背景

    ##显示管道
    screen.blit(Pipeline.pineUP,(Pipeline.wallx,-300))  ##上管道坐标位置
    screen.blit(Pipeline.pipeDown,(Pipeline.wallx,500)) ##下管道坐标位置
    Pipeline.PipelineUpdate()                           ##管道移动

    ##显示小鸟
    if Bird.dead:
        Bird.status = 2                                 ##撞管道状态
    elif Bird.jump:         
        Bird.status = 1                                 ##起飞状态
    screen.blit(Bird.birdStatus[Bird.status],(Bird.birdX,Bird.birdY))           ##设置小鸟的坐标
    Bird.birdUpdate()                                   ##鸟移动
    
    ##显示分数
    screen.blit(font.render(str(score),-1,(255,255,255)),(200,50))              ##设置颜色及坐标位置

    pygame.display.update()                             ##更新显示

##碰撞检测
def checkDead():
    ##上方管子的矩形位置
    upRect = pygame.Rect(Pipeline.wallx,-300,Pipeline.pineUP.get_width()-10,Pipeline.pineUP.get_height())
    ##下方管子的矩形位置
    downRect = pygame.Rect(Pipeline.wallx,500,Pipeline.pipeDown.get_width()-10,Pipeline.pipeDown.get_height())
    ##检测小鸟与上下方管子是否碰撞
    if upRect.colliderect(Bird.birdRect) or downRect.colliderect(Bird.birdRect): ##colliderect（）测试两个矩形的角度是否重叠,
        Bird.dead = True 
    ##检测小鸟是否飞出上下边界
    if not 0 <Bird.birdRect[1]<height:
        Bird.dead = True
        return True
    else:
        return False

##显示结果
def getResult():
    final_Text1 = "Game Over!!! "
    final_Text2 = "Your Score is :"+str(score)
    final_font1 = pygame.font.SysFont("Arial",70)         ##第一行文字字体
    final_surf1 = font.render(final_Text1, 1,(242,3,36))  ##第一行文字颜色
    final_font2 = pygame.font.SysFont("Arial",50)         ##第二行文字字体
    final_surf2 = font.render(final_Text2, 1,(253,177,6)) ##第二行文字颜色
    ##设置第一行文字显示位置
    screen.blit(final_surf1,[screen.get_width()/2-final_surf1.get_width()/2,300])
    ##设置第二行文字显示位置
    screen.blit(final_surf2,[screen.get_width()/2-final_surf2.get_width()/2,200])
    
    ##更新整个待显示的Surface对象到屏幕上
    pygame.display.flip()


if __name__ == "__main__":
    ##主程序
    pygame.init()                                       ##初始化pygame
    pygame.font.init()                                  ##初始化字体
    font = pygame.font.SysFont(None,50)                 ##设置默认字体和大小
    size = width, height = 400,680                      ##设置窗口
    screen = pygame.display.set_mode(size)              ##显示窗口
    clock = pygame.time.Clock()                         ##设置时钟
    Pipeline = Pipeline()                               ##实例化管道类
    Bird = Bird()                                       ##实例化小鸟类
    score = 0                                           ##实例化分数
    while True:
        clock.tick(60)                                  ##每秒执行60次
        ##轮询事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:               ###pygame.QUI 表示检测到关闭pygame窗口事件，如果单击关闭窗口，则退出
                sys.exit()
            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not Bird.dead:
                Bird.jump = True                        ##跳跃
                Bird.gravity = 5                        ##重力
                Bird.jumpSpeed = 10                     ##跳跃速度
  
        
        background = pygame.image.load("E:\\pythonstduy\\py_game_l\\sky.png")       ##加载背景图片
        if checkDead():                                 ##判断小鸟状态
            getResult()
        else: 
            createMap()                                 ##绘制地图

pygame.quit()                                                                       ##退出