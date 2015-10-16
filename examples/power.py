# Recursion example to show how to find the power (n) of 
# a given number (a)

def power(a,n):
  if n == 0:
    return 1
  else:
    return a*power(a,n-1)

if __name__ == "__main__":
  print power(2, 3)
