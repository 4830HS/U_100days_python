#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Easy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
# 빈 숫자열로 시작하는 password 설정하기 위해 "" 사용.
# 만약 line 15 쓰지 않고 시작하면 'NameError : name 'password' is not defined' 에러 발생

for char in range(1, nr_letters+1) :
# 19 line : 만약 nr_letters가 3이면 range 안의 1,2,3 숫자를 가지고 for문 안을 돎.
# = for char in range(0, nr_letters)
# = for char in range(nr_letters) <- 0,1,2 => 어차피 숫자 3개를 가지고 for문 안을 돌기 때문
    random_char = random.choice(letters)
    password += random_char
    # 24 line : random_char가 각각 다른 줄로 출력되지 않도록
    # 23~24 line -> password += random.choice(letters)

for char in range(nr_symbols) :
    password += random.choice(symbols)

for char in range(nr_numbers) :
    password += random.choice(numbers)

print(password)