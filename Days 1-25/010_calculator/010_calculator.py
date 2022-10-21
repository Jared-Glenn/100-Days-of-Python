# First version

from art import logo

def solution(f_num, op, l_num):
  if op == "+":
    answer = float(f_num) + float(l_num)
  elif op == "-":
    answer = float(f_num) - float(l_num)
  elif op == "*":
    answer = float(f_num) * float(l_num)
  elif op == "/":
    answer = int(f_num) / int(l_num)
  else:
    print("Invalid operator.")
    return
  if answer % 1 == 0:
    answer = int(answer)
  return answer

def equation(f_num, op, l_num, sol):
  return f"{f_num} {op} {l_num} = {sol}"

print(logo)
print("Welcome to the Calculator App!")
running = True
cur_total = None

while running:
  if cur_total:
    f_num = cur_total
  else:
    f_num = input("Input a number: ")
  op = input("""Input an operation.
  Input + to add.
  Input - to subtract.
  Input * to multiply.
  Input / to divide.
  """)
  l_num = input("Input another number: ")

  sol = solution(f_num, op, l_num)
  cur_total  = sol
  print(equation(f_num, op, l_num, sol))

  keep_going = input("Would you like to perform another operation with the current total? Type 'yes' or 'no'. ")
  if keep_going == "no" or keep_going == "n":
    running = False

print("Thank you for using the Calculator!")


# Second version.

from art import logo

print(logo)

def add(n1, n2):
  answer = float(n1) + float(n2)
  if answer % 1 == 0:
    return int(answer)
  return answer

def subtract(n1, n2):
  answer = float(n1) - float(n2)
  if answer % 1 == 0:
    return int(answer)
  return answer

def multiply(n1, n2):
  answer = float(n1) * float(n2)
  if answer % 1 == 0:
    return int(answer)
  return answer

def divide(n1, n2):
  answer = float(n1) / float(n2)
  if answer % 1 == 0:
    return int(answer)
  return answer

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}

def calculator():
  running = True
  
  n1 = input("What's the first number?: ")
  
  while running:
    for operation in operations:
      print(f"Input {operation} to {operations[operation]}.")
    
    op = input()
    
    n2 = input("What's the next number?: ")
    
    function = operations[op]
    res = function(n1, n2)
    
    print(f"{n1} {op} {n2} = {res}")
  
    if input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation: ") == "y":
      num1 = res
    else:
      keep_going = False
      calculator()

calculator()