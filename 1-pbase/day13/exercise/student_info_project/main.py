from menu import *
from student_info import *



def main():

    L=[]
    while True:
        show_menu()
        s=input('请选择：')
        if s=='1':
            input_student(L)
        elif s=='2':
            output_student(L)
        elif s== '3':
            remove_student(L)
        elif s== '4':
            change_student(L)
        elif s=='5':
            L2=sorted(L,key=reverse_score,reverse=True)
            output_student(L2)
        elif s=='6':
            L2=sorted(L,key=reverse_score)
            output_student(L2)
        elif s=='7':
            L2=sorted(L,key=reverse_age,reverse=True)
            output_student(L2)
        elif s=='8':
            L2=sorted(L,key=reverse_age)
            output_student(L2)
        elif s=='q':
            break


main()