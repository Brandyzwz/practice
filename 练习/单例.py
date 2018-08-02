class Dog():
    a = None
    def __new__(cls):
        if cls.a is None:
            cls.a = super().__new__(cls)
        return cls.a
    def __init__(self):
        print('哈哈')
d1 = Dog()
d1.name = '张三'
print('d1{}'.format(id(d1)))
d2 = Dog()
d2.name = '李四'
print('d2{}'.format(id(d2)))
print(d1.name)
