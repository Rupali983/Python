#18/6/24
#kbc gam
prize_money = 0
questions = [{
   "question": "When is the National Hindi Diwas celebrated?",
   "options": ["1. 13September", "2. 14September", "3. 14July", "4. 15Agust"],
   "answer": 2
},{
   "question": "How many states are there in India?",
   "options": ["1. 28", "2. 29", "3. 31", "4. 31"],
   "answer": 1
},{
   "question": "Where in India Gate located?",
   "options": ["1. Agra", "2. Punjab", "3. Mumbai", "4. New Delhi"],
   "answer": 4
},
{
   "question": "Who was the first Indian woman to win a medal in the Olympics?",
   "options": ["1. P.T Usha", "2. Kunjarani devi", "3. Bachedri pal", "4. Karnam Maleshwari"],
   "answer": 4
},
{
   "question": "Which of the following is not a state of India?",
   "options": ["1.Varindachal", "2. Goa", "3. Jharkhand", "4. Chhatisgra"],
   "answer": 1
}]


question_index = 0
game_over = False

while not game_over:

   question = questions[question_index]
    
   
   print(question["question"])
   for option in question["options"]:
      print(option)
    
   
   user_answer = int(input("Enter your answer (option number): "))
    
   
   if user_answer == question["answer"]:
      print("Correct answer!")
      prize_money += 1000
   else:
      print("Wrong answer!")
      game_over = True  
    
   
   question_index += 1
    
   
   if question_index == len(questions):
      game_over = True


print("Prize Money:", prize_money)
