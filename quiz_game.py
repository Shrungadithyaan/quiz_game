print("Quiz game")

yes_or_no = input("Do you want to play game? ")

score = 0
if yes_or_no.lower() != "yes":
    quit()

answer = input("CPU stands for? ")

if answer.lower() == "central processing unit":
    print("correct")
    score += 1
else :
    print("incorrect")

answer = input("RAM stands for? ")

if answer.lower() == "random access memory":
    print("correct")
    score += 1
else :
    print("incorrect")

answer = input("GPU stands for? ")

if answer.lower() == "graphics processing unit":
    print("correct")
    score += 1
else :
    print("incorrect")

answer = input("PSU stands for? ")

if answer.lower() == "power supply":
    print("correct")
    score += 1
else :
    print("incorrect")

print("you got " + str(score) + " question correct!")
print("you got " + str((score / 4)*100) + "%.")