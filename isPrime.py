# Check if input n is prime

import sys

def isPrime(n):
    def primeHelper(n, j):
        if j == 1:  
            return True
        else:
            return n % j != 0 and primeHelper(n, j - 1)
    return primeHelper(n, n-1)
    
if __name__ == "__main__":
  print isPrime(int(sys.argv[1]))
