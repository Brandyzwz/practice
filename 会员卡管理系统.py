card_infos = []

def print_menu():
    """打印显示功能"""
    print('=' * 50)
    print('超市会员卡管理系统 V1.0')
    print('1. 添加会员信息')
    print('2. 删除会员信息')
    print('3. 修改会员信息')
    print('4. 显示所有会员的信息')
    print('5. 保存会员的信息')
    print('6. 系统帮助')
    print('7. 查询会员')
    print('8. 会员抽奖')
    print('9. 限时打折')
    print('10.查询会员等级')
    print('0. 退出系统')
    print('=' * 50)

def W1(func):
     def W1_in():
         print('成功进入')
         func()
     return W1_in

def is_super(func):
    def inner(card_n):
        if 8 > len(card_n) >= 6:
            print('白金VIP')
        elif len(card_n) >=8:
            print('普通用户')
        else:
            print('钻石VIP')
        func(card_n)
    return inner

@is_super
def shu_ru(card_n):
    print('卡号{}'.format(card_n))

@W1
def add_info():
    """添加一个会员信息"""
    new_name = input('请输入会员的名字:')
    new_sex = input('请输入会员的性别:(男/女):')
    new_phone = input('请输入会员的手机号:')
    if len(new_phone) != 11:
        ex = Exception('输入手机号不正确,重新输入！')
        raise ex
    new_card_number = input('请输入会员卡号：')

    # 把会员的信息 放在一个字典里面
    new_infos = {}
    new_infos['name'] = new_name
    new_infos['sex'] = new_sex
    new_infos['phone'] = new_phone
    new_infos['card'] = new_card_number
    # 3. 把会员的字典 放在 全局的列表
    card_infos.append(new_infos)

# 删除会员的信息

def del_info(card_infos):
    """删除会员的信息"""
    del_number = int(input('请输入要删除会员的序列号'))
    quit_confirm = input('确认删除?(Yes/No):')
    if quit_confirm == 'Yes' or quit_confirm == 'yes' or quit_confirm == 'y':
        del card_infos[del_number - 1]
    else:
        print('输入有误,请重写输入')

# 修改会员的信息
@W1
def modify_info():
    # 得到要求改的会员
    card_id = int(input('请输入要修改的会员的序号:'))
    # 以下3个变量  是用户输入的
    new_name = input('请输入修改后会员的名字:')
    new_sex = input('请输入修改后会员的性别(男/女):')
    new_phone = input('请输入修改后会员的手机号:')
    # 去全局的列表里面去找
    card_infos[card_id - 1]['name'] = new_name
    card_infos[card_id - 1]['sex'] = new_sex
    card_infos[card_id - 1]['phone'] = new_phone

@W1
def show_infos():
    """展示所有会员的信息"""
    print('=' * 50)
    print('会员信息如下:')
    print('-' * 50)
    print('序号 姓名   性别   手机号      会员卡号')
    i = 1
    # 遍历列表
    # 每一次遍历出来 就是一个会员的信息
    for card_dict in card_infos:
        print('%d\t%s\t%s\t%s\t%s' % (i, card_dict['name'], card_dict['sex'], card_dict['phone'],card_dict['card']))
        i += 1
    print('=' * 50)

@W1
def save_to_file():
    """保存会员的信息到文件中"""
    file = open('card.data', 'w')
    file.write(str(card_infos))
    file.close()

# 存在本地的信息
@W1
def recover_data():
    global card_infos
    try:
        # 1. 打开文件
        file = open('card.data', 'r')
        # 2. 读取文件
        content = file.read()
        card_infos = eval(content)
        # 3. 关闭
        file.close()
    except:
        print('没有历史数据')
@W1
def help_you():
    print(
          '请按照步骤操作会员卡管理系统,'
          '1. 添加会员信息'
          '2. 删除会员信息'
          '3. 修改会员信息'
          '4. 显示所有会员的信息'
          '5. 保存会员的信息'
          '6. 系统帮助'
          '7. 查询会员'
          '8. 会员抽奖'
          '9. 限时打折'
          '0. 退出系统'
          )


def search():
    a = input('请输入手机号进行查询:')
    for i in  card_infos:
        if a == i['phone']:
            print('已搜索到您的会员信息：{}'.format(i))
            break
        else:
            print('不好意思，您还未办理会员')

@W1
def lucky():
    import random
    i = 0
    while True:
            computer = random.randint(1, 4)
            user = int(input('剪刀石头布小游戏！如果三次内您赢了就可以获得奖品哟！请输入1.石头 2.剪子 3.布：'))
            i+=1
            if (computer == 1 and user == 3) or (computer == 2 and user == 1) or (computer == 3 and user == 2):
                print('恭喜您赢了')
                break
            elif computer == user:
                print('平局')
            else:
                print('再接再厉')
    print('一共猜了{}次'.format(i))
    if i<=3:
        print('三把之内赢了我！恭喜你获得奖品')
    else:
        print('下次再来吧！')

@W1
def sale():
    b = float(input('限时打折，输入您本次购买金额：'))
    if 300 < b <= 500:
        print('本次为您打9折，打折后价格为：{}'.format(int(b*0.9)))
    elif 500 < b <= 1000:
        print('本次为您打8折，打折后价格为：{}'.format(int(b*0.8)))
    elif b > 1000:
        print('本次为您打7折，打折后价格为：{}'.format(int(b*0.7)))
    else:
        print('不好意思，您的金额没有达到本次限时打折标准')

# main  主程序调用其他函数
def main():
    # 1. 先恢复数
    recover_data()
    while True:
        print_menu()
        # 用户去输入一个数字--->判断他要实使用什么功能
        key = int(input('请输入对应功能:'))
        if key == 1:
            # 添加会员信息
            add_info()
        elif key == 2:
            # 删除会员信息
            del_info(card_infos)
        elif key == 3:
            # 修改
            modify_info()
        elif key == 4:
            # 查看所有
            show_infos()
        elif key == 5:
            #保存信息
            save_to_file()
        elif key == 6:
            #帮助信息
            help_you()
        elif key == 7:
            #查找
            search()
        elif key == 8:
            #抽奖
            lucky()
        elif key == 9:
            #活动
            sale()
        elif key == 10:
            #查询等级
            shu_ru(input('输入您的卡号，查询等级：'))
        elif key == 0:
            #退出系统
            quit_confirm = input('确认退出?(Yes/No):')

            if quit_confirm == 'Yes' or quit_confirm =='yes' or quit_confirm == 'y':
                break
            else:
                print('输入有误,请重写输入')

try:
    main()
except ValueError:
    print('请输入正确的数字')
    main()
except Exception as result:
    print(result)
    add_info()