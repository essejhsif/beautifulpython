
def qsort1(list):
  if list == []: 
    return []
  else:
    pivot = list[0]
    lesser = qsort1([x for x in list[1:] if x < pivot])
    greater = qsort1([x for x in list[1:] if x >= pivot])
    return lesser + [pivot] + greater

if __name__ == "__main__":
  list = [2,5,1,7,3,10,4,0]
  sortedlist = qsort1(list)

  print sortedlist
