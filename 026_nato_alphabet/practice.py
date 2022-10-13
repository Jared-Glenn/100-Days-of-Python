# new_list = [new_item for item in list]

# new_list = [n + 1 for n in numbers]

# new_list = [new_item for item in list if test]

# with open("file1.txt") as f1:
#   with open("file2.txt") as f2:
#     lst1 = [int(num.strip()) for num in f1.readlines()]
#     lst2 = [int(num.strip()) for num in f2.readlines()]
#
# result = [num for num in lst1 if num in lst2]
#
# # Write your code above 👆
#
# print(result)

# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
#
# # Write your code 👇 below:
#
# weather_f = {day:((c_deg * 9/5) + 32) for (day, c_deg) in weather_c.items()}
#
#
# print(weather_f)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
#
# for (key, value) in student_data_frame.items():
#     print(value)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)