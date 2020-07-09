import random

guess_small = 0
guess_big = 9

a = random.randint(guess_small,guess_big)

b = random.randint(guess_small,guess_big)
while a==b:
    b = random.randint(guess_small,guess_big)

c = random.randint(guess_small,guess_big)
while c==b or c==a :
    c = random.randint(guess_small,guess_big)

d = random.randint(guess_small,guess_big)
while d==b or d==a or d==c:
    d = random.randint(guess_small,guess_big)
answer=(0,1,4,7)# 此為亂數組成的不重複數字

A=0
ouTime =0
while( A != 4 ):
    a1=int(input('請輸入第1數字：'))
    b1=int(input('請輸入第2數字：'))
    c1=int(input('請輸入第3數字：'))
    d1=int(input('請輸入第4數字：'))
    number=(a1,b1,c1,d1)# 輸入猜測值
    
    if a1==b1 or a1==c1 or a1==d1 or b1==c1 or b1==d1 or c1==d1:
        print('數字不能重複，請重新輸入')
        continue
    
    if a1>9 or b1>9 or c1>9 or d1>9:
        print('數字由0-9組成，請重新輸入')
        continue

    A=0 # A歸零
    B=0 # B歸零
    checkTime=0
    while checkTime < 4:
        runTime=0
        while runTime < 4:
            if checkTime == runTime and number[checkTime]==answer[runTime]:
                A+=1
            elif number[checkTime]==answer[runTime]:
                B+=1
            runTime += 1
        checkTime += 1
    print('{}A{}B'.format(A,B))# 檢查是否猜對
    if A==4:
        print('你答對了')
        
    ouTime += 1
    if ouTime ==5:
        print('猜測次數達上限')# 最多只能猜五次
        break
