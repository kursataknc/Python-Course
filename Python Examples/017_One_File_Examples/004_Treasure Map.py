row1 = ["👣","👣","👣"]
row2 = ["👣","👣","👣"]
row3 = ["👣","👣","👣"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

 # say given input is 32
chosencolumn = int(position[0])-1 #3 2 VERECEK
chosenrow = int(position[1])-1 #2 1 VERECEK
map[chosenrow][chosencolumn] = "X"
print(f"{row1}\n{row2}\n{row3}")