#Create a quiz app
correctAnswer = 0
wrongAnswer = 0
print("This is a simple quiz." + " Please type the option, so that there is no error.")
print("Thank You and Good Luck")
print(" ")
print("1. Which animal is known as the 'Ship of the Desert?")
print(" a. Camel" + " b. Dog " + " c. Cow " + " d. Horse ")
answer1 = input("Type your answer: ").lower()

if (answer1 == "camel"):
  print("Correct Answer")
  correctAnswer  += 1
else:
  print("Wrong Answer")
  wrongAnswer += 1

print(" ")

print("2. How many days are there in a week?")
print(" a. 7 days " + " b. 8 days " + " c. 2 days " + " d. 10 days")
answer2 = input("Type your answer: ").lower()

if (answer2 == "7 days"):
  print("Correct Answer")
  correctAnswer  += 1
else:
  print("Wrong Answer")
  wrongAnswer += 1

print(" ")

print("3. How many hours are there in a day?")
print(" a. 34 Hours " + " b. 24 Hours " + " c. 48 Hours " + " d. 52 Hours ")
answer3 = input("Type Your Answer: ").lower()

if (answer3 == "24 Hours" or "24 hours"):
  print("Correct Answer")
  correctAnswer  += 1
else:
  print("Wrong Answer")
  wrongAnswer += 1

print(" ")

print("4. How many letters are there in the English alphabet?")
print(" a. 67 letters " + " b. 29 letters " + " c. 26 letters " + " d. 34 letters ")
answer4 = input("Type Your Answer: ").lower()

if (answer4 == "26 letters"):
  print("Correct Answer")
  correctAnswer  += 1
else:
  print("Wrong Answer")
  wrongAnswer += 1

print(" ")

print("5. Rainbow consist of how many colours?")
print(" a. 9 colors " + " b. 7 colors " + " c. 10 colors " + " d. 23 colors ")
answer5 = input("Type Your Answer: ").lower()

if (answer5 == "7 colors"):
  print("Correct Answer")
  correctAnswer  += 1
else:
  print("Wrong Answer")
  wrongAnswer += 1

print(" ")

print("Correct Answers " + str(correctAnswer))
print("Wrong Answers " + str(wrongAnswer))

if (correctAnswer == 5):
  print("You are a Genius!!")
else:
  print("You need to study More")
  