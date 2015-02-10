# Given a list of numbers, sum them up recursively

def sum(list):
  if list == []:
    return 0
  else:
    return list[0] + sum(list[1:])

if __name__ == "__main__":
  list = [1, 1, 2, 3, 5, 8]
  print sum(list)
