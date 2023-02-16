# ProblemCode
def problemCode(searchWord, gridRows, gridCols, words):
  backwardsWord = searchWord[::-1]
  # Search Horizontal
  totalFinds = 0
  foundIndex = 0
  for x in range(0, gridCols):
    for y in range(0, gridRows):
      if (words[y][x] == searchWord[foundIndex]):
        foundIndex += 1
        if (foundIndex == len(searchWord)):
          totalFinds += 1
          foundIndex = 0
    foundIndex = 0
  for x in range(0, gridCols):
    for y in range(0, gridRows):
      if (words[y][x] == backwardsWord[foundIndex]):
        foundIndex += 1
        if (foundIndex == len(searchWord)):
          totalFinds += 1
          foundIndex = 0
    foundIndex = 0
  # Search Vertical
  for x in range(0, gridRows):
    if (searchWord in words[x]):
      totalFinds += 1
  for x in range(0, gridRows):
    if (backwardsWord in words[x]):
      totalFinds += 1
  # Search Diagonal
  foundIndex = 0
  for x in range(0, gridCols):
    for y in range(1, gridRows):
      if (words[y][x] == searchWord[foundIndex]):
        foundIndex += 1
        if (foundIndex == len(searchWord)):
          totalFinds += 1
          foundIndex = 0
    foundIndex = 0
  for x in range(0, gridCols):
    for y in range(1, gridRows):
      if (words[y][x] == backwardsWord[foundIndex]):
        foundIndex += 1
        if (foundIndex == len(searchWord)):
          totalFinds += 1
          foundIndex = 0
    foundIndex = 0
  # Search L
  # Return
  return f"{totalFinds}"


# Input Code
searchWord = input("")
gridRows = int(input(""))
gridCols = int(input(""))
words = []
for x in range(0, gridRows):
  words.append(input("").replace(" ", ""))
output = problemCode(searchWord, gridRows, gridCols, words)
print(output)