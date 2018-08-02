h = 1
while h < 10:
    l = 1
    while l <= h:
        print('%d*%d=%d' % (l,h,l*h),end='\t')
        l+=1
    print('\n')
    h+=1
     
