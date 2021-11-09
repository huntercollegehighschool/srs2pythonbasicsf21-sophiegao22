"""
Define a function sumofsquares that takes an integer input number. The function then adds all the first n perfect squares (starting from 1).

For example, sumofsquares(3) should return 14, since 1 + 4 + 9 = 14.
"""

def sumofsquares(number):
  square = 0
  for i in range (1, number+1):
    square = square + i*i
    number = square
  return number