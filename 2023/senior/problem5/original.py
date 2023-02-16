# Imports
import os
from fractions import Fraction


# ProblemCode
def problemCode(filterKValue):
  # Build Test List
  output = []
  for i in range(0, filterKValue + 1):
    output.append((i, Fraction(i, filterKValue)))
  # Test
  for filterLevel in range(1, filterKValue):  # 1, filterKValue+1
    # Get Filters
    filterBase = (3**filterLevel)
    filterCell = False
    lastNumerator = 0
    for filterNumerator in range(1, filterBase + 1):
      if (filterCell):
        filterCell = False
        # Compare
        newOutput = []
        filterStart = Fraction(lastNumerator, filterBase)
        filterEnd = Fraction(lastNumerator + 1, filterBase)
        for (i, outputNumber) in output:
          if (outputNumber <= filterStart or outputNumber >= filterEnd):
            newOutput.append((i, outputNumber))
        output = newOutput
      else:
        filterCell = True
        lastNumerator = filterNumerator
  outputStr = ""
  for (i, _) in output:
    outputStr += f"{i}\n"
  # Return
  return outputStr.strip()


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
  output = problemCode(int(inputStr))
  # Check
  if (output == outputStr):
    print(f"[{testFile}]: Passed")
  else:
    print(f"[{testFile}]: Failed, {output} != {outputStr}")