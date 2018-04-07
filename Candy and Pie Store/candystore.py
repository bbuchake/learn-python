candyInStore = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Sweedish Fish", "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

allowance = 5

selectedCandy = []

#for i in range(len(candyInStore)):
    #print("[" + str(i) + "] " + candyInStore[i])
for candy in candyInStore:
    print ("[" + str(candyInStore.index(candy)) + "] " + candy)

while allowance > 0:
    candyIndex = int(input ("Which candy would you like to take home?"))
    selectedCandy.append(candyInStore[candyIndex])
    allowance = allowance - 1

print("You are taking home: ")

for j in range(len(selectedCandy)):
    print(selectedCandy[j])
    