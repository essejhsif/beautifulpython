# Given a list, perform a quicksort

def quickSort(list):
  if list == []: 
    return []
  else:
    pivot = list[0]
    lesser = quickSort([x for x in list[1:] if x < pivot])
    greater = quickSort([x for x in list[1:] if x >= pivot])
    return lesser + [pivot] + greater

if __name__ == "__main__":
  list = [2,5,1,7,3,10,4,0]
  print quickSort(list)

