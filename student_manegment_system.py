from student import Student
import csv
import tkinter as tk
import os

filename = None

def save_students_to_file(students, filename):
    file_exists = os.path.exists(filename)
    is_empty = os.path.getsize(filename) == 0 if file_exists else True

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        if is_empty:
            writer.writerow(["Name", "Student ID", "Password", "Grade level", "Math", "Science", "History", "English"])
        for s in students:
            writer.writerow(s.to_list())

def load_students_from_file(filename):
    students = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        try:
            header = next(reader)
        except StopIteration:
            return students
        for row in reader:
            if row:
                s = Student.from_list(row)
                students.append(s)
    return students

def custom_askstring(title, prompt):
    result = None

    def on_submit():
        nonlocal result
        result = entry.get()
        dialog.destroy()

    dialog = tk.Toplevel(main)
    dialog.title(title)
    dialog.configure(bg="#8dc4ff")

    tk.Label(dialog, text=prompt, bg="#8dc4ff", font=("Arial", 12)).pack(padx=20, pady=10)
    entry = tk.Entry(dialog, font=("Arial", 12))
    entry.pack(padx=20, pady=10)
    tk.Button(dialog, text="Submit", command=on_submit, bg="#FFC88D").pack(pady=10)

    dialog.transient(main)
    dialog.grab_set()
    main.wait_window(dialog)
    return result

def exit_message():
    dialog = tk.Toplevel(main)
    dialog.title("Saving")
    dialog.geometry("300x150")
    dialog.configure(bg="#8dc4ff")

    tk.Label(dialog, text="Changes saved.", bg="#8dc4ff", font=("Arial", 12), wraplength=300).pack(padx=20, pady=20)
    tk.Button(dialog, text="Exit", command=dialog.destroy, bg="#FFC88D").pack(pady=10)

    dialog.transient(main)
    dialog.grab_set()
    main.wait_window(dialog)

def custom_message(title, message):
    dialog = tk.Toplevel(main)
    dialog.title(title)
    dialog.geometry("300x150")
    dialog.configure(bg="#8dc4ff")

    tk.Label(dialog, text=message, bg="#8dc4ff", font=("Arial", 12), wraplength=300).pack(padx=20, pady=20)
    tk.Button(dialog, text="OK", command=dialog.destroy, bg="#FFC88D").pack(pady=10)

    dialog.transient(main)
    dialog.grab_set()
    main.wait_window(dialog)

def remove_student(student_id, filename):
    students = load_students_from_file(filename)
    student_to_remove = None
    for s in students:
        if s.student_id == student_id:
            student_to_remove = s
            break
    if not student_to_remove:
        custom_message("Error", f"No student found with ID {student_id}.")
        return
    updated_students = [s for s in students if s.student_id != student_id]
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Student ID", "Password", "Grade level", "Math", "Science", "History", "English"])
        for s in updated_students:
            writer.writerow(s.to_list())
    custom_message("Success", f"{student_to_remove.name} with student ID {student_to_remove.student_id} has been removed.")

def create_hover_button(parent, text, command):
    btn = tk.Button(parent, text=text, command=command, font=("Arial", 20), width=30, height=2, bg="#4CAF50", fg="white")
    btn.bind("<Enter>", lambda e: e.widget.config(bg="#66bbff"))
    btn.bind("<Leave>", lambda e: e.widget.config(bg="#4CAF50"))
    btn.pack(pady=10)
    return btn

def open_main_menu():
    global main, title_font, button_font
    main = tk.Tk()
    main.title("Student Management System Main Menu")

    main.geometry("1100x720")
    main.configure(bg="#8dc4ff")

    container = tk.Frame(main, bg="#8dc4ff")
    container.place(relx=0.5, rely=0.5, anchor='center')

    title_font = ("Arial", 28, "bold")
    button_font = ("Arial", 20)

    tk.Label(container, text="Welcome to the Student Management System", bg="#8dc4ff", font=title_font, fg="#000000").pack(pady=20)
    tk.Label(container, text="Please Select an Option", bg="#8dc4ff", font=title_font, fg="#007FFF").pack(pady=40)
    tk.Button(container, text="Add Student", command=add_student, font=button_font, width=30, height=2, bg="#FFC88D").pack(pady=10)
    tk.Button(container, text="Remove Student", command=remove_student_gui, font=button_font, width=30, height=2, bg="#FFC88D").pack(pady=10)
    tk.Button(container, text="Lookup Student", command=lookup_student_gui, font=button_font, width=30, height=2, bg="#FFC88D").pack(pady=10)
    tk.Button(container, text="Switch CSV File", command=switch_file, font=button_font, width=30, height=2, bg="#FFC88D").pack(pady=10)
    tk.Button(container, text="Save and Exit", command=save_and_exit, font=button_font, width=30, height=2, bg="#ff0000", fg="#FFFFFF").pack(pady=20)

