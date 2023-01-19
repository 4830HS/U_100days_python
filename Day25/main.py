with open("Day25\weather_data.csv") as data_file :
    data = data_file.readlines()
    print(data)
# 위와 같은 작업은 각각의 행과 열을 추출할 수 있도록 하기 위한 정리 작업이 필요함.
# -> 파이썬은 실제로 데이터 처리와 데이터 분석에 아주 많이 사용되기 때문에 CSV를 지원하는 내장 라이브러리가 따로 있음.(날씨 데이터처럼 표의 형태로 된 데이터를 다루기 위한 도구들)


import csv
with open("Day25\weather_data.csv") as data_file :
    data = csv.reader(data_file)
    temperatures = []
    # print(data)
    # 결과값 : <_csv.reader object at 0x0000014BB71654C0>
    # 이 객체는 반복 가능함.
    # 따라서 이 data에 있는 각 행을 가져오고 싶다면,
    for row in data :
        # print(row)
        # 각 요소들은 하나의 값으로 분리됨.

        # temperatures= row[1]
        # print(temperatures)

            if row[1] != "temp" :
                temperatures.append(int(row[1]))
    print(temperatures)


import pandas

data = pandas.read_csv("Day25\weather_data.csv")
print(data)
print(data["temp"])

print(type(data))
# 결과값 : <class 'pandas.core.frame.DataFrame'> -> 표와 같은 형식

print(type(data["temp"]))
# 결과값 : <class 'pandas.core.series.Series'> -> 리스트와 같은 형식

# Pandas 활용법 : https://pandas.pydata.org/docs/reference/index.html

data_dict = data.to_dict()
print(data_dict)


# Get Data in Columns
temp_list = data["temp"].to_list()
print(temp_list)
# print(len(temp_list))

# 온도의 평균값 구하기 1
average = sum(temp_list) / len(temp_list)
print(average)

# 온도의 평균값 구하기 2
print(data["temp"].mean())

# 온도 series에서 가장 높은값 구하기
print(data["temp"].max())

# 다른 방식으로 series의 요소 중 하나를 출력하는 방법
print(data.condition)


# Get Data in Row
print(data[data.day == "Monday"])

# 가장 높은 온도가 있는 행은?(Print the row of data which had the highest temperature.)
print(data[data.temp == data.temp.max()])

# 조금 더 수월하게 작업하려면
monday = data[data.day == "Monday"]
print(monday.condition)

# Convert Monday's temperature to Fahrenheit(℉ = (℃ x 1.8) + 32)
print((monday.temp * 1.8) + 32)


# Create a dataframe from scratch
data_dict = {
    "students" : ["Alex", "Jenny", "Connie"],
    "scores" : [83, 24, 96]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("Day25/new_data.csv")