student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
# student_grades["Harry"] = 81
# student_grades["Ron"] = 78
# student_grades["Hermione"] = 99
# student_grades["Draco"] = 74
# student_grades["Neville"] = 62

# student_grades={"Harry":81, "Ron":78, "Hermione":99, "Draco":74, "Neville":62}

# for student in student_grades :
#   answer = student_grades[student]
#   if 91 <= answer <= 100 :
#     student_grades[student] = "Outstanding"
#   elif 81 <= answer <= 90 :
#     student_grades[student] = "Exceeds Expectations"
#   elif 71 <= answer <= 80 :
#     student_grades[student] = "Acceptable"
#   elif answer <= 70 :
#     student_grades[student] = "Fail"

for student in student_scores :
  score = student_scores[student]
  if score > 90 :
    student_grades[student] = "Outstanding"
  elif score > 80 :
    student_grades[student] = "Exceeds Expectations"
  elif score > 70 :
    student_grades[student] = "Acceptable"
  else : 
    student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)