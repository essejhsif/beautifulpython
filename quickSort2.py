def quickSort(list):
  if (len(list) < 2):
    return list
  else:
    first = list[0]  # pivot
    rest = list[1:]
    lo = [x for x in rest if x < first]
    hi = [x for x in rest if x >= first]
    return quickSort(lo) + [first] + quickSort(hi)

if __name__ == "__main__":
  list = [2,4,1,3,0,5]
  print quickSort(list)
