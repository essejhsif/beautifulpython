# Print all permutations of a given string
# Usage: python permute.py somestring

import sys

def permute(prev_str, str):
  if(len(str) == 0 ):
    print(prev_str)
  else:
    for i in range(len(str)):
      permute( prev_str+str[i], str[:i] + str[i+1:])
      
      
if __name__ == "__main__":
  permute("", sys.argv[1])

