out = 0#非質數的開頭輸出判定	
#print('輸入值：',inPut)
inPut=int(input('請輸入一個數字:'))
cheak=inPut
outime=0
if inPut == 1:
      print('1 不是質數也無須分解')#處理不是質數也不是合數的部分
 
else:
    i=1
    while inPut//i*i <= inPut :
        i+=1
        if inPut//i*i == inPut:#若i為check的因子則等號成立，若非則check/i*i < check
            if i==cheak :
                print(i,"為質數")
                break
            inPut /= i#取正數的高斯計算
            
            while outime==0:
                print(cheak,'不是一個質數')
                print(cheak,'=',end='')
                outime+=1
            if inPut>1:
                print(i,"*",end='')
            else:
                print(i)
              
            i=1
            
        
    
