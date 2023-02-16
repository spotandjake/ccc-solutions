# Input
packageDelivered = int(input(""))
collisions = int(input(""))
# Math
finalScore = (packageDelivered * 50) - (collisions * 10)
if (packageDelivered > collisions):
  finalScore += 500
print(finalScore)