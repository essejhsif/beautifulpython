# Given an ordered list, a value to find, the index start and
# the index end, return the index where a given value is found

def binary_search(l, value, low = 0, high = -1):
  if not l: return -1
  if(high == -1): high = len(l)-1
  if low == high:
    if l[low] == value: return low
    else: return -1
  mid = (low+high)//2
  if l[mid] > value: return binary_search(l, value, low, mid-1)
  elif l[mid] < value: return binary_search(l, value, mid+1, high)
  else: return mid

l = [0, 1, 1, 2, 3, 8, 13, 21, 34]
print binary_search(l, 8, 0, 8)
