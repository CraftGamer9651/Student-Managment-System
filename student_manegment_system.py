from student import Student
import csv
import tkinter as tk



def save_students_to_file(students, filename):
    #Name, student ID, grade level, grades
    file = open(filename, 'w', newline='')
    writer = csv.writer(file)
    writer.writerow(["Name", "Student ID", "Grade level","Math","Science","History","English"])
    for s in students:
        writer.writerow(s.to_list())

def load_students_from_file(filename):
    students = []
    file = open(filename, 'r', newline='')
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        s = Student.from_list(row)
        students.append(s)
        return students
    root.destroy()

def load_clicked():
    global entry
    filename = entry.get()
    load_students_from_file(filename)


def lookup(name,students):
    student = ("")
    for s in students:
        if s.name == name:
           return name

def remove_student(name,filename):
    lookup(name,filename)




def displayMenu():
    print("\n1. Add student")
    print("2. Remove student")
    print("3. Lookup student")
    print("4. Switch schools")
    print("5. Update grades")
    print("6. Save and exit program\n")

def close_window():
    root.destroy()

if __name__ == "__main__":

    school = []
    fileName = ""

    root = tk.Tk()
    root.title("SMSA")
    #filename = tk.StringVar()

    root.configure(bg="#0085FF")
    root.minsize(192, 108)


    tk.Label(root, text="Welcome to the Student Manegment System", bg="#0085FF").grid(column=0, row=0)
    tk.Label(root, text="Enter file name:", bg="#0085FF").grid(column=0, row=1)
    tk.Button(root, text='Create new school', bg="#FFA500").grid(column=0, row=2)
    tk.Button(root, text='Load school from file', command=load_clicked, bg="#FFA500").grid(column=1, row=2)
    tk.Button(root, text='Exit application', command=close_window, bg="#FF0000").grid(column=2, row=2)
    entry = tk.Entry(root, textvariable=fileName).grid(column=1, row=1)
    
    root.mainloop()
    

    while True:
        displayMenu()
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter student name:\n")
            save_students_to_file(name,fileName)
        elif choice == "2":
            print("Hi")
        elif choice == "3":
            name = input("Enter student name:\n")
            lookup(name,studentList) # type: ignore
        elif choice == "4":
            fileName = input("Enter name of file to save to (ex. schoolname.csv):\n")
        elif choice == "6":
            print("Saving...")
            save_students_to_file(school,fileName)
            print("Saved\nClosing program\n")
            break
        else:
            print("\nError:\nInvalid input\n")



    #- 1. create a master list of students
    # 2. password save to "pass.txt"
    #- 3. open new school of load from file
    # 4. find student, add student, remove student, exit
    # 4. load student by name, load student by grade, load student by ID, or load student by grades
    # 5. print chosen option
    # 6. return to main menu
'''

test = Student("Callem",13,"12703","A","B","B","A")
test1 = Student("Jake",13,"26473","A","B","A","B")
test2 = Student("Mckinley",14,"16437","B","C","B","B")
student_list = [test,test1,test2]

save_students_to_file(student_list, "test.csv")

read_students_list = load_students_from_file("test.csv")
for s in read_students_list:
    s.student_info()

def copy_students_to_new_file():
    load_students = load_students_from_file("test.csv")
    save_students_to_file(load_students, "test_copy.csv")

copy_students_to_new_file()

load_students = load_students_from_file("test.csv")
load_students_reversed = []
for  i in range(len(load_students) - 1, - 1, - 1):
    load_students_reversed.append(load_students[i])

save_students_to_file(load_students_reversed, "test_copy.csv")'''