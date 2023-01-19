# file = open("Day24\with_keyword.py\my_file.txt")
# # read 메소드는 파일의 컨텐츠를 문자열로 반환해 줌
# contents = file.read()
# print(contents)

# # 파일을 open한 뒤에 close 해줘야 함 <- ∵ 파이썬이 파일을 열면, 기본적으로 컴퓨터의 자원을 차지하게 됨
# file.close()

# # 하지만, 매번 이렇게 close 해줄 수 있는 것은 아님 => ∴ with 키워드 사용
# with open("Day24\with_keyword.py\my_file.txt") as f :
#     contents = f.read()
#     print(contents)
# # 구성요소 f는 다른 이름으로 지정 가능

# # 만약 file을 'read'하는 것이 아니라, 'write' 하고 싶다면? -> mode = "w"를 추가하여 읽기모드를 쓰기모드로 변경해야 함
# # 파일 이름.write()의 괄호 안에 변경하고 싶은 내용을 추가하면 됨
# with open("Day24\with_keyword.py\my_file.txt", mode = "w") as file :
#     file.write("ALLO?")

# # 만약 file을 'write'하는 것이 아니라, 'add' 하고 싶다면? -> mode = "a"로 변경(append)
# with open("Day24\with_keyword.py\my_file.txt", mode = "a") as file :
#     file.write("\nWho are you?")

# 만약 file 자체를 처음부터 만들려면? (중요한 점! 이것은 "write mode" & 만들려는 파일이 존재하지 않을 때에만 가능)
with open("Day24\with_keyword.py\my_file2.txt", mode = "w") as file :
    file.write("I love my dog.")