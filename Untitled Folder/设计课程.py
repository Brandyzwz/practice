class Object():
    def __init__(self):
        self.number = 1001
        self.name = '语文'
        self.teacher = '小明'
        self.__position = '教学楼'
    def information(self):
        print('课程编号{}名称{}任课老师{}上课地点{}'.format(self.number,self.name,self.teacher,self.__position))
s = Object()
s.information()
