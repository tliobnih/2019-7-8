step = 0
high = int(input('請輸入河內塔的塔塊高度：'))
A = []
B = []
C = []
for i in range(0,high):
    A.append(high-i)

def hanoi(n,a,b,c):
    global step
    if n == 1:
        step += 1
        if a == "A" and c == "C":
            print("將塔塊",A[-1],end="")
            C.append(A[-1])
            A.pop()
        elif a == "A" and c == "B":
            print("將塔塊",A[-1],end="")
            B.append(A[-1])
            A.pop()
        elif a == "B" and c == "C":
            print("將塔塊",B[-1],end="")
            C.append(B[-1])
            B.pop()
        elif a == "B" and c == "A":
            print("將塔塊",B[-1],end="")
            A.append(B[-1])
            B.pop()
        elif a == "C" and c == "A":
            print("將塔塊",C[-1],end="")
            A.append(C[-1])
            C.pop()
        else:
            print("將塔塊",C[-1],end="")
            B.append(C[-1])
            C.pop()
        
        print("從",a,"移到",c)
    else:
        hanoi(n-1,a,c,b)
        hanoi(1,a,b,c)
        hanoi(n-1,b,a,c)
        

hanoi(high,"A","B","C")
print("塔塊最少需要的移動步數為",step)
