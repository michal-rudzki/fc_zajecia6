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
        if args[0] == USER_TYPE[0]:
            self.user_name = args[1]
            self.class_name = args[2]
        elif args[0] == USER_TYPE[1]:
            self.user_name = args[1]
            self.school_items = args[2]
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
                    pass
                elif self.user_type == USER_TYPE[2]:
                    DB[self.user_type].update({self.class_name: [self.user_name]})
                with open(FILEDB, mode='w') as file:
                    file.write(json.dumps(DB, indent = 4))
        elif os.path.isfile(FILEDB) == True and self.check_class_name() == True:
            DB = self.update_user_from_filedb()
            if self.user_type == USER_TYPE[0]:
                DB[self.user_type][self.class_name].append(self.user_name)
            elif self.user_type == USER_TYPE[1]:
                pass
            elif self.user_type == USER_TYPE[2]:
                DB[self.user_type].update({self.class_name: self.user_name})
            with open(FILEDB, mode='w') as file:
                file.write(json.dumps(DB, indent = 4))
        elif os.path.isfile(FILEDB) == True and self.check_class_name() != True:
            DB = self.update_user_from_filedb()
            if self.user_type == USER_TYPE[0]:
                DB[self.user_type].update({self.class_name: [self.user_name]})
            elif self.user_type == USER_TYPE[1]:
                pass
            elif self.user_type == USER_TYPE[2]:
                DB[self.user_type].update({self.class_name: self.user_name})
            with open(FILEDB, mode='w') as file:
                file.write(json.dumps(DB, indent = 4))
            

if __name__ == '__main__':
    lista_db =[['student',['Michał Rudzki', '3c'],['Grzegorz Rudzki', '3c'],['Mirosław Topor', '3c'],['Urszula Tapicer', '3c']]]
    
    for student in lista_db:
        for s in student[1:]:
            # 'student', 'user_name', 'class_name'
            obj = School(student[0], s[0].split(' '), s[1])
            obj.add_user()