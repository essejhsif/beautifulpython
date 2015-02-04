# Convert from an integer in base 10 to any base

def toStr(n,base):
  convertString = "0123456789ABCDEF"
  if n < base:
    return convertString[n]
  else:
    return toStr(n//base,base) + convertString[n%base]

print(toStr(1234,16))
