import tkinter as tk
from tkinter import messagebox


courses = {}

def welcome_screen():
    for widget in root.winfo_children():
        widget.destroy() 

    root.configure(bg="black")  

    tk.Label(root, text="Grade Calculator", fg="#0080ff", bg="black", font=("Arial", 30, "bold")).place(relx=0.5, rely=0.3, anchor="center")

    tk.Label(root, text="Drag to Start", fg="white", bg="black", font=("Arial", 16)).place(relx=0.5, rely=0.5, anchor="center")

    global start_slider
    start_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", length=300, bg="black", fg="white", 
                            showvalue=0, sliderlength=40, troughcolor="#172a45", highlightthickness=0, 
                            command=check_slider)
    start_slider.place(relx=0.5, rely=0.6, anchor="center")

def check_slider(value):
    if int(value) == 100:
        open_next_page()


def submit_course():
    course_name = course_entry.get().strip().upper() 
    if course_name:
        courses[course_name] = []  
        open_next_page()



def grades_exist():
    return any(len(grades) > 0 for grades in courses.values())


def open_next_page():
    for widget in root.winfo_children():
        widget.destroy() 
    
    tk.Label(root, text="Choose an Action", fg="white", bg="#0a192f", font=("Arial", 16)).pack(pady=20)
    
    tk.Button(root, text="Add Another Course", command=start_program, bg="#0080ff", fg="white", font=("Arial", 14), width=25, height=2).pack(pady=10)
    tk.Button(root, text="Enter Grades", command=enter_grades_screen, bg="#0080ff", fg="white", font=("Arial", 14), width=25, height=2).pack(pady=10)
    tk.Button(root, text="Calculate Average", command=calculate_average_screen, bg="#0080ff", fg="white", font=("Arial", 14), width=25, height=2).pack(pady=10)
    tk.Button(root, text="Calculate Final Grade", command=required_final_grade_screen, bg="#0080ff", fg="white", font=("Arial", 14), width=25, height=2).pack(pady=10)
    


    if grades_exist():
        tk.Button(root, text="See All Assignments & Marks", command=show_all_assignments, bg="#0080ff", fg="white", font=("Arial", 14), width=25, height=2).pack(pady=10)
    else:
        tk.Button(root, text="See All Assignments & Marks", state=tk.DISABLED, bg="#444444", fg="white", font=("Arial", 14), width=25, height=2).pack(pady=10)
    
    tk.Button(root, text="Back", command=start_program, bg="#ffaa00", fg="black", font=("Arial", 12)).pack(pady=20)
    tk.Button(root, text="Quit", command=root.quit, bg="#ff4040", fg="white", font=("Arial", 12)).pack(pady=20)

def start_program():
    for widget in root.winfo_children():
        widget.destroy() 
    
    tk.Label(root, text="Enter a Course:", fg="white", bg="#0a192f", font=("Arial", 20)).place(relx=0.5, rely=0.4, anchor="center")

    global course_entry
    course_entry = tk.Entry(root, font=("Arial", 20))
    course_entry.place(relx=0.5, rely=0.5, anchor="center")  

    tk.Button(root, text="Submit", command=submit_course, bg="#0080ff", fg="white", font=("Arial", 12)).place(relx=0.5, rely=0.6, anchor="center")  # Moves button below



def enter_grades_screen():
    for widget in root.winfo_children():
        widget.destroy()  
    
    tk.Label(root, text="Enter Grades", fg="white", bg="#0a192f", font=("Arial", 20)).place(relx=0.5, rely=0.2, anchor="center")

    global grade_course_entry, assignment_entry, grade_entry, weight_entry

    tk.Label(root, text="Course Name:", fg="white", bg="#0a192f", font=("Arial", 16)).place(relx=0.4, rely=0.3, anchor="e")
    grade_course_entry = tk.Entry(root, font=("Arial", 16), width=20)
    grade_course_entry.place(relx=0.5, rely=0.3, anchor="w")

    tk.Label(root, text="Assignment Name:", fg="white", bg="#0a192f", font=("Arial", 16)).place(relx=0.4, rely=0.38, anchor="e")
    assignment_entry = tk.Entry(root, font=("Arial", 16), width=20)
    assignment_entry.place(relx=0.5, rely=0.38, anchor="w")

    tk.Label(root, text="Grade:", fg="white", bg="#0a192f", font=("Arial", 16)).place(relx=0.4, rely=0.46, anchor="e")
    grade_entry = tk.Entry(root, font=("Arial", 16), width=20)
    grade_entry.place(relx=0.5, rely=0.46, anchor="w")

    tk.Label(root, text="Weight:", fg="white", bg="#0a192f", font=("Arial", 16)).place(relx=0.4, rely=0.54, anchor="e")
    weight_entry = tk.Entry(root, font=("Arial", 16), width=20)
    weight_entry.place(relx=0.5, rely=0.54, anchor="w")

    tk.Button(root, text="Submit", command=add_grade, bg="#0080ff", fg="white", font=("Arial", 14), width=15, height=2).place(relx=0.5, rely=0.65, anchor="center")
    tk.Button(root, text="Back", command=open_next_page, bg="#ffaa00", fg="black", font=("Arial", 14), width=15, height=2).place(relx=0.5, rely=0.75, anchor="center")

