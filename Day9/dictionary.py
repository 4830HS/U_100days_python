programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# dictionary 안의 값을 불러오고 싶을 때?
print(programming_dictionary["Bug"])

# adding new items to dictionary
programming_dictionary["Loop"] = "The actions of doing something over and over again."
print(programming_dictionary)

# 코드를 작성할 때, 빈 dictionary를 먼저 선언하고 시작하는 것이 도움이 될 때가 있음.
empty_dictionary = {}
empty_dictionary["Key1"] = "Value1"

# dictionary를 통째로 지우고 싶을 때?(wipe an existing dictionary)
programming_dictionary = {}
print(programming_dictionary)

#  dictionary 안의 값을 수정하고 싶을 때?(edit an item in a dictionry)
Hey_dictionary = {"k1":"a1", "k2":"a2", "k3":"a3"}
Hey_dictionary["k1"] = "a111"
print(Hey_dictionary)

# dictionary 이용하여 반복문 사용하고 싶을 때?(loop through a dictionary)
for thing in Hey_dictionary :
    print(thing)
    print(Hey_dictionary[thing])