'''PROJECT - 1 :- STUDENT MANAGEMENT SYSTEM'''
import json
class studentmanager:
    def __init__(self,filename = 'student.json'):
       self.filename = filename
       self.student = self.load_student_data()
    def load_student_data(self):
        try:
            with open(self.filename,'r') as file:
                content = json.load(file)
                return (content)
        except FileNotFoundError:
            return {}
    def save_student_data(self):
            with open(self.filename,'w') as file:
                json.dump(self.student,file)
    def view_student(self):
        new = self.student
        for key_1,value_1 in new.items():
           print()
           print(f'{key_1}:- ')
           for key,value in value_1.items():
              print(f'{key} = {value}') 
    def add_student(self):
        name = input("Enter student name: ").lower()
        if name in self.student:
                print('student already exists')
        else:
            subjects = {}
            n = int(input("How many subjects? "))

            for i in range(n):
                sub = input("Enter subject name: ")
                marks = int(input("Enter marks: "))
                subjects[sub] = marks

            self.student[name] = subjects
            self.save_student_data()

            print("Student added successfully")
    def delete_student(self):
        name = input("enter the student name :- ").lower()
        if name in self.student:
            del self.student[name]
            self.save_student_data()
            print(self.load_student_data())
        else:
            print('student dont exists')

    def search_student(self):
        name = input("enter the student name :-  ").lower()
        # print(self.student[name])
        #method-2
        if name in self.student:
            print(self.student[name])
        else:
            print('student dont exists')
    
    def show_topper(self):
        topper_marks = 0
        topper_name = ''
        for student_name , subjects in self.student.items():
            total_marks = sum(subjects.values())
            if total_marks > topper_marks:
                topper_marks = total_marks
                topper_name = student_name
        print(f'topper = {topper_name} , marks = {topper_marks}')
    def show_class_average(self):
        total_class = 0
        total_student = len(self.student)
        for student_name,subjects in self.student.items():
            total_subjects = (sum(subjects.values()))
            total_class = total_class + total_subjects
        if total_student > 0:
            class_average = total_class / total_student
            return(class_average)
    def show_pass_fail(self):
        pass_list =[]
        fail_list = []
        for student_name,subject in self.student.items():
            avg = sum(subject.values()) /len(subject)
            print(avg)
            if avg > 60:
                pass_list.append(student_name)
            else:
                fail_list.append(student_name)
        print(pass_list)
        print(fail_list)            
    def menu_system(self):
        while True:
                try:
                    print('chooose the option you wante ')
                    print('1   :- add student    ')
                    print('2 :- delete student ')
                    print('3 :- search student ')
                    print('4 :- show topper    ')
                    print('5 :- for pass / fail list ')
                    print('6 :- class average  ')
                    print('7 :- view student ')
                    print("8 :- to exit the program")

                    user = int(input('enter the option :-'))
                    if user == 1:
                        (self. add_student())
                    elif user == 2:
                        (self. delete_student())
                    elif user == 3:
                        (self. search_student())
                    elif user == 4:
                        (self. show_topper())
                    elif user == 5:
                        (self. show_pass_fail())
                    elif user == 6:
                        print(self. show_class_average())
                    elif user == 7:
                        (self. view_student())
                    elif user == 8:
                        break
                    else:
                        print('invalid')

                except ValueError:
                    print('enter valid input >>>(number)<<<')
            
           
new = studentmanager()
# marks = {'physics':45,'maths':67}
# new.add_student('saikumar',marks)
# marks_1 = {'physics':75,'maths':97}
# new.add_student('manoj',marks_1)
# marks_3 = {'physics':95,'maths':67}
# new.add_student('reddy',marks_3)
# new.add_student('reddy',marks)
# new.delete_student('saikumar')
# print(new.load_student_data())
# new.search_student('reddy')
# new.show_topper()
# new.show_class_average()
# new.show_pass_fail()
new.menu_system()
