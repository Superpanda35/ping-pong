##import pygame
##from pygame.locals import*
##import random
##pygame.init()
##screen=pygame.display.set_mode((800,600))
##pygame.display.set_caption("title")
##x,y=50,50
##xchange=0
##ychange=0
##while 1:
##    screen.fill((0,0,0))
##    pygame.draw.circle(screen,(0,0,255),(x,y),50)
##    x=x+xchange
##    y=y+ychange
##    
##    if  x>=750 :
##       xchange=-random.randint(1,5)
##       ychange=-random.randint(1,5)
##    if  x<=50 :
##        xchange=random.randint(1,5)
##        ychange=random.randint(1,5)
##    if y<=50:
##        xchange=random.randint(1,5)
##        ychange=random.randint(1,5)
##    if y>=550:
##        xchange=-random.randint(1,5)
##        ychange=-random.randint(1,5)
##    pygame.display.update()



##import pygame
##from pygame.locals import*
##import random
##pygame.init()
##screen=pygame.display.set_mode((800,600))
##pygame.display.set_caption("title")
##x,y=50,50
##xchange=random.randint(1,5)
##ychange=random.randint(1,5)
##while 1:
##    screen.fill((0,0,0))
##    pygame.draw.circle(screen,(0,0,255),(x,y),50)
##    x=x+xchange
##    y=y+ychange
##    if  x>=750 or x<=50 :
##       xchange=-xchange
##    if y<=50 or y>=550:
##        ychange=-ychange
##    pygame.display.update()


## drawing a rain drop animation
##import pygame
##from pygame.locals import*
##import random
##pygame.init()
##screen=pygame.display.set_mode((800,600))
##pygame.display.set_caption("title")
##a_list=[]
##red=(255,0,0)
##blue=(0,0,255)
##green=(0,255,0)
##white=(255,255,255)
##yellow=(255,255,0)
##aqua=(0,255,255)
##magenta=(255,0,255)
##sliver=(192,192,192)
##teal=(0,128,128)
##purple=(128,0,128)
##gray=(128,128,128)
##colors=[blue,red,green,white,aqua,magenta,sliver,purple,teal,gray]
##for x in range(0,50,1):
##    x=random.randint(0,800)
##    y=random.randint(0,600)
##    a_list.append([x,y])
##
##fpsclock=pygame.time.Clock()
##color=random.choice(colors)
##while 1:
##    screen.fill((0,0,0))
##    for i in range(0,50,1):
##        pygame.draw.circle(screen,color,a_list[i],3)
##        a_list[i][1]+=1
##        if  a_list[i][1]>=600:
##            a_list[i][1]=0
##            a_list[i][0]=random.randint(0,800)
##        color=random.choice(colors)
##    pygame.display.update()
##    fpsclock.tick(100000)


##import pygame
##from pygame.locals import*
##import random
##pygame.init()
##screen=pygame.display.set_mode((500,500))
##a=[]
##for x in range(0,5,1):
##    q=random.randint(50,450)
##    p=random.randint(50,450)
##    s1=pygame.Surface((q,p))
##    a.append(s1)
##for i in range(0,5,1):
##    pygame.draw.circle(a[i],(255,0,0),(50,50),50)
##    screen.blit(a[i],(random.randint(0,500),random.randint(0,500)))
##    pygame.display.updatwe()
##    




import pygame
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((1200,600))
pygame.display.set_caption("pong")
s1=pygame.Surface((1200,600))
pygame.draw.circle(s1,(255,255,255),(50,50),25)
screen.blit(s1,(575,275))
x1,y1=0,275
x2,y2=1175,275
y1change=0
y2change=0
while True:
    print(y1,y2) 
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,0,0),(x1,y1,25,100))
    pygame.draw.rect(screen,(0,0,255),(x2,y2,25,100))
    y1=y1+y1change
    y2=y2+y2change
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
           
        elif event.type==KEYDOWN:
            
            if event.key==K_UP:
                if 0<=y2<=500:
                    y2change=-1
                else:
                    y2change=0
            if event.key==K_DOWN:
                if 500>=y2>=0:
                    y2change=1
                else:
                    y2change=0
            
                

            if event.key==K_w:
                if 0<=y1<=500:
                    y1change=-1
                else:
                    y1change=0
            if event.key==K_s:
                if 500>=y1>=0:
                    y1change=1
                else:
                    y1change=0

        elif event.type==KEYUP:
            if event.key==K_UP or event.key==K_w or event.key==K_DOWN or event.key==K_s:
                if 500>=y1>=0 and 500>=y2>=0:
                    y2change=0
                    y1change=0
        
    pygame.display.update()

    



