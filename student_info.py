import os
import student
# os.system('clear')

def input_student():
    info = []
    while True:
        os.system('clear')
        name = input("请输入姓名：")
        if name != '':
            while True:
                try:
                    age = int(input("请输入年龄："))
                except ValueError:
                    input("您输入的年龄不是整数，按任意键继续...")
                    continue
                try:
                    assert 18<= age <= 24, '您输入的年龄不在范围内，学生年龄应在18到24之间'
                except AssertionError as err:
                    print(err, end='')
                    input('，按任意键继续...')
                    continue
                break
            while True:
                try:
                    score = float(input("请输入成绩："))
                except ValueError:
                    input("您输入的成绩不是数字，按任意键继续...")
                    continue
                try:
                    assert 0 <= score <= 150, '您输入的成绩不在范围内，学生成绩应在0到150之间'
                except AssertionError as err:
                    input(err + '，按任意键继续...')
                    continue
                break
            d_temp = student.Student(name, age, score)
            info.append(d_temp)
            if d_temp in info:
                input("添加成功，按任意键继续...")
                os.system('clear')
                continue
            else:
                input("添加失败，按任意键继续...")
                os.system('clear')
                continue
        else:
            input("按任意键返回主界面...")
            break
    return info

def output_student(L):
    print('+' + '-' * 15 + '+' + '-' * 8 + '+' + '-' * 8 + '+')
    print('|' + '姓名'.center(13) + '|' + '年龄'.center(6) + '|' + '成绩'.center(6) + '|')
    print('+' + '-' * 15 + '+' + '-' * 8 + '+' + '-' * 8 + '+')
    for i in L:
        name_center = 15
        age_center = 8
        score_center = 8
        for temp in i.get_name():
            if 0x4E00 <= ord(temp) <= 0x9FA5:
                name_center -= 1
        print('|' + i.get_name().center(name_center) + '|' 
                + str(i.get_age()).center(age_center) 
                + '|' + str(i.get_score()).center(score_center) + '|')
    print('+' + '-' * 15 + '+' + '-' * 8 + '+' + '-' * 8 + '+')

def del_sutdent(L):
    while True:
        os.system('clear')
        name = input("请输入要删除的学生的姓名：")
        if name != '':
            for i in L:
                if i.get_name() == name:
                    if L.pop(L.index(i)):
                        del i
                        input("删除成功，按任意键继续...")
                        os.system('clear')
                        break
                    else:
                        input("删除失败，按任意键继续...")
                        os.system('clear')
                        break
            else:
                input("该生不存在于系统中，按任意键继续...")
                os.system('clear')
                break
            continue
        else:
            input("按任意键返回主界面...")
            break
    return L

def change_student(L):
    while True:
        os.system('clear')
        name = input("请输入要修改的学生的姓名：")
        if name != '':
            for i in L:
                if i.get_name() == name:
                    while True:
                        try:
                            age = int(input("请输入学生%s的新年龄：" %(i.get_name())))
                        except ValueError:
                            input("您输入的年龄不是整数，按任意键继续...")
                            continue
                        try:
                            assert 18<= age <= 24, '您输入的年龄不在范围内'
                        except AssertionError as err:
                            print(err, end='')
                            input('，按任意键继续...')
                            continue
                        break
                    while True:
                        try:
                            score = float(input("请输入学生%s的新成绩：" %(i.get_name())))
                        except ValueError:
                            input("您输入的成绩不是数字，按任意键继续...")
                            continue
                        try:
                            assert 0 <= score <= 150, '您输入的年龄不在范围内'
                        except AssertionError as err:
                            print(err, end='')
                            input('，按任意键继续...')
                            continue
                        break
                    i.set_age(age)
                    i.set_score(score)
                    input("更改成功，按任意键继续...")
                    os.system('clear')
                    break
            else:
                input("该生不存在于系统中，按任意键继续...")
                os.system('clear')
                break
            continue
        else:
            input("按任意键返回主界面...")
            break
    return L

def save(L):
    try:
        file = open('si.txt', 'w')
    except OSError:
        pass
    for i in L:
        s = i.get_name() + ' ' + str(i.get_age()) + ' ' + str(i.get_score()) + '\n'
        file.write(s)
    file.close()
    return

def load():
    L = []
    try:
        file = open('/home/tarena/Vio/Project/Students/si.txt', 'rt')
    except OSError:
        pass
    flag = False
    while True:
        s = file.readline()
        if not s:
            break
        l = list(s.rstrip().split(' '))
        if l[0] != '' and 18<=int(l[1])<=24 and 0<= float(l[2])<=150:
            pass
        else:
            flag = True
            continue
        d_temp = student.Student(l[0], int(l[1]), float(l[2]))
        L.append(d_temp)
    if flag:
        print("部分非法数据已跳过")
    file.close()
    return L