class QuizBrain:
    def __init__(self,q_list):
        self.qustion_number=0
        self.qustion_list=q_list
        self.score=0


    def still_has_qustion(self):
        if self.qustion_number <= len(self.qustion_list)-1:
            return True
        else: return False

    def nextQustion(self):
        currentQustion = self.qustion_list[self.qustion_number]
        self.qustion_number +=1
        userAns=input(f"Q{self.qustion_number}: {currentQustion.Q_Text} (True/False):")
        self.check_answer(userAns,currentQustion.Answer)

    def check_answer(self,userAns,orginal_ans):
        if userAns.lower()==orginal_ans.lower():
            self.score+=1
            print(f"You got it right!\nThe correct answer was: {orginal_ans}."
                  f"\nYour current score is: {self.score}/{self.qustion_number}")
        else:
            print(f"That's wrong.!\nThe correct answer was: {orginal_ans}."
                  f"\nYour current score is: {self.score}/{self.qustion_number}")

        print("\n")
