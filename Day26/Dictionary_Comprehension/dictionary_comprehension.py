# Dictionary Comprehension

# new_dict = {new_key:new_value for item in list}
# list 자리에는 반복할 수 있는 종류의 것이라면 어떤 것이든 사용 가능.
# (list, range, string...)

# 또는, 이미 존재하는 dictionary에 있는 값을 가지고 새로운 dictionary를 만들 수도 있음.
# new_dict = {new_key:new_value for (key,value) in dict.items()}

# Conditional Dictionary Comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

names = ["Alex","Beth","Caroline","Dobby","Elizabeth","Forbie"]

# Original way
# student_score = {
#     "Alex" : 89,
#     "Beth" : 98, ...
# }

import random
students_scores = {student:random.randint(1,100) for student in names}
# print(students_scores)

passed_students = {
    student:score
    for (student,score) in students_scores.items() if score >= 60
}

print(passed_students)