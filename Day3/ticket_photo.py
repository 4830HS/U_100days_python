print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120 :
    print("You can ride the rollercoaster.")
    age = int(input("What is your age?\n"))
    if age < 12 :
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18 : 
        bill = 7
        print("Youth tickets are $7.")
    else :
        bill = 12
        print("Adult tickets are $12.")
              
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y" :
#         bill = bill + 3
          bill += 3
#   else : 는 작성하지 않아도 ok.
    
#   print를 if 다음 indentation 하고 쓰지 않아도 되는 이유? 각각 다른 명령. if 실행 후, print 실행. separately.
    print(f"Your final bill is ${bill}.")
        
else :
    print("Sorry. You have to grow taller before you can ride.")