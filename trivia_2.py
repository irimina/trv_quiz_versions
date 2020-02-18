# MORE STATS

# Trivia Quiz starter

print ('This is a quiz that tests your knowledge of world geography\n')
name = input('Enter your name: ')
print ('\nHi There ' + name + '! Are you ready? \n')
print ('I will ask you 10 questions and give you three choices for each question.\n\nYou select which choice is the correct answer: A, B or C')
print ('-----------------------------------------------------------\n-----------------------------------------------------------')

# set the quiz score to 0
score = 0
score = int(score)  #Convert the 0 into a number so we can add scores

# question 1
print ('QUESTION 1: WHAT IS THE LARGEST OCEAN IN THE WORLD?\n')
print ('A. The Indian Ocean')
print ('B. The Pacific Ocean')
print ('C. The Atlantic Ocean')
print ('')

Q1answer ='B'         # the right answer to question 1 
Q1response= input('Your answer: ')  

if Q1response == 'B' or Q1response =='b':
    print('Well done ' + Q1response + ' is correct!')
    score = score +1
    
elif Q1response != 'B' or Q1response != 'b': 
    print ('Sorry, that is incorrect!')
    
print ('Your current score is ' + str(score) + ' out of 10')
print ('-----------------------------------------------------------\n-----------------------------------------------------------')

# question 2 

print ('QUESTION 2: AUSTRALIA IS A ...\n')
print ('A. continent')
print ('B. island')
print ('C. very hot place')
print ('')

Q2answer = "A"
Q2response= input('Your answer : ')

if Q2response == 'A' or Q2response =='a':
    print('Well done ' + Q2response + ' is correct!')
    score = score +1
    
elif Q2response != 'A' or Q2response != 'a': 
    print ('Sorry, that is incorrect!')
    

print ('Your current score is ' + str(score) + ' out of 10')

# more stats
final_score = (score * 100)/10
# if you want the percentage
print('This is a score of ' + str(final_score) + ' percent')
print ('-----------------------------------------------------------\n-----------------------------------------------------------')


# continue in the same format to produce a quiz of 10 questions
# In the end include a message with TOTAL score
