# 打开文件（复制需要同时打开两个文件，一个是被复制的，另一个是需要复制到的）
file_read = open('/home/zwz/Desktop/b.py','r')
file_write = open('/home/zwz/Desktop/b[副本1].py','w')
# 操作文件
read_test = file_read.read()
file_write.write(read_test)
# 关闭（要把两个都关闭）
file_read.close()
file_write.close() 
