import random

class Teacher:
    def __init__(self,
                 name:str = 'BestTeacher',
                 age:int = 25,
                 gender:str = 'Male',
                 subject:str = 'Programming',
                 interest:int = 10,
                 fatigue:int = 6):
        self.name = name
        self.age = age
        self.gender = gender
        self.subject = subject
        self.interest = interest
        self.fatigue = fatigue

    def ask_a_student(self, student):
        if student.knowledge > 8:
            print('Студент ответил верно')
        elif student.knowledge > 5:
            if student.fatigue > 6:
                if bool(random.getrandbits(1)):
                    print('Студент ответил верно')
                else:
                    print('Студент ответил не верно')
            else:
                print('Студент ответил верно')
        else:
            print('Студент ответил не верно')

    def share_something_new(self, student):
        if student.knowledge == 10:
            print('Знания студента максимальны')
        elif student.interest > 4 and student.fatigue < 7:
            student.knowledge += 1
            print('Новые знания получены')
        else:
            print('Студент не обучился')

    def rest(self, student):
        if student.fatigue > 0:
            student.fatigue -= 1
            if self.fatigue > 0:
                self.fatigue -= 1
            print('Отдых')
        else:
            print('Студент полностью отдохнувший')

    def to_entice(self, student):
        if student.interest < 10:
            student.interest += 1
            print('Студент заинтересовался')
        else:
            print('Студент уже заинтересован')

    def become_interested(self):
        if self.interest < 10:
            self.interest += 1
            print('Интерес повышен')
        else:
            print('Максимальный интерес достигнут')


class Student:
    def __init__(self,
                 name:str = 'Student 1',
                 age:int = 18,
                 gender:str = 'Male',
                 interest:int = 7,
                 knowledge:int = 7,
                 perseverance:int = 4,
                 fatigue:int = 6):
        self.name = name
        self.age = age
        self.gender = gender
        self.interest = interest
        self.knowledge = knowledge
        self.perseverance = perseverance
        self.fatigue = fatigue

    def to_skip(self):
        if self.fatigue > 0:
            self.fatigue -= 1
        if self.knowledge > 0:
            self.knowledge -= 1
        if self.perseverance > 0:
            self.perseverance -= 1
        print('Пара прогулена')

    def learn_something_new(self):
        if self.knowledge < 10:
            self.knowledge += 1
            print('Новый материал выучен')
        else:
            print('Материал повторён')

    def rest(self):
        if self.fatigue > 0:
            self.fatigue -= 1
            print('Отдых')
        else:
            print('Время прошло')

    def ask_the_teacher(self, teacher):
        if teacher.interest > 3:
            if teacher.fatigue < 10:
                teacher.fatigue += 1
            if self.knowledge < 10:
                self.knowledge += 1
            if self.fatigue < 10:
                self.fatigue += 1
                print('Преподаватель ответил')
        else:
            if self.perseverance > 0:
                self.perseverance -= 1
            print('Преподаватель не ответил')