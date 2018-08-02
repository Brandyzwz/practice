# 全局变量card_list增删改查都可以用
card_list = []
def printLines(num):
    print('*'*num)
def show_menu():
    '''显示菜单'''
    printLines(60)
    print('欢迎使用[名片管理系统]V1.0\n')
    print('1.新建名片\n2.显示全部\n3.查询名片\n0.退出系统')
    printLines(60)
def new_card():
    '''新建名片'''
    printLines(60)
    print("功能：新建名片")
    name=input('请输入姓名：')
    phone=input('请输入手机号：')
    QQ=input('QQ:')
    email=input('email:')
    card_dict={'name':name,'phone':phone,'QQ':QQ,'email':email}
    card_list.append(card_dict)
    print('成功添加一张新名片')
    printLines(60)
def show_all():
    '''显示全部'''
    printLines(60)
    print("功能：显示全部")
    if len(card_list) == 0:
        print('对不起，没有名片')
        return
    print('姓名\t\t电话\t\tQQ\t\t邮箱')
    print('-'*60)
    for card_dict in card_list:
        print('%s\t\t%s\t\t%s\t\t%s'%(card_dict['name'],card_dict['phone'],card_dict['QQ'],card_dict['email']))
def search_card():
    '''搜索名片'''
    printLines(60)
    print("功能：搜索名片")
    find_name=input('请输入要搜索的内容：')
    for card_dict in card_list:
        if find_name == card_dict['name']:
            print('姓名\t\t电话\t\tQQ\t\t邮箱')
            print('-'*60)
            print('%s\t\t%s\t\t%s\t\t%s'%(card_dict['name'],card_dict['phone'],card_dict['QQ'],card_dict['email']))
            deal_card(card_dict)
            break           
        else:
            print('找不到')
def deal_card(card_dict):
    '''查询到名片以后，要做的事情，封装到这个函数里面，实现一句话调用'''
    action = input('请输入您要进行的操作：[1]修改[2]删除\n')
    if action== '1':
        card_dict['name'] = input('请输入要修改的名字：')
        card_dict['phone'] = input('请输入要修改的手机号：')
        card_dict['QQ'] = input('请输入要修改的QQ号:')
        card_dict['email']=input('请输入要修改的邮箱：')
        print('恭喜你，名片更改成功')
    elif action == '2':
        card_list.remove(card_dict)
    else:
        print('输入有误，重新输入')







