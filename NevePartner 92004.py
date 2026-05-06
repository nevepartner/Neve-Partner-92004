'''Code gives a quiz on Lisa Carrington, one of New Zealand's sporting stars.
   By Neve Partner. Created on 22/04/2026'''

#Introducing the audience to the quiz
print("This is a quiz on Lisa Carrington, one of New Zealand's greatest sporting stars.")
print("The questions are all multi choice")

correct_answers = 0
total_questions = 10
minimum_value = 1
max_value = 4

#Creating the first five multi choice questions
print("Please input the number corresponding to the answer you think is correct.")
questions_and_answers = {"\nHow many Olympic Games has she competed in?\n1. 1\n2. 2\n3. 3\n"
              "4. 4" : 4,
              "\nWhich of these places did Lisa Carrington not win an Olympic" 
              "medal at?\n1. Tokyo\n2. Sydney\n3. Rio\n4. Paris" : 2,
              "\nWhat sport does Lisa Carrington compete in?\n1. Rowing\n2. "
              "Canoeing\n3. Kayaking\n4. Whitewater rafting" : 2,
              "\nWhen did she obtain the record for world's fastest K1 200m?\n"
              "1. 2010\n2. 2012\n3. 2014\n4. 2016" : 3,
              "\nHow many Olympic bronze medals has she won?\n1. 1\n2. 2\n3. 3\n"
              "4. 4" : 1,
              "\nWhat year was Lisa Carrington born?\n1. 1983\n2. 1985\n"
              "3. 1987\n4. 1989" : 4,
              "\nHow many Olympic medals has she won?\n1. 6\n2. 7\n3. 8\n4. 9"
              : 4,
              "\nWhat city was she born in?\n1. Aukland\n2. Tauranga\n3. Wellington\n"
              "4. Christchurch" : 2,
              "\nHow many World Championship gold medals has she won?\n1. 5\n"
              "2. 10\n3. 15\n4. 20" : 3,
              "\n When did she win her first Olympic gold medal?\n1. 2010\n2. 2012\n"
              "3. 2014\n4. 2016" : 2}

#Asking the user for the multi choice answers
for question, answer in questions_and_answers.items():
    print(question)
    #Seeing if answer is valid
    valid = False
    while valid == False:
        user_answer = input('Your answer: ')
        try:
            user_answer = int(user_answer)
            if user_answer < minimum_value:
                print('Please enter a number that corresponds to an answer')
            elif user_answer > max_value:
                print('Please enter a number that corresponds to an answer')
            else:
                valid = True
        except:
           print('Please enter an integer')
    #Seeing if the answer is correct
    if user_answer == answer:
        print('Correct!')
        correct_answers = correct_answers + 1
    else:
        print(f'Incorrect. The correct answer was {answer}.')

#Calculating users final score. I multiplied the score by 10 to get a percentage.
percentage_correct = correct_answers / total_questions
percentage_correct = percentage_correct * 100

#Printing a message to show user how they did
if correct_answers < 5:
    print(f"\nWell done! You got {correct_answers} correct. That's {percentage_correct}%")
elif correct_answers < 8:
    print(f"\nGreat job! You got {correct_answers} correct. That's {percentage_correct}%")
else:
    print(f"\nExcellent work! You got {correct_answers} correct. That's {percentage_correct}%")