
class Quiz():
    def __init__(self , question , answer , score):
        self.question = question
        self.answer = answer
        self.score = score

    def ask_question(self):
        print(question)

    def check_the_answer(self):
        if user_answer == question_and_answer["question_1"]:
            print("Верный ответ!")
            self.score += 1

    def get_score(self ):
        print(self.score)

question = "1. Начало второй мировой войны ? "

question_and_answer = {
    "question_1" : 1939,
    "question_2" : 4 ,
    "question_3" : 5,
    "question_4" : "question"
    
}


question_1 = Quiz("Начало Второй Мировой Войны ?" , 1939 , 0 )
question_2 = Quiz("два плюс два ?", 4 , 0 )
question_3 = Quiz("корень из 25 ? ", 5, 0 )
question_4 = Quiz("английский перевод слова вопрос ? " , "question" , 0)
question_1.ask_question()
user_answer = input("Введите ваш ответ:")
question_1.check_the_answer()
question_1.get_score()