a=int(input('輸入第一個數:'))
b=int(input('輸入第二個數:'))
t=a%b
print(a,'=',a//b,'*',b,'+',t)

while t!=0:
    t=a%b
    a=b
    
    if t!=0:
        b=t
        print(a,'=',a//b,'*',b,'+',a%b)
    else:
        print('最大公因數是',b)
        

    
    
