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


colCount = int(input(""))
row1 = input("").split(" ")
row2 = input("").split(" ")
output = problemCode(colCount, row1, row2)
print(output)