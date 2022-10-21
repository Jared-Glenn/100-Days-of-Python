#
# with open("weather_data.csv") as data:
#     data = data.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as data:
#     data = csv.reader(data)
#     temperatures = []
#     for row in data:
#         try:
#             temperatures.append(int(row[1]))
#         except:
#             continue
#
#     print(temperatures)

import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(data.info())

# data_dictionary = data.to_dict()
# print(data_dictionary)

# print(data[data["temp"] == data["temp"].max()])


# print((data.temp[data.day == "Monday"]) * 9 / 5 + 32)

data = pd.read_csv("Squirrel_Data.csv")
fur_color = data["Primary Fur Color"].value_counts()
fur_color.to_csv("Fur_Color.csv")

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()