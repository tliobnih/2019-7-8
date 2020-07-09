#multi = lambda n,x,y:

#lst=[]
#def multi(n,x,y):
#    if n == x:
#        lst.append(n)
#        return lst
#    else:
#        if n % x == 0 and n % y != 0:
#            lst.append(n)
#        return multi(n-1,x,y)


multi=lambda n,x,y,lst: lst if n == x else multi(n-1,x,y) if n % x == 0 and n % y != 0 else multi(n-1,x,y)

print(multi(20,2,3,[]))
#s = for i in range(1,6)(lambda i:"" if x == 1 else "s")
#print(s)
