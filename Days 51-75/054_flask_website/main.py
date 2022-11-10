from flask import Flask
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


def speed_calc_decorator(function):
    def wrapper_function():
        time1 = time.time()
        function()
        time2 = time.time()
        diff_secs = time2 - time1
        print(function.__name__, "run speed: ", diff_secs)
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
