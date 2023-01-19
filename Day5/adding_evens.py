# even_number = 0
# for number in range(2,101,2) :
#     even_number += number
# print(even_number)

total = 0
for number in range(2,101,2) :
    total += number
print(total)

# or

total2 = 0
for number in range(1, 101) :
    if number % 2 == 0 :
        total2 += number
print(total2)