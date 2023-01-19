class Student : 
    def __init__(self, name, age, GPA) :
        self.name = name
        self.age = age
        self.GPA = GPA
    
    def get_name(self) :
        print(f'My name is {self.name}.')
    
    def get_age(self) :
        print(f"I am {self.age} years old.")

    def get_GPA(self) :
        print(f"I have a {self.GPA} GPA.")

# 위와 같은 경우, Person 클래스에서 사용했던 name과 age 속성, 그리고 get_name과 get_age 메소드를 중복해서 작성하고 있음.
# 만일, 다른 직업에 대한 클래스를 Person 클래스의 정보를 포함하여 새롭게 구현해야 하는 상황에도 같은 작업이 반복되는 것은 낭비.
# 따라서, 이와 같은 경우 중복된 속성과 메소드를 쉽게 포함시킬 수 있게 해주는 기능이 클래스의 상속.

class Student(Person):
    def __init__(self, name, age, GPA) :
        super().__init__(name,age)
        self.GPA = GPA
    
    def get_GPA(self) :
        print(f"I have a {self.GPA} GPA.")

# 클래스 선언 시, Student(Person)처럼 상속할 부모 클래스의 이름을 괄호 내에 적어주면 됨
# 초기화 단계에서 부모 클래스의 __init__ 메소드를 호출하는 원리로 진행됨
# 그리고, 부모 클래스에 전달할 input을 super().__init__() 내에 적어주면 됨

# 부모 클래스에서 구현했던 메소드를 호출하기(get_name을 자식 클래스에서 새롭게 구현했음에도, 부모 클래스에서 구현되었던 get_name을 호출해보는 경우)
class Student(Person) :
    def __init__(self, name, age, GPA) :
        super().__init__(name, age)
        self.GPA = GPA

    def get_name(self) :
        print(f"저는 대학생 {self.name}입니다.")
    
    def get_GPA(self) :
        super().get_name()
        print(f"제 학점은 {self.GPA}입니다.")

# get_GPA 함수 내에서 Student 클래스의 get_name이 아닌, Person 클래스의 get_name이 호출됨
# 부모 클래스의 메소드를 호출하는 경우, super().메소드이름 형태로 코드 작성할 것