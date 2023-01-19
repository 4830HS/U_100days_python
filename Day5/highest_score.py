student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# 78 65 89 86 55 91 64 89

highest_score = 0
for score in student_scores :
  if score > highest_score : 
    highest_score = score
print(f"The highest score in the class is : {highest_score}")

# Line 10~11
# [78, 65, 89, 86, 55, 91, 64, 89]
# 78 > 0 -> 78
# 65 > 78 -> 78 (False)
# 89 > 78 -> 89
# 86 > 89 -> 89 (False)
# 55 > 89 -> 89 (False)
# 91 > 89 -> 91
# 64 > 91 -> 91 (False)
# 89 > 91 -> 91 (False)
# => 91