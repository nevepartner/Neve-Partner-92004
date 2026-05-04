'''Code gives a quiz on Lisa Carrington, one of New Zealand's sporting stars. By Neve Partner.
Created on 22/04/2026'''

#Introducing the audience to the quiz
print("This is a quiz on Lisa Carrington, one of New Zealand's greatest sporting stars.")
print("The first five questions will be multi choice, and the last five will be user input.\n")

correct_answers = 0
total_questions = 10

#Creating the first five multi choice questions
print('For the multi choice questions, please input the number corresponding to the answer you think is correct.')
multiQandA = {"\nHow many Olympic Games has she competed in?\n1. 1\n2. 2\n3. 3\n4. 4" : 4,
              "\nWhich of these places did Lisa Carrington not win an Olympic medal at?\n1. Tokyo\n2. Sydney\n3. Rio\n4. Paris" : 2,
              "\nWhat sport does Lisa Carrington compete in?\n1. Rowing\n2. Canoeing\n3. Kayaking\n4. Whitewater rafting" : 2,
              "\nWhen did she obtain the record for world's fastest K1 200m?\n1. 2010\n2.2012\n3. 2014\n4. 2016" : 3,
              "\nHow many Olympic bronze medals has she won?\n1. 1\n2. 2\n3. 3\n4. 4" : 1}

#Asking the user for the multi choice answers
for question, answer in multiQandA.items():
    #Seeing if answer is valid
    print(question)
    valid = False
    while valid == False:
        multi_answer = input('Your answer: ')
        try:
            multi_answer = int(multi_answer)
            if multi_answer < 1:
                print('Please enter a number that corresponds to an answer')
            elif multi_answer > 4:
                print('Please enter a number that corresponds to an answer')
            else:
                valid = True
        except:
           print('Please enter an integer')
    #Seeing if the answer is correct
    if multi_answer == answer:
        print('Correct!')
        correct_answers = correct_answers + 1
    else:
        print(f'Incorrect. The correct answer was {answer}.')

# #Creating a dictionary with user input questions and answers
questions_answers = {"What year was Lisa Carrington born?" : 1989,
                     "How many Olympic medals has she won?" : 9,
                     "What city was she born in?" : "Tauranga",
                     "How many World Championship gold medals has she won?" : 15,
                     "She is nicknamed the '____ in the boat'" : "GOAT"}
