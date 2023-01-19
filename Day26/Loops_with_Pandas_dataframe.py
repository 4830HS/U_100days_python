student_dict = {
    "student" : ["Alex","James","Laura"],
    "score" : [56,92,24]
}

# for (key, value) in student_dict.items() :
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a data frame(데이터 프레임을 반복 실행하기)
for (key, value) in student_data_frame.items() :
    print(value)

for (index, row) in student_data_frame.iterrows() :
    print(row.student)

    if row.student == "Alex" :
        print(row.score)