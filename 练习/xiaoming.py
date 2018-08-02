class Person:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    def run(self):
        self.weight -= 0.5
        print('{}的体重为{}'.format(self.name,self.weight)) 
    def eat(self):
        self.weight += 1
        print('{}的体重为{}'.format(self.name,self.weight)) 
    def __str__(self):
        return '继续加油吧'
xiaoming = Person('小明',75)
xiaoming.run()
xiaoming.run()
xiaoming.eat()
print(xiaoming)
xiaomei = Person('小妹',45)
xiaomei.run()
xiaomei.eat()
print(xiaomei)
