# Module
import os


# Calculations
def problemCode(colCount, row1, row2):
  totalTileCount = 0
  triType = 0
  for x in range(0, colCount):
    if (x < (colCount - 1) and row1[x] == "1" and row1[x + 1] == "1"):
      totalTileCount += 1
    elif (row1[x] == "1"):
      totalTileCount += 3

    if (x < (colCount - 1) and row2[x] == "1" and row2[x + 1] == "1"):
      totalTileCount += 1
    elif (row2[x] == "1"):
      totalTileCount += 3

    if (row1[x] == "1" and row2[x] == "1" and triType == 0):
      totalTileCount -= 2
    # Flip Tri
    if (triType == 0):
      triType = 1
    else:
      triType = 0
  return f"{totalTileCount}"


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
  colCount = int(inputArr[0])
  row1 = inputArr[1].split(" ")
  row2 = inputArr[2].split(" ")
  output = problemCode(colCount, row1, row2)
  # Check
  if (output == outputStr):
    print(f"[{testFile}]: Passed")
  else:
    print(f"[{testFile}]: Failed, {output} != {outputStr}")