import os
import student_info
import menu
import student
import math

def main_begin():
    infos = []
    while True:
        os.system('clear')
        menu.main_photo()
        choose = input("请选择")
        if choose == '1':
            os.system('clear')
            infos += student_info.input_student()
            continue
        elif choose == '2':
            os.system('clear')
            student_info.output_student(infos)
            input("按任意键继续...")
            continue
        elif choose == '3':
            os.system('clear')
            infos = student_info.del_sutdent(infos)
            continue
        elif choose == '4':
            os.system('clear')
            infos = student_info.change_student(infos)
            continue
        elif choose == '5':
            os.system('clear')
            student_info.output_student(sorted(infos, key=lambda x:x.get_score(), reverse=True))
            input("按任意键继续...")
            continue
        elif choose == '6':
            os.system('clear')
            student_info.output_student(sorted(infos, key=lambda x:x.get_score()))
            input("按任意键继续...")
            continue
        elif choose == '7':
            os.system('clear')
            student_info.output_student(sorted(infos, key=lambda x:x.get_age(), reverse=True))
            input("按任意键继续...")
            continue
        elif choose == '8':
            os.system('clear')
            student_info.output_student(sorted(infos, key=lambda x:x.get_age()))
            input("按任意键继续...")
            continue
        elif choose == '9':
            os.system('clear')
            infos += student_info.load()
            input("读取成功，按任意键继续...")
            continue
        elif choose == '0':
            os.system('clear')
            student_info.save(infos)
            input("保存成功，按任意键继续...")
            continue
        elif choose == '*':
            os.system('clear')
            print(student.Student.counts)
            input("保存成功，按任意键继续...")
            continue
        elif choose == '+':
            os.system('clear')
            L = []
            for i in infos:
                L.append(i.score)
            print(sum(L)/len(L))
            input("保存成功，按任意键继续...")
            continue
        elif choose == 'q':
            os.system('clear')
            break
        else:
            os.system('clear')
            input("您的输入有误，按任意键继续...")
            continue
main_begin()