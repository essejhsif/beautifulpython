# Given a list (L) find the min element 

def minElement(L):
  if len(L) == 1:
    return L[0]

  else:
    min = minElement(L[1:])
    if L[0] < min:
      return L[0]
    else:
      return min

L = ['1','1','2','3','5','8','13']
print minElement(L)
