# PyBank
import os
import csv

# define file path
filepath = os.path.join('Resources', 'budget_data.csv')

# open file and skip headers
with open(filepath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter= ',')
    csvheader = next(csvreader)
    
    # set variables and create empty strings/list
    totalprofit = 0
    totalmonths = 0
    increase = 0
    decrease = 0
    previousprofit = 0 
    previousloss = 0
    increase_date = ''
    decrease_date = ''
    avgchange = 0
    delta = []

    # for loop
    for row in csvreader:
        
        # total months counter
        totalmonths += 1

        # total profit counter
        totalprofit += int(row[1])
        
        # monthly change calculation and storage. We don't want previousvalue 
        # to subtract itself, so it is outside the if statement
        if totalmonths >= 2:
            change = int(row[1]) - previousvalue
            delta.append(change)
        previousvalue = int(row[1])

        # biggest decrease calculation and storage. This also stores the date. 
        # By having it outside the if statement, we can overwrite the previous loss until we have 
        # compared all losses to find the biggest. The last one left over will be the biggest. 
        if (int(row[1]) - previousprofit) < decrease:
            decrease = int(row[1]) - previousloss
            decrease_date = row[0]
        previousloss = int(row[1])

        # biggest increase calculation and storage. This follows the same logic as the 
        # decrease, only measuring if it is greater than the difference.
        if (int(row[1]) - previousprofit) > increase:
            increase = int(row[1]) - previousprofit
            increase_date = row[0]
        previousprofit = int(row[1])

    # average change calculation. displays properly because it is outside of the for loop.
    # rounded to two decimal places.     
    avgchange = round(sum(delta) / len(delta), 2)   
    

# print outputs
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {totalmonths}")
print(f"Total: ${totalprofit}")
print(f"Average Change: ${avgchange}")
print(f"Greatest Increase in Profits: {increase_date} , (${increase})")
print(f"Greatest Decrease in Profits: {decrease_date} , (${decrease})")


# create and write to new text file
with open('analysis\Results.txt', 'w') as results:
    
    results.write ("Financial Analysis\n")
    results.write("-------------------------\n")               
    results.write(f"Total Months: {totalmonths}\n")
    results.write(f"Total: {totalprofit}\n")
    results.write(f"Average Change: ${avgchange}\n")
    results.write(f"Greatest Increase in Profits: {increase_date} , (${increase})\n")
    results.write(f"Greatest Decrease in Profits: {decrease_date} , (${decrease})")
