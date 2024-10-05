class Student:
    def __init__(self,name,student_id,grade_level,math,science,history,english):
        self.name = name
        self.student_id = student_id
        self.grade_level = grade_level
        self.math = math
        self.science = science
        self.history = history
        self.english = english
        self.grades = [math,science,history,english]

    def update_grade(self,subject_I,grade):
        self.grades[subject_I] = grade
    
    def get_gpa(self,):
        grade_sum = 0.0
        for g in self.grades:
            if g == "A":
                grade_sum += 4
            elif g == "B":
                grade_sum += 3
            elif g == "C":
                grade_sum += 2
            elif g == "D":
                grade_sum += 1
        return grade_sum / len(self.grades)
    
    def student_info(self):
        print("Name: " + self.name)
        print("Id: " + str(self.student_id))
        print("Grades: " + ', '.join(self.grades))
        print("GPA: " + str(self.get_gpa()))

    def to_list(self):
        return [self.name, self.student_id, self.grade_level, self.math, self.science, self.history, self.english]

    @staticmethod
    def from_list(data):
        name, student_id, grade_level, math, science, history, english = data
        return Student(name, student_id, grade_level, math, science, history, english)

if __name__ == "__main__":
    callem = Student("Callem", 12703)
    callem.update_grade(0,"A")
    callem.update_grade(1,"B")
    callem.update_grade(2,"B")
    callem.update_grade(3,"A")
    callem.student_info()