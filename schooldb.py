import sys

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
                print("Podaj Imie i Nazwisko:")
                student = input().split(' ')
                print("Podaj nazwę klasy: ")
                student.append(input().strip())
                print(student)
            elif user_input in ['n', 'nauczyciel']:
                pass
            elif user_input in ['w', 'wychowawca']:
                pass
            

        elif user_input in ['zarządzaj', 'z']:
            print("Zarządzaj...")

if __name__ == '__main__':
    main()