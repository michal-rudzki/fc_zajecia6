import json
import os.path
from globals_modules import FILEDB

DB = {
    'student': [],
    'teacher': [],
    'tutor': []
}
class School():

    def __init__(self, title, name, surname, user_type, class_name, school_items):
        self.title = title
        self.name = name
        self.surname = surname
        self.user_type = user_type
        self.class_name = class_name
        self.school_items = school_items
    
    def update_user_from_filedb(self):
        with open(FILEDB, mode='r') as file:
            data_file = file.read()
        
        DB = json.loads(data_file)
        return DB
    
    def db_creation(self):
        with open(FILEDB, mode='w') as file:
            file.write(json.dumps(DB, indent=4))

    def add_user(self):
        # make a exception for student, teacher, tutor
        if os.path.isfile(FILEDB) == False:
            self.db_creation()
        DB = self.update_user_from_filedb()
        DB[self.user_type].append([self.name, self.surname, self.class_name])
        #print(DB)
        with open(FILEDB, mode='w') as file:
            file.write(json.dumps(DB, indent=4))


if __name__ == '__main__':
    d = School(name='Michał', surname='Rudzki', user_type='student', class_name='2C')
    d.add_user()
    
    f = School(name='Grzegorz', surname='Rudzki', user_type='teacher', class_name='1C')
    f.add_user()
    
    g = School(name='Urszula', surname='Rudzka', user_type='tutor', class_name='2C')
    g.add_user()