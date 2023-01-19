# Functions with Outputs

def format_name(f_name, l_name) :
    print(f_name.title())
    print(l_name.title())

format_name("aLEx", "bLACK")

# or

def format_name(f_name, l_name) :
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    print(f"{formated_f_name} {formated_l_name}")

format_name("alex", "BLack")

#  or

def format_name(f_name, l_name) :
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("AlEx", "BLack"))

# 함수가 하나 이상의 리턴문을 가진 경우?
# - 컴퓨터은 return문을 만났을 때, 그 줄을 함수의 마지막으로 인식.
# (따라서 return 다음에 명령을 추가하여도 return까지만 실행. return이 컴퓨터에게 함수의 마지막 부분이라서 함수를 종료해야 하는 것으로 인지)
# - 실제로 같은 함수 내부에 return 키워드를 여러 개 가질 수 있음.(심지어 빈 return 키워드도 가능)
def format_name(f_name, l_name) :
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))