studentList = load_students_from_file("students.csv")

if __name__ == "__main__":
    def get_entry_value(name):
        global fileName
        fileName = text_var.get()
        name.destroy()

    title_font = ("Arial", 28, "bold")
    button_font = ("Arial", 20)

    login = tk.Tk()
    login.title("Student Management System Login")

    login.geometry("720x240")
    login.configure(bg="#8dc4ff")

    container = tk.Frame(login, bg="#8dc4ff")
    container.place(relx=0.5, rely=0.5, anchor='center')

    tk.Label(container, text="Student Management System Login", bg="#8dc4ff", font=title_font, fg="#000000").pack(pady=1)
    tk.Label(container, text="Enter Filename:", bg="#8dc4ff", font=title_font, fg="#007FFF").pack(pady=10)
    text_var = tk.StringVar()
    entry = tk.Entry(container, textvariable=text_var, width=30).pack(pady=10)
    tk.Button(container, text="Enter", command=lambda: get_entry_value(login), bg="#FFC88D").pack(pady=1)

    text_var.set("students.csv")

    login.mainloop()

    school = []
    if os.path.exists(fileName):
        school = load_students_from_file(fileName)
    else:
        print("File not found. Creating new file.")
        open(fileName, 'w').close()
        school = []

    studentList = school.copy()

    def add_student():
        name = custom_askstring("Add Student", "Enter student name:")
        student_id = custom_askstring("Add Student", "Enter student ID:")
        password = custom_askstring("Add Student", "Enter student password:")
        grade_level = custom_askstring("Add Student", "Enter grade level:")
        math = custom_askstring("Add Student", "Enter math grade:")
        science = custom_askstring("Add Student", "Enter science grade:")
        history = custom_askstring("Add Student", "Enter history grade:")
        english = custom_askstring("Add Student", "Enter English grade:")

        if None in [name, student_id, password, grade_level, math, science, history, english]:
            custom_message("Cancelled", "Student addition cancelled.")
            return

        new_student = Student(name, student_id, password, grade_level, math, science, history, english)
        school.append(new_student)
        save_students_to_file([new_student], fileName)
        custom_message("Success", f"{name} has been added.")

    def remove_student_gui():
        student_id = custom_askstring("Remove Student", "Enter student ID to remove:")
        if student_id:
            remove_student(student_id, fileName)

    def lookup_student_gui():
        name = custom_askstring("Lookup Student", "Enter student name:")
        if name:
            matching_students = [s for s in studentList if s.name == name]
            if matching_students:
                s = matching_students[0]
                info = (
                    f"Name: {s.name}\nStudent ID: {s.student_id}\nPassword: {s.password}\nGrade: {s.grade_level}\n"
                    f"Math grade: {s.math}\nScience grade: {s.science}\nHistory grade: {s.history}\nEnglish grade: {s.english}"
                )
                custom_message("Student Info", info)
            else:
                custom_message("Not Found", f"No student named {name} found.")

    def switch_file():
        global fileName, school
        new_file = custom_askstring("Switch File", "Enter new file name (ex. school.csv):")
        if new_file:
            fileName = new_file
            if os.path.exists(fileName):
                school = load_students_from_file(fileName)
                custom_message("Success", f"Switched to file: {fileName}")
            else:
                open(fileName, 'w').close()
                school = []
                custom_message("New File", f"Created new file: {fileName}")

    def save_and_exit():
        save_students_to_file(school, fileName)
        exit_message()
        main.destroy()

    open_main_menu()
    main.mainloop()