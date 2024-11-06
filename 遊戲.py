import pygame
import sys
from pygame.locals import *


hig = 700
wit = 600
blk = (0,0,0)


class wellleft(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,600])
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
class wellDown(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([wit-80,10])
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]


class Rect1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = [(wit/2),50]
    def turn(self):
       
        self.image = pygame.transform.rotate(self.image,90)
        #self.image = pygame.Surface([x+xyx[i],y+xyy[i]])
        #self.image.fill((255,255,0))
       
       
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]==True:
            if self.rect.x>=526 or self.rect.x<=43:
                self.rect.x+=5
            self.rect.x-=5
        if key[pygame.K_RIGHT]==True:
            if self.rect.x>=526 or self.rect.x<=43:
                self.rect.x-=5
            self.rect.x+=5
    def down(self):
        if self.rect.y==600:
            self.rect.y-=5
        self.rect.y+=5
    #問題點!!!如何偵測(解決)
    def gg(self,cc,x,y):
        #for i in range(len(cc)):
        X = 600//x
        Y = y/20
        for j in range(len(cc[0])):
            hj = 600
            lk = 0
            for i in range(40,600,60):
                if abs(x-i)<hj:
                    hj = abs(x-i)
                    lk = i
                    #if Y-j<5:
            if abs(x-lk)<50:
               
                #print(abs(x-lk))
                ha = lk//60
                #print(ha)
                cc[0][ha]=1
        return cc
   
    def ch(self,g):
        f = [0]*10
        #for i in range(len(g)):
        for j in range(len(g[0])):
            if g[0][j]==1:
                f[j]=1
                return f
        return f
    def killl(self):
        #30,26
        s = 0
        chc=[0]*10
        cc = [[0]*(10) for i in range(26)]
        if self.rect.y==(600):  
            cg = self.gg(cc,self.rect.x,self.rect.y)
            chc = self.ch(cg)
        for i in range(10):
            if chc[i]==1:
                s = i
                return s  
        return s
    def downone(self,alls):
        vk = 0
        X = self.rect.x
        for i in alls:
            if X==i.rect.x:
                vk+=1
        return vk
    def downalls(self,alls):
        sss = 1
        if self.rect.y==600:
            return sss
        for i in alls:
            if i.rect.x==self.rect.x:
                sss = 0
                return sss
        return sss






           










       


       










#def qqq(sec):
ggh = pygame.sprite.Group()
bb = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
wellft = wellleft(30,30)
wellht = wellleft(wit-50,30)
wellwn = wellDown(40,620)
rect1 = Rect1()
rects = pygame.sprite.Group()


#rects.add(Rect1())












def main():
    global g
    g= Rect1()
    rects.add(g)
    pygame.init()
    pygame.display.set_caption("俄羅斯方塊")
    sec = pygame.display.set_mode((wit,hig))
    clock = pygame.time.Clock()
    bg = pygame.surface.Surface([800,600])
   
   
    j = 0
    x = 20
    y = 40
    #s = Rect1()
    vv = 0
    e = 0
    vb = [[0]*10 for i in range(26)]
    while True:
       
        b = 0
       


        if vv==1:
            for j in range(1):
                g= Rect1()
                rects.add(g)

            #all_sprites.add(rect1)
            #rects.add(Rect1())
            vv=0
       
        if vv==0:
            
            for i in all_sprites:
                if i.rect.y==600:
                    ggh.add(i)

            for i in rects:
                #all_sprites.add(i)
                bh = i.downone(ggh)
                if i.rect.y==(600-(20*bh)):
                   
                    #rects.remove(rect1)
                    for j in range(1):
                        all_sprites.add(g)
                        e+=1
                        rects.remove(g)
                       
                    vv = 1
                
                i.down()
                i.move()
                
                #print(vb)
                
                #i.rect.y = 600
                for d in all_sprites:
                    #dff = i.downone(ggh)
                    q = d.killl()
                   
                    if q>-1:
                        print(q)
                        vb[0][q]=1
                hk = False
                we=0
                for l in vb[0]:
                    if l==1:
                        we+=1
                if we==9:
                    hk=True
                
                if hk==True:
                    for l in ggh:
                        
                        l.kill()
                    vb = [[0]*10 for i in range(26)]
                    hk=False

                break
            QQ = [1]*100
            for i in bb:
                bb.remove(i)

            for i in all_sprites:
                if i.rect.y!=600:
                    bb.add(i)
        
                    
            
            gee=0
            for i in bb:
                hc = i.downalls(ggh)
                QQ[gee]=hc
            gees= 0
                
                
            for i in bb:
                if QQ[gees]==1:
                    pass
                else:
                    i.rect.y+=20
                ggh.add(i)
                bb.remove(i)
                
                gees+=1

                
            
            








               
            #if b>vv:
                   
                #i.rect.topleft = [(wit/2),50]
                #vv+=1
                #break
            #else:
                #continue
       
           
        clock.tick(60)
       
       
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()


            #if event.type==pygame.KEYDOWN:
                #if event.key==pygame.K_a:
                    #rect1.turn()
        sec.fill(blk)
        sec.blit(wellft.image,wellft.rect)
        sec.blit(wellht.image,wellht.rect)
        sec.blit(wellwn.image,wellwn.rect)
        #sec.blit(.image,s.rect)
       
       
        rects.draw(sec)
        rects.update()
        all_sprites.draw(sec)
        #bb.draw(sec)
        ggh.draw(sec)
       
        pygame.display.update()




if __name__=="__main__":

    main()