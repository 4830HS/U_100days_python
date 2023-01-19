# List Comprehensions

# Previous method : For Loop
# numbers = [1,2,3]
# new_list = []
# for n in numbers :
    # add_1 = n+1
    # new_list.append(add_1)

# New method : List Comprehension
# numbers = [1,2,3]
# new_list = [new_list for item in list]
# -> [n+1 for n in numbers]

# Challenge : Create a new list for numbers, where you added 1 to each value
numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]

print(new_numbers)

# 반드시 list로만 작업할 수 있는 것은 아님. 다른 시퀀스로도 작업가능.(ex : 문자열)

# Challenge : Predict what new_list will contain. Check your prediction in PyCharm.
name = "Alex"
# new_list = [letter for letter in name]
letters_list = [letter for letter in name]
print(letters_list)

# Python Sequences : list, range, string, tuple <- 명확하게 순서를 갖고 있음. 그래서 List Comprehension을 사용할 때 문자열에 있는 문자나 리스트에 있는 요소들은 시퀀스를 써서 순서대로 통과하게 됨. 그런 다음, 정확한 순서로 각각의 요소를 취하고 그 요소에 대해 뭔가를 함.

# Challenge : Create a new list from a range, where the list items are double the values in the range. -> range(1,5) => 2,4,6,8

# My answer
# ranges = [i+i for i in range(1,5)]
# print(ranges)

range_list = [num*2 for num in range(1,5)]
print(range_list)

# Conditional List Comprehension : 조건이 포함된 리스트 컴프리헨션
# new_list = [new_item for item in list if test]
names = ["Alex","Beth","Caroline","Dave","Freddie","Black","Pauly"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

# Challenge : Create a new list that contains the names longer than 5 characters in ALL CAPS.

# My answer
cap_names = [name.upper() for name in names if len(name) > 5]
print(cap_names)