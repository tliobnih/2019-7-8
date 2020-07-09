
a=input('請輸入一個清單:')
a= a.split(',')
a1=a[0].split('[')
a2=a[3].split(']')
l=[a1[1],a[1],a[2],a2[0]]
for i in range(4):
    if complex(l[i]).imag==0:
        if float.is_integer(float(l[i])) == True:
            l[i]=int(l[i])
        elif float.is_integer(float(l[i])) == False:
            l[i]=float(l[i])
    elif float.is_integer(float(complex(l[i]).real)) == True:
        l[i]=complex(l[i])
        
    
    
    
print(l)
