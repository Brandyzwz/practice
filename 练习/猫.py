class Cat:
    def eat(self):
        print('小猫爱吃鱼')
    def drink(self):
        print('小猫爱喝水')
tom = Cat()
tom.eat()
tom.drink()
print('汤姆猫的内存：%x'%id(tom))
print('*'*50)
lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()
print('懒猫的内存：%x'%id(lazy_cat))


