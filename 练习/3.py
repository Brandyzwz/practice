h = 1
l = 1
for h in [1,2,3,4,5,6,7,8,9]:
    print('%d*%d=%d'% (l,h,l*h),end='\n')
    l+=1
    for l in [2,3,4,5,6,7,8,9]:     
        print('%d*%d=%d'% (h,l,h*l),end='\n')

