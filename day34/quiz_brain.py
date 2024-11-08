import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        # Unescape HTML characters in the question text
        return f"Q.{self.question_number}: {html.unescape(current_question.text)} (True/False)?"

    def check_answer(self, user_answer):
        correct_answer = self.question_list[self.question_number - 1].answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def reset(self):
        self.question_number = 0
        self.score = 0
