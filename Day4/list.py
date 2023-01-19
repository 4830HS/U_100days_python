# List = Data structure
# ex : fruits = [item1, item2]

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"]

print(states_of_america[0])

print(states_of_america[-2])

# List 안의 철자를 바꾸고 싶을때?
states_of_america[1] = "Penn"
print(states_of_america[1])

print(states_of_america)

# List 안에 항목 추가하고 싶을때?
states_of_america.append("Alexland")
print(states_of_america)

# List 안에 여러가지 항목을 추가하고 싶을때?
states_of_america.extend(["Legoland","Turtleland"])
print(states_of_america)

# Data Structures : https://docs.python.org/3/tutorial/datastructures.html