# Recursively evaluates whether string 1 (s1) is the same
# length as string 2 (s2)
# https://github.com/essejhsif

import sys

def sameLength(s1,s2):    
  if s1 == '' or s2 == '':
    return s1 == '' and s2 == ''
  else:
    return sameLength(s1[1:],s2[1:])

if __name__ == "__main__":
  print sameLength(sys.argv[1], sys.argv[2])