def calculate_average_screen():
    for widget in root.winfo_children():
        widget.destroy()  

    tk.Label(root, text="Calculate Course Average", fg="white", bg="#0a192f", font=("Arial", 20)).place(relx=0.5, rely=0.2, anchor="center")

    global avg_course_entry
    tk.Label(root, text="Enter Course Name:", fg="white", bg="#0a192f", font=("Arial", 16)).place(relx=0.4, rely=0.4, anchor="e")
    avg_course_entry = tk.Entry(root, font=("Arial", 16), width=20)
    avg_course_entry.place(relx=0.5, rely=0.4, anchor="w")

    tk.Button(root, text="Calculate", command=calculate_average, bg="#0080ff", fg="white", font=("Arial", 14), width=15, height=2).place(relx=0.5, rely=0.5, anchor="center")
    tk.Button(root, text="Back", command=open_next_page, bg="#ffaa00", fg="black", font=("Arial", 14), width=15, height=2).place(relx=0.5, rely=0.6, anchor="center")

def required_final_grade_screen():
    for widget in root.winfo_children():
        widget.destroy()  

    tk.Label(root, text="Required Final Grade", fg="white", bg="#0a192f", font=("Arial", 20)).place(relx=0.5, rely=0.2, anchor="center")

    global current_avg_entry, final_weight_entry, desired_grade_entry

    tk.Label(root, text="Current Average (%):", fg="white", bg="#0a192f", font=("Arial", 16)).place(relx=0.4, rely=0.35, anchor="e")
    current_avg_entry = tk.Entry(root, font=("Arial", 16), width=10)
    current_avg_entry.place(relx=0.5, rely=0.35, anchor="w")

    tk.Label(root, text="Final Exam Weight (%):", fg="white", bg="#0a192f", font=("Arial", 16)).place(relx=0.4, rely=0.45, anchor="e")
    final_weight_entry = tk.Entry(root, font=("Arial", 16), width=10)
    final_weight_entry.place(relx=0.5, rely=0.45, anchor="w")

    tk.Label(root, text="Desired Final Grade (%):", fg="white", bg="#0a192f", font=("Arial", 16)).place(relx=0.4, rely=0.55, anchor="e")
    desired_grade_entry = tk.Entry(root, font=("Arial", 16), width=10)
    desired_grade_entry.place(relx=0.5, rely=0.55, anchor="w")

    tk.Button(root, text="Calculate", command=calculate_required_final_grade, bg="#0080ff", fg="white", font=("Arial", 14), width=15, height=2).place(relx=0.5, rely=0.65, anchor="center")
    tk.Button(root, text="Back", command=open_next_page, bg="#ffaa00", fg="black", font=("Arial", 14), width=15, height=2).place(relx=0.5, rely=0.75, anchor="center")


def calculate_average():
    course_name = avg_course_entry.get().strip().upper()  

    if course_name not in courses or not courses[course_name]:
        messagebox.showerror("Error", "Course not found or no grades entered.")
        return

    total_weighted_score = sum(score * weight for _, score, weight in courses[course_name])
    total_weight = sum(weight for _, _, weight in courses[course_name])

    average = total_weighted_score / total_weight if total_weight > 0 else 0
    messagebox.showinfo("Course Average", f"The average for {course_name} is {average:.2f}%")


# Function to add a grade
def add_grade():
    course_name = grade_course_entry.get().strip().upper()  
    assignment_name = assignment_entry.get().strip()
    
    if course_name not in courses:
        messagebox.showerror("Error", "Course not found. Please add the course first.")
        return
    
    if not assignment_name:
        messagebox.showerror("Error", "Please enter an assignment name.")
        return
    
    try:
        score = float(grade_entry.get())
        weight = float(weight_entry.get())
        courses[course_name].append((assignment_name, score, weight))
        messagebox.showinfo("Success", f"Grade for '{assignment_name}' added to {course_name}.")
        open_next_page()
    except ValueError:
        messagebox.showerror("Error", "Enter valid numeric values for grade and weight.")

def calculate_required_final_grade():
    try:
        current_avg = float(current_avg_entry.get())
        final_weight = float(final_weight_entry.get())
        desired_grade = float(desired_grade_entry.get())

        if final_weight <= 0 or final_weight > 100:
            messagebox.showerror("Error", "Final weight must be between 1 and 100.")
            return

        required_final = ((desired_grade / 100) - ((1 - (final_weight / 100)) * (current_avg / 100))) / (final_weight / 100) * 100
        required_final = max(0, min(100, required_final)) 

        messagebox.showinfo("Final Grade Needed", f"You need {required_final:.2f}% on your final to achieve {desired_grade:.2f}%.")
    
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")



def show_all_assignments():
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Label(root, text="All Assignments & Marks", fg="white", bg="#0a192f", font=("Arial", 16)).pack(pady=20)
    
    for course, grades in courses.items():
        tk.Label(root, text=f"Course: {course}", fg="white", bg="#0a192f", font=("Arial", 14)).pack(pady=5)
        for assignment, score, weight in grades:
            tk.Label(root, text=f"{assignment} - Grade: {score}%, Weight: {weight}%", fg="white", bg="#0a192f", font=("Arial", 12)).pack()
    
    tk.Button(root, text="Back", command=open_next_page, bg="#ffaa00", fg="black", font=("Arial", 12)).pack(pady=20)


root = tk.Tk()
root.title("Grade Calculator")
root.geometry("800x700")
root.configure(bg="#0a192f")  

welcome_screen()
root.mainloop()