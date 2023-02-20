from data import question_data
from question_model import Qustion
from quiz_brain import QuizBrain

QustionBank = []


for singleQustion in question_data:

    q_text = singleQustion["text"]
    ans = singleQustion["answer"]
    obj_qustion = Qustion(q_text,ans)
    QustionBank.append(obj_qustion)
quiz=QuizBrain(QustionBank)

while quiz.still_has_qustion():
    quiz.nextQustion()

print("Your Quiz is compliteed!")
print(f"Your final Score is: {quiz.score}/{quiz.qustion_number}")