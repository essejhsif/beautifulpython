# Given a list, return the index of a given value (n)

def search(n, l):
  try:
    return l.index(n)
  except:
    return -1

l = [1,2,3,4]

print search(3,l)

