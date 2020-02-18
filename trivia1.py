
# Trivia Quiz

print("This is a quiz that tests your knowledge of geography")
name = input('Enter your name: ')

print('\nHi there', name + ' Are you ready to take this quiz?\n')
print('I will ask you you 10 questions and give you three choices for each question')
print('Select the right choice by pressing A, B or C')

print("------------------------------------------------------------------------------")

# set quiz score to 0

score = 0
score = int(score) # convert 0 into a number so we can add scores


# question 1

print('QUESTION 1: What is the largest ocean in the world?')
print("A. The Indian Ocean")
print("B. The Atlantic Ocean")
print("C. The Pacific Ocean")
print('')

Q1answer = 'C'  # right answer to question 1
Q1response = input('Your answer: ')

if Q1response =="C" or Q1response == 'c':
    print('Well done ' + Q1response + ' is correct!')
    score = score +1
else:
    print('Sorry, that is incorrect!')

print('Your current score is ' + str(score) + ' out of 10')
    
    


























