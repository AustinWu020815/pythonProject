array = [21, 32, 0.73, 55, 67, 2.158, 92, 45, 48, 9.4]
oddnum = []
evennum = []
error = []
for i in range(len(array)):
  if array[i]%2 == 0:
    evennum.append(array[i])
  elif array[i]%2 == 1:
    oddnum.append(array[i])
  else:
    error.append(array[i])

print(oddnum)
print(evennum)
print("Error! Those are not integers:", error)