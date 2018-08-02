file_read = open('b.py','r')
file_wirte = open('b5.py','w')
while True:
    a = file_read.read()
    if not a:
        break
    file_wirte.write(a)
file_read.close()
file_wirte.close()