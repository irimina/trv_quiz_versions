# Functions Create ready


def greeting():
    
    print("Welcome to this trivia game that will test your knowledge on the black lives meatter movement")
    print(" ")
    name=input("enter your name: ")
    print("--------------")
    print("Hi there,",name, "Are you ready to start the quiz?")
    print("--------------")

    print("I will ask you 6 questions and give you four choices")
    print("Select which choice is the correct answer, A, B, C, or D")

def scoreFunction(score):
  print("--------------")
  print("Your current score is " +str(score)+" out of 6")
  final_score=(score*100)/6
  print("Percentage Score: " + str(final_score) + "%")
  print("--------------")

def thankyou():
        print("thank you for completing this quiz")
        User= input("Do you want to retake the quiz? y/n?: ")
        if User=="y":
             print("retake quiz")
             run()
        else:
             print("quiz is over")
        

greeting()      
#set the score of the quiz to 6
score = 0 
score = int(score)

#question 1
print("Question 1: how many times as likely are African Americans to be killed by police officers when unarmed compared to whites")

print("A. 3 times as likely")
print("B. 2 times as likely")
print("C. 10 times as likely")
print("D. 5 times as likely")

Q1answer="B"#the right answer to question
print(" ")
Q1response=input("Your answer: ")
print("_______")

if Q1response == "B" or Q1response == "b":
   print("Correct answer", Q1response)
   score = score+1
elif Q1response != "B" or Q1response != "b":
   print("Sorry, incorrect")

scoreFunction(score)


#question 2
print("Question 2: What percentage of people that are killed by police in an average year are African American")

print("A. 33.33%")
print("B. 25%")
print("C. 60.4%")
print("D. 20%")

Q2answer="A"#the right answer to question 2
Q2response=input("Your answer: ")
print("_______")

if Q2response == "A" or Q2response == "a":
   print("Correct answer", Q2response)
   score= score+1
elif Q2response != "A" or Q2response != "a":
   print("Sorry, incorrect")

scoreFunction(score)

#question 3
print("Question 3:In how many of the 100 largest U.S. cities did police kill black men at higher rates than the U.S. murder rate?")

print("A. 22")
print("B. 33")
print("C. 13")
print("D. 5")

Q3answer="C"#the right answer to question 3
Q3response=input("Your answer: ")
print("_______")

if Q3response == "C" or Q3response == "c":
   print("Correct answer", Q3response)
   score= score+1
elif Q3response != "C" or Q3response != "c":
   print("Sorry, incorrect")

scoreFunction(score)

#question 4

print("Question 4: In 2017 what percentage of African Americans killed by police were unarmed")

print("A. 9.2%")
print("B. 8.76%")
print("C. 5.02%")
print("D. 22.41%")


Q4answer="C"#the right answer to question 4
Q4response=input("Your answer: ")
print("_______")

if Q4response == "B" or Q4response == "b":
   print("Correct answer", Q4response)
   score= score+1
elif Q4response != "B" or Q4response != "b":
   print("Sorry, incorrect")

scoreFunction(score)

#Question 5

print("Question 5: What murder spurred the black lives matter movement")

print("A. Freddie Gray")
print("B. Eric Garner")
print("C. Michael Brown")
print("D. Trayvon Matin")

Q5answer="D"#the right answer to question 5
Q5response=input("Your answer: ")
print("_______")

if Q5response == "D" or Q5response == "d":
   print("Correct answer", Q5response)
   score= score+1
elif Q5response != "D" or Q5response != "d":
   print("Sorry, incorrect")

scoreFunction(score)   

#Question 6 

print("Question 6: Where was Eric Garner murdered by a police man")

print("A. Ferguson, Missouri")
print("B. Myrtle Beach, South Carolina")
print("C. Staten Island, New York City")
print ("D Detroit")

Q6answer="C"#the right answer to question 6
Q6response=input("Your answer: ")
print("_______")

if Q6response == "C" or Q6response == "c":
   print("Correct answer", Q6response)
   score= score+1
elif Q6response != "C" or Q6response != "c":
   print("Sorry, incorrect")

scoreFunction(score)
thankyou()
