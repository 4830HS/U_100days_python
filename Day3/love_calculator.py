# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# 
# name = name1.lower() + name2.lower()
# 
# true = name.count("t") + name.count("r") + name.count("u") + name.count("e")
# love = name.count("l") + name.count("o") + name.count("v") + name.count("e")
# 
# ttrue_love = str(true) + str(love)
# 
# true_love = int(ttrue_love)
# 
# if true_love < 10 or true_love > 90 :
#     print(f"Your score is {true_love}, you go together like coke and mentos.")
#     
# elif 40 < true_love < 50 :
#     print(f"Your score is {true_love}, you are alright together.")
#     
# else :
#     print(f"Your score is {true_love}.")
    
    
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score) > 90 :
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif (40 <= love_score <= 50) :
    print(f"Your score is {love_score}, you are alright together.")
else :
    print(f"Your score is {love_score}.")
    
    