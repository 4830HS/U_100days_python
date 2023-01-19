import pandas

data = pandas.read_csv("Day25/2018_Central_Park_Squirrel_Census/2018_Central_Park_Squirrel_Censusa.csv")
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
# print(gray_squirrels)

# 만약 각각 다른 squirrels의 수를 알고 싶다면?
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

# 다음 step : dataframe 만들기 -> 딕셔너리 만들기
data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

# print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("Day25/2018_Central_Park_Squirrel_Census/squirrel_count.csv")