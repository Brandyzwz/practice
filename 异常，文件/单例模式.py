class In():
    a = None
    def __new__(cls):
        if cls.a is None:
            cls.a = super().__new__(cls)
        return cls.a
    def __init__(self):
        print('')
s1 = In()
s1.name = '小白'
s2 = In()
s2.name = '小黄'
print(s1.name)
