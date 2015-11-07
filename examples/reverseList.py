# Given a list, reverse its order
# https://github.com/essejhsif

def reverse(l):
  if l == []:
    return [];
  else:
    return reverse(l[1:]) + [l[0]] 

if __name__ == "__main__":
  list = [2,5,1,7,3,10,4,0]

  print reverse(list)
