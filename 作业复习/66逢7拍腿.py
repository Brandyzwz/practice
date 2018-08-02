i = 0 
for num in range(1,100):
    if num%7 == 0 or num%10 == 7:
        i+=1
    else:
        continue
print('共拍腿：{}'.format(i))
