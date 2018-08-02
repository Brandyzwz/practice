file_read = open('/home/zwz/Desktop/b.py','r')
file_write = open('/home/zwz/Desktop/b3.py','w')
num = 0
while True:
    text = file_read.readline()
    if len(text) == 0:
        break
    file_write.write(text)
    print('当前复制第{}次，内容是{}'.format(num,text))
    num+=1
file_read.close()
file_write.close()
