# 打开文件
file = open('/home/zwz/Desktop/b.py','r')
# 操作文件，一次读一行
num = 0 
while True:
    test = file.readline()
    if len(test) == 0:
        break
    print('当前第{}行，内容是{}'.format(num,test))
    num+=1
# 关闭文件
file.close

