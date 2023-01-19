# *args: Positional Variable-Length Arguments

# 만약 더 많은 숫자를 더하고 싶다면? function을 바꾸지 않고도 계속 더하도록 만들고 싶다면? -> '아스테리스크' 사용(함수 add가 몇 개의 인수라도 허용한다는 것을 의미)
# def add(*args) :
    # for n in args :
        # print(n)

# Challenge : Modify the add function to take an unlimited number of arguments. Use a loop to sum all the arguments inside the function. Test it out by calling add() to calculate sum of some arguments.

def add(*args) :
    
    print(args[0])

    total = 0
    for n in args :
        total += n
    return total

print(add(23,444,5563,3,2433456784))



# **kwargs: Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)


calculate(2, add=3, multiply=5)


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)