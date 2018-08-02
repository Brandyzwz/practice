for l in [1,2,3,4,5,6,7,8,9]:
    for h in [1,2,3,4,5,6,7,8,9]:
        if l >= h:
            print('%d*%d=%d'% (h,l,h*l),end='\t')
    print('\n') 
