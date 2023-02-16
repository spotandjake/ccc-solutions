# Imports
from fractions import Fraction


# ProblemCode
def problemCode(filterKValue):
  # Build Test List
  output = []
  usedSymmetry = False
  if (filterKValue % 2 == 0):
    usedSymmetry = True
    for i in range(0, int(filterKValue / 2) + 1):
      output.append((i, Fraction(i, filterKValue)))
  else:
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
        filterStart = Fraction(lastNumerator, filterBase)
        filterEnd = Fraction(lastNumerator + 1, filterBase)
        output = list(filter(lambda x: (x[1] <= filterStart or x[1] >= filterEnd), output))
        if (
          len(output) == 1 or (len(output) == 2 and output[0] == 0 and output[1] == filterKValue)
        ):
          break
      else:
        filterCell = True
        lastNumerator = filterNumerator
    else:
      continue
    break
  # Numerical Output
  outputList = []
  for point in output:
    outputList.append(point[0])
  if (usedSymmetry):
    for point in reversed(output):
      outputList.append(filterKValue - point[0])
  # Return
  return outputList
for test in range(3, 20):
  print(f"{test} -> {problemCode(test)}")