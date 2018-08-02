class Gun:
    def __init__(self, new_model):
        # 枪的型号
        self.model = new_model
        # 子弹数量
        self.bullet_count = 0
    def add_bullet(self, count):  # 装子弹
        self.bullet_count += count
    def shoot(self): # 射击
        # 判断是否还有子弹
        if self.bullet_count <= 0:
            print("没有子弹了...")
        else:  
            # 发射一颗子弹
            self.bullet_count -= 1
            print("子弹发射了，还剩余{}".format (self.bullet_count))

class Soldier:
    def __init__(self,new_name):
        self.name = new_name
        self.gun = None
    def fire(self):
        if self.gun is None:
            print('{}没有枪'.format(self.name))
        else:
            # self.gun是一个对象（枪）
            # 枪是枪类创建出来的
            # 对象.属性名
            if self.gun.bullet_count <= 0:
                print('没有子弹')
            else:
                print('冲啊')
                self.gun.shoot()
ak47 = Gun("ak47")
laowang = Soldier('laowang')
laowang.gun = ak47
ak47.bullet_count=50
laowang.fire()
laowang.fire()
