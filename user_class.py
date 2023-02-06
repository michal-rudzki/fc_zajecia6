import json
import os.path

DB = {
    'student': [],
    'teacher': [],
    'tutor': []
}
class School():

    def __init__(self, name, surname, user_type, class_name):
        self.name = name
        self.surname = surname
        self.user_type = user_type
        self.class_name = class_name
    
    def update_user_from_filedb(self):
        with open('filedb.py', mode='r') as file:
            data_file = file.read()
        
        DB = json.loads(data_file)
        return DB
    
    def db_creation(self):
        with open('filedb.py', mode='w') as file:
            file.write(json.dumps(DB, indent=4))

    def add_user(self):
        if os.path.isfile('filedb.py') == False:
            self.db_creation()
        DB = self.update_user_from_filedb()
        DB[self.user_type].append([self.name, self.surname, self.class_name])
        print(DB)
        with open('filedb.py', mode='w') as file:
            file.write(json.dumps(DB, indent=4))


if __name__ == '__main__':
    d = School(name='Michał', surname='Rudzki', user_type='student', class_name='2C')
    d.add_user()
    
    f = School(name='Grzegorz', surname='Rudzki', user_type='teacher', class_name='1C')
    f.add_user()
    
    g = School(name='Urszula', surname='Rudzka', user_type='tutor', class_name='2C')
    g.add_user()