a = input('请输入一串字符：')
list1=[]
list2=[]
for i,v in enumerate(a):
    if i%2 == 0:
        list1.append(v)
    elif i%2 !=0:
        list2.append(v)
print(''.join(list1)+''.join(list2))
