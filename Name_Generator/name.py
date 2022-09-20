import random
  
# Open the file in read mode
with open("Name_Generator/firstName.txt", "r") as fn:
    firstName = fn.read()
    first = list(map(str, firstName.split()))
    f = random.choice(first)
  
with open("Name_Generator/lastName.txt", "r") as ln:
    lastName = ln.read()
    last = list(map(str, lastName.split()))
    l = random.choice(last)


print("Generating First Name... ", f)
print("Generating Last Name... ", l)
print(f + " " + l)