class Dog():
    a = None
    def __new__(cls):
        if cls.a is None:
            cls.a = super().__new__(cls)
        return cls.a
    def __init__(self):
        print('哈哈哈')
d1 = Dog()
d1.name = '张三'
d2 = Dog()
d2.name = '李四'
print(d1.name)