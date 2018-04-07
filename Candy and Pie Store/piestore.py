#Create the pie list
pieList = ["Pecan", "Apple Crisp", "Bean", "Banoffee",  "Black Bun", "Blueberry", "Buko", "Burek",  "Tamale", "Steak"]

#Display list for user
for pie in pieList:
    print("(" + str(pieList.index(pie)) + ") " + pie)

#variable for storing another order boolean
orderAgain = "y"
numberOfPies = [0,0,0,0,0,0,0,0,0,0]

while orderAgain == "y":
    #prompt user for pie(s)
    pieOrder = int(input("Which pie would you like to order? Enter the pie number - "))
    numberOfPies[pieOrder] = numberOfPies[pieOrder] + 1
    #display message
    print("Great! We'll have that " + pieList[pieOrder] + " right out for you.")
    #order again message
    orderAgain = input("Would you like to place another order? (y/n)?")

print("Thank you! You ordered - ")
for pie in pieList:
    print(str(numberOfPies[pieList.index(pie)]) + " " + pie)

