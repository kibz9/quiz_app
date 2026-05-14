class Question:
    def __init__(self, question, correct_answer, explanation):
        self.question = question
        self.correct_answer = correct_answer
        self.explanation = explanation

    def check_answer(self, user_answer):
        """Returns True if user's answer is correct"""
        return user_answer == self.correct_answer

    def __repr__(self):
        return f"Question('{self.question[:40]}...')"