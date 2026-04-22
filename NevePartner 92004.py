'''Code gives a quiz on Lisa Carrington, one of New Zealand's sporting stars. By Neve Partner.
Created on 22/04/2026'''

#Introducing the audience to the quiz
print("This is a quiz on Lisa Carrington, one of New Zealand's greatest sporting stars.")
print("The first five questions will be multi choice, and the last five will be user input.")

#Creating the first five multi choice questions
print('For the multi choice questions, please input the number corresponding to the answer you think is correct.')
multiquestion1 = input("Question one: Which of these places did Lisa Carrington not win an Olympic medal at?\n1. Tokyo\n2. Sydney\n3. Rio\n4. Paris\n")
multianswer1=2
multiquestion1 = input('What sport does Lisa Carrington compete in?\n1. Rowing\n2. Canoe Slalem\n )
# #Creating a dictionary with user input questions and answers
questions_answers = {'What year was Lisa Carrington born?' : 1989,
                     'What sport does Lisa Carrington compete in?' : 'kayaking',
                     'How many Olympic medals has she won?' : 9,
                     'What city was she born in?' : 'Tauranga',
                     'How many World Championship gold medals has she won?' : 15,
                     'How many Olympic bronze medals has she won?' : 1,}
