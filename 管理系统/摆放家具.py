class HouseItem:
    def __init__(self,new_name,new_area):
        self.name = new_name
        self.area = new_area
    def __str__(self):
        return '{}占地面积为:{}'.format(self.name,self.area)
bed = HouseItem('席梦思',4)
chest = HouseItem('衣柜',2)
table = HouseItem('餐桌',1.5)
class House:
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []
    def __str__(self):
        return ("户型：{}\n总面积：{:.2f}[剩余：{:.2f}]\n家具：{}".format(self.house_type, self.area,self.free_area, self.item_list))
    def add_item(self,item):
        print('要添加{}'.format(item))
        if item.area > self.free_area:
            print("%s 的面积太大，不能添加到房子中" % item.name)
            return
        self.item_list.append(item.name)
        self.free_area -= item.area
my_home = House("两室一厅", 60)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)
