def insertionSort(list):
  if (len(list) < 2):
    return list
  else:
    first = list[0]
    rest = insertionSort(list[1:])
    lo = [x for x in rest if x < first]
    hi = [x for x in rest if x >= first]
    return lo + [first] + hi

if __name__ == "__main__":
  list = [2,5,3,0,1,4]
  print insertionSort(list)
