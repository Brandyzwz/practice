class Animal():
    def run(self):
        print('跑')
class Dog(Animal):
    def run (self):
        print('狗会跑')
class Cat(Animal):
    def run (self):
        print('猫会跑')
dog = Dog()
dog.run()
cat = Cat()
cat.run()
