class Cat:
    def __init__ (self,new_name):
        self.name = new_name
    def eat(self):
        print('self:%x'%id(tom))
    def __del__(self): #对象销毁之前调用
        print('快桥边自乐')
    def __str__(self):
        return '{}'.format(id(tom))
tom = Cat('打烂猫')
print(tom.name)
print(tom)
del tom # 删除一个对象 是指上再内存中销毁

