import sys
from globals_modules import USER_TYPE
from class_modules import School

def main():
    while True:
        print("Wybierz: [k]oniec, [u]twórz, [z]arządzaj")
        user_input = input().strip()
        if not user_input or user_input in ['koniec', 'k']:
            print("Koniczymy...")
            break

        elif user_input in ['utwórz', 'u']:
            print("Utwórz...")
            print("[u]czeń, [n]auczyciel, [w]ychowawca")
            user_input = input().strip()
            if user_input in ['u', 'uczeń']:
                print(f"Podaj Imie i Nazwisko: [{USER_TYPE[0]}] ")
                student = input().split(' ')
                print("Podaj nazwę klasy: ")
                student.append(input().strip())
                student_obj = School(USER_TYPE[0], student[0:2], student[2])
                student_obj.add_user()

            elif user_input in ['n', 'nauczyciel']:
                print(f"Podaj Tytuł oraz Imię i Nazeisko: [{USER_TYPE[1]}] ")
                teacher  = input().split(' ')
                print(f"Podaj nazwę przedmiotu prowadzonego (może lista przedmiotów oddzielona ','): ")
                teacher.append(input().split(','))
                print(f"Podaj listę klas, które nauczyciel prowadzi: ")
                school_subject = []
                while True:
                    user_input = input()
                    if not user_input or user_input == 'k' or user_input == 'koniec':
                        break
                    school_subject.append(user_input)
                teacher.append(school_subject)
                if len(teacher) == 5:
                    teacher_obj = School(USER_TYPE[1], teacher[0:3], teacher[3], teacher[4])
                    teacher_obj.add_user()
                elif len(teacher) == 6:
                    teacher_obj = School(USER_TYPE[1], teacher[0:4], teacher[4], teacher[5])
                    teacher_obj.add_user()
                    
            elif user_input in ['w', 'wychowawca']:
                print(f"Podaj Tytuł oraz Imię i Nazwisko: [{USER_TYPE[2]}] ")
                tutor = input().split(' ')
                print(f"Nazwa prowadzonej klasy: ")
                tutor.append(input().strip())
                if len(tutor) == 4:
                    tutor_obj = School(USER_TYPE[2], tutor[0:3], tutor[3])
                    tutor_obj.add_user()
                elif len(tutor) == 5:
                    tutor_obj = School(USER_TYPE[2], tutor[0:4], tutor[4])
                    tutor_obj.add_user()

        elif user_input in ['zarządzaj', 'z']:
            print(f"Zarządzaj...")
            print(f"[kl]asa, [u]czeń, [n]auczyciel, [w]ychowawca")
            user_input = input()
            if user_input in ['klasa', 'kl']:
                print(f"Lista klas:")
                class_list = School(USER_TYPE[0])
                all_class = class_list.list_all_class()
                for list_class in all_class:
                    print(list_class)
                print(f"wybierz klasę: ")
                user_input = input()
                class_list = School(USER_TYPE[0])
                students_list = class_list.list_all_users_from_class(user_input)
                tutor = " ".join(class_list.tutor_of_the_class(user_input))
                print(f"Wychowawcą {user_input} jest {tutor}.")
                for students in students_list:
                    student = " ".join(students)
                    print(f"uczeń: {student}")
            elif user_input in ['uczeń', 'u']:
                students = School(USER_TYPE[0])
                for student in students.list_all_students():
                    print(f"student: {student}")
                print(f"Podaj Imię i Nazwisko ucznia: ")
                user_input = input()
                student_class = students.return_students_class(user_input)
                school_items = students.get_school_items(student_class)
                print(f"Uczeń [{user_input}] chodzi do klasy [{student_class}]")
                print(f"Przedmioty: \n")
                for items in school_items:
                    if items[0]:
                        print(f"Nauczyciel: {items[0]}")
                        for i in items[1]:
                            print(f"Przedmiot: {i}")
                            
            elif user_input in ['nauczyciel', 'n']:
                pass
            elif user_input in ['wychowawca', 'w']:
                pass

if __name__ == '__main__':
    main()