# Inputs
totalPeople = int(input(""))
dayCount = [0, 0, 0, 0, 0]
for x in range(0, totalPeople):
  schedule = input("")
  for i in range(0, len(schedule)):
    if (schedule[i] == "Y"):
      dayCount[i] += 1
# Check Each
maxDay = 0
for i in range(0, 5):
  if (dayCount[i] > maxDay):
    maxDay = dayCount[i]
days = []
for i in range(0, 5):
  if (dayCount[i] == maxDay):
    days.append(f"{i + 1}")
print(",".join(days))