def multiple_table():
    h = 1
    while h<=9:
        l=1
        while l<=h:
            print('%d*%d=%d'%(l,h,l*h),end='\t')
            l+=1
        print('\n')
        h+=1
for i in range(1,101):
    multiple_table()
    print('这是第%d次打印'%i)
