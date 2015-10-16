# Given a list, recursively find the length

def len(l):
  if l == []:
    return 0
  else:
    return 1 + len(l[1:])

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print len(l)
