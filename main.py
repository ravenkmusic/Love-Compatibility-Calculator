# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

name1_score = (
  lower_name1.count('t') +
lower_name1.count('r') +
lower_name1.count('u') +
lower_name1.count('e') +
lower_name1.count('l') +
lower_name1.count('o') +
lower_name1.count('v'))

name2_score = (
lower_name2.count('t') +
lower_name2.count('r') +
lower_name2.count('u') +
lower_name2.count('e') +
lower_name2.count('l') +
lower_name2.count('o') +
lower_name2.count('v'))

old_score = str(name1_score) + str(name2_score)
new_score = int(old_score)

if new_score <= 10 or new_score >= 90:
  print(f"Your score is {new_score}, you go together like coke and mentos.")
if new_score >= 40 and new_score <= 50:
  print(f"Your score is {new_score}, you are alright together.")
else:
  print(f"Your score is {new_score}.")
