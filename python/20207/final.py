import pygame
from pygame.locals import *
from collections import namedtuple

pygame.init()

#設定螢幕大小
screen = pygame.display.set_mode((500, 400), 0, 32)

#載入需要圖片
laugh= pygame.image.load("s.jpg").convert()
humer=pygame.image.load("st.png").convert_alpha()

# 創建一個命名元組以跟踪桿及圓盤的大小/位置
Rod = namedtuple('Rod', ['rect', 'items'])

# 有三個桿，後面list中每個數字代表一個圓盤
rods = (Rod(pygame.Rect((100, 150, 25, 250)), [ 3, 2, 1]),
        Rod(pygame.Rect((225, 150, 25, 250)), []),
        Rod(pygame.Rect((350, 150, 25, 250)), []))

# 跟蹤當前選擇的桿
selected = None

#總共有10個關卡
level=[13,12,11,10,9,8,7,6,5,4,3]

#第1關的最小步數
step=7
minstep=7

#每關你走的步數
move=0

while True:
    
    #點擊關閉視窗
    if pygame.event.get(QUIT):
        break
    screen.fill((200, 200, 255))
    #字型
    font = pygame.font.SysFont("arial", 16)
    blod_font = pygame.font.Font(None, 30)
    #提示文字
    end=font.render('Put all here',True,(0,0,255),(255,220, 255))
    screen.blit(end, (330,120))
    start=font.render('START',True,(0,0,255),(255, 220, 255))
    screen.blit(start, (92,120))
    ideal=font.render('the least steps:',True,(100,0,200),(200,200, 255))
    screen.blit(ideal, (350,0))
    real=font.render('your steps:',True,(200,0,200),(200,200, 255))
    screen.blit(real, (374,20))
    haha=font.render('haha',True,(200,0,200),(200,200, 255))

    #該關卡的最少步數、你走的步數
    num1 = blod_font.render(str(minstep), 1, (100, 0, 200))
    screen.blit(num1, (450,0))
    num2 = blod_font.render(str(move), 1, (200, 0, 200),(200,220, 245))
    screen.blit(num2, (450,20))

    #超過最少步數會被嘲笑
    if move>=minstep:
        screen.blit(laugh, (0,0))
        screen.blit(haha, (220,0))
    #每完成一關卡之後，提示還有下一關
    if len(rods[0].items)+len(rods[1].items)+len(rods[2].items)>3 and move==0:
        screen.blit(humer, (0,0))

    # 畫桿。每個桿都有一個rect，我們可以與pygame.draw.rect一起使用
    for rod in rods:

        # 如果選擇了桿，我們將其繪製為亮藍綠色而不是深藍色
        pygame.draw.rect(screen, pygame.Color('aquamarine' if selected == rod else 'mediumblue'), rod.rect)    
        # 畫每個桿的每個圓盤
        for i, item in enumerate(rod.items):            
            r = pygame.Rect(rod.rect.x - item * 8, 375 - 25 * i, 25 + item * 16, 25)
            # 如果選擇了桿，我們將該桿的圓盤繪製為亮藍色而不是藍色
            pygame.draw.rect(screen, pygame.Color('cyan' if selected == rod else 'royalblue'), r)
            

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 檢查我們是否點擊了桿。rect.collidepoint：測試點是否在矩形內//pygame.mouse.get_pos()：點擊的座標
            rod = next((r for r in rods if r.rect.collidepoint(pygame.mouse.get_pos())), None)
            
            if rod:
                if selected:# 如果之前已經選擇了一根桿
                    if selected.items:
                        if rod.items:
                            if pygame.event.get(QUIT):#點擊關閉視窗
                                break
                            if int(min(rod.items))>int(min(selected.items)):#確認圓盤移動到比自己小的圓盤上
                                rod.items.append(selected.items.pop())
                                move+=1
                                selected = None
                                for i in level:#每完成1關卡，則再加1個圓盤
                                    if len(rod.items)==i and rod==rods[2]:
                                        rods[0].items.append(i+1)
                                        step=2**(int(max(rods[0].items))-1)-1
                                        minstep=step*2+1#新關卡的最少步數
                                        
                                        move=0#新關卡步數重算
                                        level.pop()
                                        
                            else:#大圓盤不能放到小圓盤上
                                selected = None
                        else:
                            rod.items.append(selected.items.pop())
                            move+=1                            
                            selected = None
                    else:
                        selected = None

                else:
                    # 如果沒有選擇桿，則選擇當前單擊的桿（如果有圓盤）
                    selected = rod
            else:
                selected = None
    


                
    pygame.display.update()
pygame.quit()

#附上參考程式碼
#https://www.pythonheidong.com/blog/article/351722/
