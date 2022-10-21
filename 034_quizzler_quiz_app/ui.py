from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(width=400, height=400, bg=THEME_COLOR, padx=20, pady=20)

        self.frame = Frame(self.window, bg=THEME_COLOR, width=100, height=50)
        self.frame.grid(row=0, column=1, sticky="E")
        self.frame.grid_propagate(0)
        self.frame.update()
        self.label = Label(self.frame, fg="white", text=f"Score: {self.quiz.score}", bg=THEME_COLOR, font=("Arial", 10, "normal"))
        self.label.place(x=40, y=20, anchor="center")

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, width=275, text="test", font=("Arial", 15, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20, padx=5)

        green_check = PhotoImage(file="images/true.png")
        self.true_answer = Button(padx=50, pady=50, image=green_check, border=0, highlightthickness=0,
                                  command=self.is_true)
        self.true_answer.grid(column=0, row=2, pady=10, padx=5)

        red_x = PhotoImage(file="images/false.png")
        self.false_answer = Button(padx=100, pady=100, image=red_x, border=0, highlightthickness=0,
                                   command=self.is_false)
        self.false_answer.grid(column=1, row=2, pady=10, padx=5)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        self.canvas.itemconfig(self.question, fill="black")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz!")
            self.false_answer.config(state="disabled")
            self.true_answer.config(state="disabled")

    def is_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def is_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, yes_no):
        if yes_no:
            self.label.configure(text=f"Score: {self.quiz.score}")
            self.canvas.configure(bg="green")
            self.canvas.itemconfig(self.question, fill="white")
            self.window.after(1000,self.get_next_question)
        else:
            self.canvas.configure(bg="red")
            self.canvas.itemconfig(self.question, fill="white")
            self.window.after(1000, self.get_next_question)

