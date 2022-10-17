# try = Something that might cause an exception.
#
# except = Do this if there WAS an exception.
#
# else = Do this if there were NO exceptions.
#
# finally = Do this no matter what happens.

# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")

# raise KeyError
# raise TypeError("This is an error that I made up.")

# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")
#
# bmi = weight / height ** 2
# print(bmi)

# fruits = ["Apple", "Pear", "Orange"]
#
# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         fruit = "Fruit"
#     print(fruit + " pie")
#
#
# make_pie(4)


# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass
#
#
# print(total_likes)

# json.dump() = to add to json file
# json.load() = read json