import tkinter as tk
from tkinter import messagebox

def calculate_grade():
    try:
        # Get user inputs
        marks = entry_marks.get("1.0", tk.END).strip()
        if not marks:
            raise ValueError("Please enter marks for subjects.")
        
        marks_list = [float(mark) for mark in marks.split(",")]
        if any(mark < 0 or mark > 100 for mark in marks_list):
            raise ValueError("All marks must be between 0 and 100.")
        
        # Calculate total, average, and grade
        total_marks = sum(marks_list)
        num_subjects = len(marks_list)
        average_marks = total_marks / num_subjects

        if average_marks >= 75:
            grade = "Distinction"
        elif average_marks >= 60:
            grade = "First Class"
        elif average_marks >= 50:
            grade = "Second Class"
        elif average_marks >= 35:
            grade = "Pass"
        else:
            grade = "Fail"
        
        # Display result
        result_text.set(f"Total Marks: {total_marks}/{num_subjects * 100}\n"
                        f"Average Marks: {average_marks:.2f}\n"
                        f"Grade: {grade}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def clear_fields():
    entry_marks.delete("1.0", tk.END)
    result_text.set("")

# Create the main window
app = tk.Tk()
app.title("Student Grade Calculator")
app.geometry("400x400")

# Widgets
tk.Label(app, text="Enter marks for all subjects (comma-separated):", font=("Arial", 12)).pack(pady=10)
entry_marks = tk.Text(app, height=5, width=40)
entry_marks.pack(pady=10)

tk.Button(app, text="Calculate Grade", command=calculate_grade, bg="green", fg="white").pack(pady=10)
tk.Button(app, text="Clear", command=clear_fields, bg="red", fg="white").pack(pady=5)

result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text, font=("Arial", 12), fg="blue", justify="left")
result_label.pack(pady=20)

# Run the app
app.mainloop()
