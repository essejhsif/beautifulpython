# Given two inputs, print the greatest common denominator
# Usage: python gcd3.py 1 2

import sys

gcd = lambda m,n: m if not n else gcd(n,m%n)

if __name__ == "__main__":
  print gcd(int(sys.argv[1]), int(sys.argv[2]))  
