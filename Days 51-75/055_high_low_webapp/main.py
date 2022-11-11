from flask import Flask
import random

app = Flask(__name__)

random_num = None

@app.route('/')
def index():
    global random_num
    random_num = random.randint(0, 9)
    return '<h1>Guess a number between 0 and 9</h1><br>' \
           '<div><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></div>'




@app.route('/<guess>')
def guess_page(guess):
    guess = int(guess)
    if guess == random_num:
        return '<h1 style="color:green;">You found me!</h1><br>' \
           '<div><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"></div>'
    elif guess < random_num:
        return '<h1 style="color:red;">Too low! Try again!</h1><br>' \
               '<div><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"></div>'
    else:
        return '<h1 style="color:red;">Too high! Try again!</h1><br>' \
               '<div><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"></div>'

# def make_bold(function):
#     def bolding():
#         return "<strong>" + function() + "</strong>"
#     return bolding
#
# def make_emphasis(function):
#     def emphasizing():
#         return "<em>" + function() + "</em>"
#     return emphasizing
#
# def make_underlined(function):
#     def underlining():
#         return "<u>" + function() + "</u>"
#     return underlining
#
#
# @app.route("/bye")
# @make_bold
# @make_emphasis
# @make_underlined
# def bye():
#     return "Bye!"

# # Create the logging_decorator() function 👇
#
# def logging_decorator(function):
#     def wrapper(*args, **kwargs):
#         res = function(*args)
#         print(f"You called {function.__name__}{args}")
#         print(f"It returned: {res}")
#     return wrapper
#
#
# # Use the decorator 👇
#
# @logging_decorator
# def add(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
#
# add(1, 2, 3)



if __name__ == "__main__":
    app.run(debug=True)
