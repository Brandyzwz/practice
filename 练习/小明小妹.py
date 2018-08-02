class Person:
    def __init__(self,new_weight,new_name):
        self.weight = new_weight
        self.name = new_name
    def run(self):
        self.weight -= 0.5
        print('{}的体重是{}'.format(self.name,self.weight))
    def eat(self):
        self.weight +=1
        print('{}的体重是{}'.format(self.name,self.weight))
    def __str__(self):
        return '哈哈哈'
xiaoming = Person(20,'小明')
xiaoming.run()
xiaoming.run()
xiaoming.eat()
xiaoming.eat()
print(xiaoming)
xiaomei = Person(45,'小妹')
xiaomei.run()
xiaomei.run()
xiaomei.eat()
print(xiaomei)
