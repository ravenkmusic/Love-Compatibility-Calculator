# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

name1_score = int(
name1.count('t') +
name1.count('r') +
name1.count('u') +
name1.count('e') +
name1.count('l') +
name1.count('o') +
name1.count('v') +
name1.count('e'))

print(name1_score)

name2_score = int(
name2.count('t') +
name2.count('r') +
name2.count('u') +
name2.count('e') +
name2.count('l') +
name2.count('o') +
name2.count('v') +
name2.count('e'))

print(name2_score)

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
if score >= 40 and score < 50:
  print(f"Your score is {score}, you go together like coke and mentos.")
else:
  print(f"Your score is {score}.")
