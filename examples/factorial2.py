# Recursive factorial definition

def fact(n):
  if n < 0:
    # Just a check to make sure we don't call (-n)!
    return "Error - cannot accept neg numbers."
  elif n == 0:
    # Base case: 0! = 1
    return 1
  else:
    # Recursive case: n! = n*(n-1)!
    return n * fact(n-1)
