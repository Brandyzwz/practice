'''设计一个表示学生(Student)的类,该类属性有名字(name),年龄(age),成绩(scores)(成绩包含语文,数学和英语三科成绩,每科成绩的类型为整数)
另外有3个方法. (1) 获取学生姓名的方法:get_name(),返回类型为String (2) 获取学生年龄的方法:get_age()方法,返回类型为Int
(3) 返回3门科目中最高的分数,get_course(),返回类型为Int
'''
class Student():
    def __init__(self,name,age,scores):
        self.name = name
        self.age = age
        self.scores =scores
    def get_name(self):
        print('学生姓名是：{}'.format(self.name))
    def get_age(self):
        print('学生的年龄是：{}'.format(self.age))
    def get_course(self):
        print('3门科目中最高的：{}'.format(max(self.scores)))
xiaoming = Student('小明','18',[98,87,99])
xiaoming.get_name()
xiaoming.get_age()
xiaoming.get_course()