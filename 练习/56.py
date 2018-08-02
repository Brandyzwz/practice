list1 = [1,2,3,4,5,6,7,8,9,2,4,5,3,2,2]
for i,v in enumerate(list1):
    len1=len(list1)
    n=(len1-1)/2 
    if i==n:
        print('中间数为:%d'%v)
