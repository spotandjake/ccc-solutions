# Imports
import os


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


# TestSuite
testFiles = os.listdir("./tests/")
for testFile in testFiles:
  if (testFile.endswith(".out")):
    continue
  # Read In
  inputFile = open(f"./tests/{testFile}")
  inputStr = inputFile.read().strip()
  inputFile.close()
  # Read Out
  outName = testFile.replace(".in", ".out")
  outputFile = open(f"./tests/{outName}")
  outputStr = outputFile.read().strip()
  outputFile.close()
  # Run
  print(f"[{testFile}]: Running")
  inputArr = inputStr.split('\n')
  searchWord = inputArr[0]
  gridRows = int(inputArr[1])
  gridCols = int(inputArr[2])
  words = []
  for x in range(0, gridRows):
    words.append(inputArr[3 + x].replace(" ", ""))
  output = problemCode(searchWord, gridRows, gridCols, words)
  # Check
  if (output == outputStr):
    print(f"[{testFile}]: Passed")
  else:
    print(f"[{testFile}]: Failed, {output} != {outputStr}")