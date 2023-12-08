import tkinter as tk
from grades import GradeCalculator
from data_handling import DataHandler

class GradeApp(tk.Tk):
    """GUI application for grade calculation."""

    def __init__(self):
        super().__init__()
        self.title("Grade Calculator")
        self.geometry("400x300")
        self.grade_calculator = GradeCalculator()
        self.data_handler = DataHandler()
        self.create_widgets()

    def create_widgets(self):
        # Create GUI components here
        self.label = tk.Label(self, text="Enter Score:")
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.calculate_grade)
        self.submit_button.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def calculate_grade(self):
        score = int(self.entry.get())
        best = 100  # Assuming best score is 100
        grade = self.grade_calculator.determine_grade(score, best)
        self.result_label.config(text=f"Grade: {grade}")

app = GradeApp()
app.mainloop()
