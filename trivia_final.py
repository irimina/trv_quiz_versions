import time

def intro():
    print("Welcome to the Crimminal Justice Trivia game!")
    name = input("What's your name?:")
    print("Hello", name)

    print(
        "Today you will be quized on your knowlege about crime and the law by answering a few questions.  Good Luck !"
    )
    print("---------------------------------")

def points(score):
  print("--------------")
  print("Your current score is " +str(score)+" out of 6")
  final_score=(score*100)/6
  print("Percentage Score: " + str(final_score) + "%")
  print("--------------")
  
  done=False
  while not done:
    if score==6:
      print("Perfect score")
    elif score <6 and score>=4:
      print("Great work")
    elif score<4:
      print("You should practice more")
    done=True



def question_answer():
    score = 0
    score = int(score)
    print(
        "Whats the name of the speech given to suspect once they've been arested? "
    )
    print("A: Innocene Speech")
    print("B: Arizona Law")
    print("C: Miranda Rights")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Q1answ = "C"
    Q1resp = input("Your Answer:")
  

    if Q1resp == "C" or Q1resp == "c":
        print("Correct")
        score = score+1
    else:
        print("Incorrect")
 
    points(score)
    print("------------------------------------")
    print("")
    print("")
    


    #Question 2
    print("Who is the head of the Justice Department?")
    print("A: Donald Trump")
    print("B: William Barr")
    print("C: Lorreta Lynch")
    print("D: Jeff Sessions")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Q2answ = "B"
    Q2resp = input("Your answer:")
    time.sleep(2)
    if Q2resp == "B" or Q2resp == "b":
        print("Correct")
        score=score+1
    else:
        print("Incorrect")
    points(score)

    print("----------------------")
    print("")
    print("")
   
    #Question 3
    print(
        "What clause prevents a defendant from being charged with the same crime twice? "
    )
    print("A: Double Jepordy")
    print("B: Fair Trial")
    print("C: Jury Duty")
    print("D: Speedy Trial ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Q3answ = "A"
    Q3resp = input("Your Answer:")
    time.sleep(2)
    if Q3resp == "A" or Q3resp == "a":
        print("Correct")
        score=score+1
    else:
        print("Incorrect")
    points(score)
    print("-------------------------")
    print("")
    print("")
    


    #Question 4
    print("What does I Plea the fifth mean ? ")
    print("A: I want a five minuet break.")
    print("B: I don't know the answer.")
    print("C: I want food.")
    print("D: I Invoke my right to Self-Incrimination.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Q4answ = "D"
    Q4resp = input("Your Answer:")
    time.sleep(2)
    if Q4resp == "D" or Q4resp == "d":
        print("Correct")
        score=score+1
    else:
        print("Incorrect")
    points(score)

    print("-------------------")
    print("")
    print("")
  
    #Question 5
    print("What is the longest running crime related televsion show?")
    print("A: Chicago PD")
    print("B: Crimminal Minds")
    print("C: Law & Order:Special Victums Unit")
    print("D: Bones")

    print("~~~~~~~~~~~~~~~~~~~~~~~")

    Q5resp = input("Your answer:")
    Q5asnw = "C"
    time.sleep(2)
    if Q5resp == "C" or Q5resp == "c":
        print("Correct")
        score=score+1
    else:
        print("Incorrect")
    points(score)
    time.sleep(2)
    print("")
    print("")
    


    #Question 6
    print("This is the last question.")
    time.sleep(3)
    print("How much money do jurours get paid in New York State? ")
    print("A: $80")
    print("B: $20 ")
    print("C: $40 ")
    print("D: $6")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Q6resp = input("Your Answer:")
    Q6answ = "C"
    time.sleep(2)
    if Q6resp == "C" or Q6resp == "c":
        print("Correct")
        score=score+1
    else:
        print("Incorrect")
    
    points(score)
    print("")
    print("")
    user = input("Do you wish to take the quiz again? y/n: ")
    while True:
         if user == "Y" or user == "y":
              question_answer()
         else:
              break
    
   

intro()
question_answer()
