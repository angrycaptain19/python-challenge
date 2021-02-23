import os
import csv 

#Collecting Data From Resources Folder 
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

date = []
profit = []
changes = []

with open(budget_data_csv, 'r') as csvfile: 

    csvreader = csv.reader(csvfile, delimiter = ',') 
    header = next(csvreader) 

    for row in csvreader:

        date.append(row[0])

        profit.append(row[1])


#https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int
profit = [int(i) for i in profit]

#https://www.geeksforgeeks.org/python-program-to-find-sum-of-elements-in-list/
totalprofit = 0
difference = 0
for row in range(len(profit)):
    totalprofit += profit[row]
    if row == len(profit) - 1:
        break

    difference = profit[row + 1] - profit[row]
    changes.append(difference)
print(" ' ' ' text")
print("Finanical Analysis")
print("--------------------------")

numofmonths = len(date)
print(f"Total Months: {numofmonths}")

print(f"Total: ${totalprofit}")

average = sum(changes) / len(changes)
average = round(average, 2)
print(f"Average Changes: ${average}")

highestincrease = max(changes)
highestdecrease = min(changes)

for row in range(len(changes)):
    if changes[row] == highestincrease: 
        dateofincrease = date[row+1]
        break

for row in range(len(changes)):
    if changes[row] == highestdecrease: 
        dateofdecrease = date[row+1]
        break


print(f"Greatest Increase In Profits: {dateofincrease}  $({highestincrease})")
print(f"Greatest Decrease In Profits: {dateofdecrease}  $({highestdecrease})" )
print(" ' ' '")