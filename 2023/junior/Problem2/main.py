pepperCount = int(input(""))
totalSpice = 0
for i in range(0, pepperCount):
  pepperType = input("")
  if (pepperType == "Poblano"):
    totalSpice += 1500
  elif (pepperType == "Mirasol"):
    totalSpice += 6000
  elif (pepperType == "Serrano"):
    totalSpice += 15500
  elif (pepperType == "Cayenne"):
    totalSpice += 40000
  elif (pepperType == "Thai"):
    totalSpice += 75000
  elif (pepperType == "Habanero"):
    totalSpice += 125000
print(totalSpice)