print("WELCOME TO MY COMPUTER QUIZ GAME! ")
playing=input("DO you want to paly? ")

if playing.lower() != "yes":
    quit()

print("Ohh Great Let's Play :) ")
score=0
print("\n")
print("*" * 70)


answer= input("Who is the prime minister of INDIA ? ")
if answer.lower()=="narendra modi":
    print("Correct answer..")
    score +=1
else:
    print("ohh that is wrong answer...! ")
print("\n")
print("*" * 70)




answer= input("Who is the RAM Stands for? ")
if answer.lower()=="random access memory":
    print("Correct answer..")
    score+=1
else:
    print("ohh that is wrong answer...! ")
print("\n")
print("*" * 70)



answer= input("What is the captial of INDIA? ")
if answer.lower()=="delhi":
    print("Correct answer..")
    score+=1

else:
    print("ohh that is wrong answer...! ")
print("\n")
print("*" * 70)


answer= input("Who is the National game of INDIA? ")
if answer.lower()=="hockey":
    print("Correct answer..")
    score+=1
else:
    print("ohh that is wrong answer...! ")
print("\n")
print("*" * 70)



answer= input("Who is the full form of MCA? ")
if answer.lower()=="master of computer application":
    print("Correct answer..")
    score+=1
else:
    print("ohh that is wrong answer...! ")
print("\n")
print("*" * 70)

print("You got " + str(score) + " questions correct! ")
