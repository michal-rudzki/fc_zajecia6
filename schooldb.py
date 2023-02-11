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
                user_obj = School(None, student[0], student[1], USER_TYPE[0], student[2], None)
                user_obj.add_user()
            elif user_input in ['n', 'nauczyciel']:
                print(f"Podaj Tytuł oraz Imię i Nazwisko [{USER_TYPE[1]}]: ")
                teacher = input().split(' ')
                print(f"Podaj przedmiot(y) jaki będzię uczył: ")
                print(f"(przedmioty odziel przecinkami)")
                teacher.append(input().split(','))
                user_obj = School(teacher[0], teacher[1], teacher[2], USER_TYPE[1], None, teacher[3])
                user_obj.add_user()
            elif user_input in ['w', 'wychowawca']:
                pass
            

        elif user_input in ['zarządzaj', 'z']:
            print("Zarządzaj...")

if __name__ == '__main__':
    main()