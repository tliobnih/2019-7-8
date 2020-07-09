for i in range(1,11):
    
    if i==1:
        print('{0:>2}|'.format(' '),end='')
    elif i==2:
        print('{0:-<26}'.format('--+'))
        continue
    else:
        print('{0:0>2}|'.format(i-1),end='')

        
    for j in range(2,10):
        if i==1 :
            if j<9:
                print('{0:0>2} '.format(i*j),end='')
            else:
                print('{0:0>2}'.format(i*j))
            
        else:
            if j<9:
                print('{0:0>2} '.format((i-1)*j),end='')
            else:
                print('{0:0>2}'.format((i-1)*j))


        
