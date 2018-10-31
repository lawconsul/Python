
class People:
    def __init__(self, name, surname, fname, birth_date, school):
        self.name = name
        self.surname = surname
        self.fname = fname
        self.birth_date = birth_date
        self.school = school

    def get_full_name(self):
        return self.surname + ' '+ self.name + ' ' + self.fname

    def get_initials(self):
        return self.surname + ' ' + self.name[0] + '.' + self.fname[0] + '.'

    def set_name(self, new_name):
        self.name = new_name


class Student(People):
    def __init__(self, name, surname, fname, birth_date, school, class_room):
        self.name = name
        self.surname = surname
        self.fname = fname
        self.birth_date = birth_date
        self.school = school
        self._class_room = {'class_num': int(class_room.split()[0]),
                            'class_char': class_room.split()[1]}

    @property
    def class_room(self):
        return "{} {}".format(self._class_room['class_num'], self._class_room['class_char'])

    def next_class(self):
        self._class_room['class_num'] += 1


class Teacher(People):
    def __init__(self, name, surname, fname, birth_date, school, subject, teach_classes):
        self.name = name
        self.surname = surname
        self.fname = fname
        self.birth_date = birth_date
        self.school = school
        self.subject = subject
        self.teach_classes = list(map(self.convert_class, teach_classes))

    def convert_class(self, class_room):
        return {'class_num': int(class_room.split()[0]),
                'class_char': class_room.split()[1]}

    def get_subject(self):
        return self.subject

 
class Parent(People):
    def __init__(self, name, surname, fname, childs):
        self.name = name
        self.surname = surname
        self.fname = fname
        #self.birth_date = birth_date
        #self.school = school
        self.childs = childs
    
    def get_childs(self):
        return self.childs

teacher1 = Teacher("Ivan", "Ivanov", "Ivanovich", "01.01.1980", "88", "Mathematic", ("5 A", "7 A"))
teacher2 = Teacher("Petr", "Petrov", "Petrovich", "01.01.1990", "88", "English", ("5 A", "6 A"))
parent_01_1 = Parent("Sidr", 'Sidorov', 'Sidorovich', ['Sidorov Oleg Sidorovich'])
parent_01_2 = Parent("Anna", 'Sidorova', 'Sidorovna', ['Sidorov Oleg Sidorovich'])
student_01 = Student("Oleg", "Sidorov", 'Sidorovich', "88", "01.01.2005","5 A")
student_11 = Student("Semen", "Simonov", "Semenovich", "88", "01.01.2004","6 A")
student_12 = Student("Olga", "Oleva", "Olegovna", "88", "02.01.2004","6 A")
student_31 = Student("San", "Sanov", "Sanich", "88", "03.01.2003","7 A")

Teachers = (teacher1, teacher2)
Parents = (parent_01_1, parent_01_2)
Students = (student_01, student_11,student_12)

#print(teacher1.get_full_name, teacher1.teach_classes)
#print(parent_01_1.get_full_name())
#print(parent_01_2.get_full_name())
#print(student_01.get_full_name())

def get_classes(Students):
    class_rooms = []
    for student in Students:
        if student.class_room not in class_rooms:
            class_rooms.insert(0,student.class_room)
    return(class_rooms)


def get_students_of_class(Students, class_room):
    Students_of_class_room = []
    for student in Students:
        if student.class_room == class_room:
            Students_of_class_room.insert(0,student.get_initials())
    return(Students_of_class_room)

def get_subjects_of_student(full_name, Students, Teachers):
    class_room = None
    for student in Students:
        if student.get_full_name() == full_name:
            class_room = student.class_room
    print(class_room)

    subjects = []
    _class_room = {'class_num': int(class_room.split()[0]),
                            'class_char': class_room.split()[1]}
    
    for teacher in Teachers:
        for class_rooms in teacher.teach_classes:
            if class_rooms == _class_room:
                subjects.insert(0,teacher.get_subject())
    return(subjects)

def get_parents_of_student(full_name, Parents):
    parents = []
    for parent in Parents:
        for child in parent.get_childs():           
            if child == full_name:
                parents.insert(0,parent.get_full_name())
    return(parents)
    

def get_teachers_of_class(class_room, Teachers):
    teachers = []
    _class_room = {'class_num': int(class_room.split()[0]),
                            'class_char': class_room.split()[1]}
    for teacher in Teachers:
        for class_rooms in teacher.teach_classes:
            if class_rooms == _class_room:
                teachers.insert(0,teacher.get_full_name())
    return(teachers)

print(get_classes(Students))
print(get_students_of_class(Students,"6 A"))
print(get_subjects_of_student("Sidorov Oleg Sidorovich", Students, Teachers))
print(get_parents_of_student("Sidorov Oleg Sidorovich", Parents))
print(get_teachers_of_class("5 A",Teachers))