# Reverse the input of a string using recusion
# https://github.com/essejhsif

import sys

def reverseString(s):
  if s == "":
    return s
  else:
    return reverseString(s[1:]) + s[0]

if __name__ == "__main__":
  print reverseString(sys.argv[1])
