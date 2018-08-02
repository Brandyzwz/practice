try:
    score = int(input("请输入学生的成绩："))
    if score>=90 and score<=100:
        print("A:优秀")
    elif score>=80 and score<90:
        print("B:良好")
    elif score>=60 and score<80:
        print("C:合格")
    else:
        assert score>60,"D:不及格"
except Exception as result:
    print("低于60分：\n",result)
