i = 0
while i<100:
    if i >=20:
        break
    elif i == 3:
        i +=1
        continue
    else:
        print('这是第%d' % i)
    i+=1
print('这是第%d' % i)
print('')
