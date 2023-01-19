# year = int(input("Which year do you want to check? "))
# 
# if year % 4 == 0 :
#     if year % 100 != 0 :
#         print("Leap year.")
#     elif year % 100 == 0 :
#         print("Not leap year.")
#         if year % 400 == 0 :
#             print("Leap year.")
#         elif year % 400 != 0 :
#             print("Not leap year.")
# else :
#     print("Not leap year.")


# while True :
#     try :
#         year = int(input("Which year do you want to check? "))
#     except ValueError :
#         print("Number! 바보야ㅋㅋㅋㅋ")
#     else :
#         if year % 4 == 0 :
#             if year % 100 != 0 :
#                 print("Leap year.")
#                 break
#             elif year % 100 == 0 :
#                 print("Not leap year.")
#                 break
#                 if year % 400 == 0 :
#                     print("Leap year.")
#                     break
#                 elif year % 400 != 0 :
#                     print("Not leap year.")
#                     break
#         else :
#             print("Not leap year.")
#             break

# year = int(input("Which year do you want to check? "))
# 
# if year % 4 == 0 :
#   if year % 100 == 0 :
#     if year % 400 == 0 :
#         print("Leap year")
#     else :
#         print("Not leap year")
#   else :
#       print("Leap year")
# else :
#     print("Not leap year")

while True :
    try :
        year = int(input("Which year do you want to check? "))
    except ValueError :
        print("Number! Try again.")
    else :
        if year % 4 == 0 :
            if year % 100 == 0 :
                if year % 400 == 0 :
                    print("Leap year")
                    break
                else :
                    print("Not leap year")
                    break
            else :
                print("Leap year")
                break
        else :
            print("Not leap year")
            break
    