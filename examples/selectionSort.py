def selectionSort(list):
  if (len(list) < 2):
    return list
  else:
    i = list.index(min(list))
  return [list[i]] + selectionSort(list[:i] + list[i+1:])

if __name__ == "__main__":
  list = [1,5,6,2,4,0]
  print selectionSort(list)
