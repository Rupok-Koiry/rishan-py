from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler by RISHAN")
        self.window.config(padx=200, pady=200, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        # Start with the instruction screen
        self.show_instruction()

        self.window.mainloop()

    def show_instruction(self):
        self.canvas.itemconfig(
            self.question_text,
            text="Welcome to the RISHAN Quiz!\n\nPress 'Start Quiz' to begin."
        )
        self.start_button = Button(
            text="Start Quiz", command=self.start_quiz, bg="green", fg="white", font=("Arial", 16, "bold"))
        self.start_button.grid(row=3, column=0, columnspan=2, pady=20)

    def start_quiz(self):
        self.start_button.grid_forget()  # Hide start button
        self.get_next_question()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.show_restart_button()

    def show_restart_button(self):
        self.restart_button = Button(
            text="Restart Quiz", command=self.restart_quiz, bg="blue", fg="white", font=("Arial", 16, "bold"))
        self.restart_button.grid(row=3, column=0, columnspan=2, pady=20)

    def restart_quiz(self):
        self.quiz.reset()  # Assuming you have a reset method in QuizBrain
        self.true_button.config(state="active")
        self.false_button.config(state="active")
        self.restart_button.grid_forget()
        self.get_next_question()

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def restart_quiz(self):
        self.quiz.reset()  # Reset the quiz data
        self.true_button.config(state="active")
        self.false_button.config(state="active")
        self.restart_button.grid_forget()
        self.get_next_question()
