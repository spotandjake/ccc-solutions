# Imports
from fractions import Fraction
import matplotlib.pyplot as plt

def getEachOuterRange(x1, x2, currDenominator, newDenominator):
  # Find Scale
  scale = newDenominator / currDenominator
  # Scale Range
  x1 *= scale
  x2 *= scale
  # Compute Ranges
  firstRange = (x1 - 2, x1 - 1, newDenominator)
  secondRange = (x2 + 1, x2 + 2, newDenominator)
  # Return Ranges
  return (firstRange, secondRange)

# ProblemCode
def problemCode(filterDepth):
  # Build Filter Ranges
  ranges = [(1, 2, 3)]
  lastFilterBase = 0
  for k in range(1, filterDepth + 1):
    filterBase = 3**k
    for idx in range(0, len(ranges)):
      currRange = ranges[idx]
      if (currRange[2] != lastFilterBase):
        continue
      (firstRange, secondRange) = getEachOuterRange(*currRange, filterBase)
      ranges.append(firstRange)
      ranges.append(secondRange)
    lastFilterBase = filterBase
  d = filterDepth+1
  lastDenom = ranges[0][2]
  for idx, (x1, x2, denominator) in enumerate(ranges):
    if (denominator != lastDenom):
      lastDenom = denominator
      d -= 1
    plt.plot([x1 / denominator, x2 / denominator], [d, d])
  # Show Plot
  plt.xlabel("X")
  plt.ylabel("Y")
  plt.title("Problem 5 Senior 2023")
  plt.axis([0, 1, 1, filterDepth+2])
  plt.grid()
  plt.show()
  # Return
  return ""


problemCode(5)
