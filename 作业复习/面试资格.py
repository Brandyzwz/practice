age = int(input('请输入年龄'))
subject = input('请输入专业名称')
college = input('请输入重点或者非重点')
if (age > 25 and subject == '电子信息工程')or (college == '重点' and subject == '电子信息工程')or(age <= 28 and subject == '计算机'):
    print('恭喜,您已经获取我们公司的面试机会!')
else:
    print('抱歉,您未达到面试要求')

