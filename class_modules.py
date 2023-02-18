import json
import os.path
from globals_modules import FILEDB, USER_TYPE

DB = {
    'student': {},
    'teacher': {},
    'tutor': {}
}
class School():

    def __init__(self, *args):
        self.user_type = args[0]
        if args[0] == USER_TYPE[0] and len(args) == 1:
            self.user_type = args[0]
        elif args[0] == USER_TYPE[1] and len(args) == 1:
            self.user_type = args[0]
        elif args[0] == USER_TYPE[2] and len(args) == 1:
            self.user_type = args[0]
        elif args[0] == USER_TYPE[0]:
            self.user_name = args[1]
            self.class_name = args[2]
        elif args[0] == USER_TYPE[1]:
            self.user_name = args[1]
            self.school_items = args[2]
            self.class_name = args[3]
        elif args[0] == USER_TYPE[2]:
            self.user_name = args[1]
            self.class_name = args[2]
    
    def update_user_from_filedb(self):
        with open(FILEDB, mode='r') as file:
            data_file = file.read()
        
        DB = json.loads(data_file)
        return DB
    
    def db_creation(self):
        with open(FILEDB, mode='w') as file:
            file.write(json.dumps(DB, indent = 4))

    def check_if_duplicate(self, user_list):
        for duplicates in user_list:
            if duplicates == self.user_name:
                return True
            else:
                return False
    
    def check_class_name(self):
        DB = self.update_user_from_filedb()
        for class_list in DB[self.user_type].keys():
            if class_list == self.class_name:
                return True
        return False
            
    def add_user(self):
        if os.path.isfile(FILEDB) == False:
            self.db_creation()
            DB = self.update_user_from_filedb()
            if len(DB[self.user_type]) == 0:
                if self.user_type == USER_TYPE[0]:
                    DB[self.user_type].update({self.class_name: [self.user_name]})
                elif self.user_type == USER_TYPE[1]:
                    DB[self.user_type].update({" ".join(self.user_name): [self.class_name, self.school_items]})
                elif self.user_type == USER_TYPE[2]:
                    DB[self.user_type].update({self.class_name: [self.user_name]})
                with open(FILEDB, mode='w') as file:
                    file.write(json.dumps(DB, indent = 4))
        elif os.path.isfile(FILEDB) == True and self.check_class_name() == True:
            DB = self.update_user_from_filedb()
            if self.user_type == USER_TYPE[0]:
                DB[self.user_type][self.class_name].append(self.user_name)
            elif self.user_type == USER_TYPE[1]:
                DB[self.user_type].update({" ".join(self.user_name): [self.class_name, self.school_items]})
            elif self.user_type == USER_TYPE[2]:
                DB[self.user_type].update({self.class_name: self.user_name})
            with open(FILEDB, mode='w') as file:
                file.write(json.dumps(DB, indent = 4))
        elif os.path.isfile(FILEDB) == True and self.check_class_name() != True:
            DB = self.update_user_from_filedb()
            if self.user_type == USER_TYPE[0]:
                DB[self.user_type].update({self.class_name: [self.user_name]})
            elif self.user_type == USER_TYPE[1]:
                DB[self.user_type].update({" ".join(self.user_name): [self.class_name, self.school_items]})
            elif self.user_type == USER_TYPE[2]:
                DB[self.user_type].update({self.class_name: self.user_name})
            with open(FILEDB, mode='w') as file:
                file.write(json.dumps(DB, indent = 4))
    
    def list_all_class(self):
        DB = self.update_user_from_filedb()
        class_list = DB[USER_TYPE[0]].keys()
        return class_list
    
    def list_all_users_from_class(self, class_name):
        DB = self.update_user_from_filedb()
        tmp = class_name
        class_students = DB[USER_TYPE[0]][class_name]
        return class_students
    
    def list_all_students(self):
        DB = self.update_user_from_filedb()
        students = []
        for key, value in DB[USER_TYPE[0]].items():
            for student in value:
                students.append(" ".join(student))
        return students
    
    def list_all_teachers(self):
        DB = self.update_user_from_filedb()
        teachers = []
        for key, value in DB[USER_TYPE[1]].items():
            teachers.append(key)
        return teachers
    
    def list_teachers_class(self, teacher):
        DB = self.update_user_from_filedb()
        teacher_class = DB[USER_TYPE[1]][teacher][0]

        return teacher_class
        
    def return_students_class(self, student):
        DB = self.update_user_from_filedb()
        for key, value in DB[USER_TYPE[0]].items():
            for students_list in value:
                if students_list == student.split(" "):
                    student_class = key
                    return student_class
        return f"Brak: {student}"
    
    def get_school_items(self, class_name):
        DB = self.update_user_from_filedb()
        items_list = []
        for teacher, items in DB[USER_TYPE[1]].items():
            if class_name in items[0]:
                items_list.append([teacher, items[1]])
        school_items = items_list
        return school_items
    
    def tutor_of_the_class(self, class_name):
        DB = self.update_user_from_filedb()
        tutor = DB[USER_TYPE[2]][class_name]
        return tutor
    
    def list_tutors_class(self, tutors):
        DB = self.update_user_from_filedb()
        tutor_class = []
        tutor_students_list = []
        for key, value in DB[USER_TYPE[2]].items():
            value = " ".join(value)
            if tutors in value:
                tutor_class.append(key)
        tutor_students_list = self.list_all_users_from_class(tutor_class[0])
        return tutor_students_list
        
        
    def list_all_tutors(self):
        DB = self.update_user_from_filedb()
        tutor = []
        for key, values in DB[USER_TYPE[2]].items():
            tutor.append(" ".join(values))
        return tutor
    
    
if __name__ == '__main__':
    students_list = [['student',['Michał Korona', '3c'],['Grzegorz Kos', '3c'],['Mirosław Topor', '3c'],['Urszula Tapicer', '3c'],['Karolina Wędzonka', '3c'],['Katarzyna Wronka', '2c'],['Daniel Kiełbasa', '2c'],['Konrad Wolny', '2c'],['Piotr Węgiel', '2c'],['Alicja Cudo', '2c'],['Marcin Prokop', '1c'],['Mateusz Zielony', '1c'],['Daria Kuma', '1c'],['Dagmara Kruk', '1c'],['Tadeusz Sok', '1c']]]
    
    for student in students_list:
        for s in student[1:]:
            # 'student', 'user_name', 'class_name'
            obj = School(student[0], s[0].split(' '), s[1])
            obj.add_user()
    
    # teachers_list = [['teacher'], ['mgr Adam Kłaput', ['1c','2c'],['Matematyka','Fizyka']]]
    
    #for teacher in teachers_list: