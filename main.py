# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

name1_score = int(
lower_name1.count('t') +
lower_name1.count('r') +
lower_name1.count('u') +
lower_name1.count('e') +
lower_name1.count('l') +
lower_name1.count('o') +
lower_name1.count('v'))

print(name1_score)

name2_score = int(
lower_name2.count('t') +
lower_name2.count('r') +
lower_name2.count('u') +
lower_name2.count('e') +
lower_name2.count('l') +
lower_name2.count('o') +
lower_name2.count('v'))

print(name2_score)

score = (name1_score + name2_score)

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
if score >= 40 and score < 50:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif:
  print(f"Your score is {score}.")
