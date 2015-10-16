def radixSort(list):
  # Only works for lists of non-negative integers!
  maxValue = max(list)
  
  def rsort(list, digitSelector):
    if (digitSelector > maxValue):
      return list
    else:
      zeroes = [x for x in list if (x & digitSelector == 0)]
      ones = [x for x in list if (x & digitSelector != 0)]
      return rsort(zeroes + ones, digitSelector<<1)
  return rsort(list, 1)

if __name__ == "__main__":
  list = [2,5,3,1,0,4]
  print radixSort(list)
