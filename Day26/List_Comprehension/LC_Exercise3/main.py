# My answer
# with open(r"Day26/Exercise3/file1.txt") as file_1 :
#     f1 = file_1.read().split()

# with open(r"Day26/Exercise3/file2.txt") as file_2 :
#     f2 = file_2.read().split()

# result = [int(num) for num in f1 if num in f2]

# # Write your code above 👆

# print(result)

# Angela's answer
with open(r"Day26/Exercise3/file1.txt") as file_1 :
    f1 = file_1.readlines()

with open(r"Day26/Exercise3/file2.txt") as file_2 :
    f2 = file_2.readlines()

result = [int(num) for num in f1 if num in f2]

# Write your code above 👆

print(result)