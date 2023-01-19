# Treasure Map
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

# row1 = map[0]
# row2 = map[1]
# row3 = map[2]

# print(map[vertical -1])

selected_row = map[vertical -1]
selected_row[horizontal -1] = "X"

# or : map[vertical -1][horizontal -1] = "X"

print(f"{row1}\n{row2}\n{row3}")