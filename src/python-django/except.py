import sys

try:
  x = int(input("x: "))
  y = int(input("y: "))
except ValueError:
  print("Invalid input")
  sys.exit(1)   # Exit program to prevent it from continuing

try:
  print(f"{x} / {y} = {x / y}")
except ZeroDivisionError:
  print("Cannot divide a number by zero")
  sys.exit(1)
