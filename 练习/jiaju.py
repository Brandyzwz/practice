class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return '添加家具{}，占地面积为{}'.format(self.name,self.area)

class House:
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
    def __str__(self):
        return
    def add_item(self,item):
        print('要添加{}'.format(item)) 
            if item.area >= self.free_area:
                print('对不起你的家具{}占地太大，无法添加'.format(item.name))
            else:
		self.free_area -= item.area

bed = HouseItem('席梦思',4)
chest = HouseItem('衣柜',2)
table = HouseItem('餐桌',1.5)
print(bed)
print(chest)
print(table)
