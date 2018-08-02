student_infos = []


def print_menu():
    """打印显示功能"""
    print('='*50)
    print('学生管理系统 V1.0')
    print('1. 添加学生信息')
    print('2. 删除学生信息')
    print('3. 修改学生信息')
    print('4. 显示所有学生的信息')
    print('5. 保存学生的信息')  # 保存到本地
    print('0. 退出系统')
    print('='*50)


# 添加学生信息
def add_info():
    """添加一个学生信息"""
    # 1. 你必须要知道学生有哪些信息(并且获取学生的信息)
    new_name = input('请输入新学生的名字:')
    new_sex = input('请输入新学生的性别:(男/女):')
    new_phone = input('请输入新学生的手机号:')
    # 2. 把学生的信息 放在一个字典里面
    new_infos = {}
    new_infos['name'] = new_name
    new_infos['sex'] = new_sex
    new_infos['phone'] = new_phone

    # 3. 把学生的字典 放在 全局的列表(他是记录我们所有学生信息的)
    student_infos.append(new_infos)


# 删除学生的信息
def del_info(student):
    """删除学生的信息"""
    del_number = int(input('请输入要删除的学生的序列号'))
    del student[del_number-1]

# 修改学生的信息


def modify_info():
    # 得到要求改的学生  到底是哪个学生
    student_id = int(input('请输入要修改的学生的序号:'))
    # 你需要 把你要修改的内容你得输入一下
    # 以下3个变量  是用户输入的
    new_name = input('请输入修改后的学生的名字:')
    new_sex = input('请输入修改后的学生的性别(男/女):')
    new_phone = input('请输入修改后的学生的手机号:')
    # 当我们 拿到用户输入的信息后  我们就去找
    #  去所有学生里面找到要修改的哪个学生
    # 去全局的列表里面去找
    student_infos[student_id-1]['name'] = new_name
    student_infos[student_id-1]['sex'] = new_sex
    student_infos[student_id-1]['phone'] = new_phone


# 显示学生的所有信息
def show_infos():
    """展示所有学生的信息"""
    # 展示了一下 横线
    print('='*50)
    # 普通的输出
    print('学生信息如下:')
    # 一条横线
    print('-'*50)
    # excel 表头(其实就是第一行显示的内容)
    print('序号 姓名 性别 手机号')
    # 其实就是序号
    i = 1
    # 遍历列表----> 列表装了所有学生的信息
    # 每一次遍历出来 或者说每一次循环出来的  就是一个学生的信息
    for student_dict in student_infos:
        print('%d%s%s%s' % (i, student_dict['name'], student_dict['sex'], student_dict['phone']))
        i += 1
    print('='*50)

# 保存学生的信息(文件版,保存到本地)


def save_to_file():
    """保存学生的信息到文件中"""
    # 打开文件
    file = open('student.data', 'w')
    # 写入内容
    file.write(str(student_infos))
    # 关闭
    file.close()

# 读取信息---->将来你这个程序 一运行  我先去 读取信息
#  先看一下  有没有  存在本地的信息


def recover_data():
    global student_infos

    try:
        # 1. 打开文件
        file = open('student.data','r')
            # 2. 读取文件
        # content 内容
        content = file.read()
        student_infos = eval(content)
        # 3. 关闭
        file.close()
    except:
        print('没有历史数据')
        


# main  主程序----> 调用其他函数
def main():
    # 1. 先恢复数据
    recover_data()
    while True:
        print_menu()

        # 用户去输入一个数字--->判断他要实使用什么功能
        key = input('请输入对应功能:')

        if key == '1':
            # 添加学生信息
            add_info()
        elif key == '2':
            # 删除学生信息
            del_info(student_infos)
        elif key == '3':
            # 修改
            modify_info()
        elif key == '4':
            # 查看所有
            show_infos()
        elif key == '5':
            save_to_file()
        elif key == '0':  # 退出系统
            quit_confirm = input('亲,你真的要退出吗?(Yes/No):')

            if quit_confirm == 'Yes':
                break
            else:
                print('输入有误,请重写输入')


main()
            
