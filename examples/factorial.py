# Gives the factorial of a given integer

import sys

def factorial(n):
  n = int(n)
  if n == 1:
    return 1
  else:
    return n * factorial(n-1)

if __name__ == "__main__":
  print factorial(sys.argv[1])

