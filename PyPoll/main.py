# PyPoll
import os
import csv

# define file path
filepath = os.path.join('Resources', 'election_data.csv')

# open file and skip headers
with open(filepath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter= ',')
    csvheader = next(csvreader)
    
    # set variables
    totalvotes = 0
    candidate_1 = 0
    candidate_2 = 0
    candidate_3 = 0
    candidate_1_name = 'Charles Casper Stockham'
    candidate_2_name = 'Diana DeGette'
    candidate_3_name = 'Raymon Anthony Doane'
    # create for loop
    for row in csvreader:

        # total vote counter
        totalvotes += 1
        
        # vote sorter
        if (row[2]) == candidate_1_name:
            candidate_1 += 1

        if (row[2]) == candidate_2_name :
            candidate_2 += 1

        if (row[2]) == candidate_3_name:
            candidate_3 += 1 

    # percentage calculations        
    candidate_1_percentage = round((candidate_1 / totalvotes) * 100, 3)
    candidate_2_percentage = round((candidate_2 / totalvotes) * 100, 3)
    candidate_3_percentage = round((candidate_3 / totalvotes) * 100, 3)
    
    # determine winner
    if candidate_1 > candidate_2 and candidate_3:
        winner = candidate_1_name
    
    if candidate_2 > candidate_1 and candidate_3:
        winner = candidate_2_name 
    
    if candidate_3 > candidate_1 and candidate_2:
        winner = candidate_3_name

# print outputs
print("Election Results")
print("-------------------------")
print(f"Total Months: {totalvotes}")
print("-------------------------")
print(f"{candidate_1_name}: {candidate_1_percentage}% ({candidate_1})")
print(f"{candidate_2_name}: {candidate_2_percentage}% ({candidate_2})")
print(f"{candidate_3_name}: {candidate_3_percentage}% ({candidate_3})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# create and write text file with results
with open('analysis\Results.txt', 'w') as results:
    results.write ("Election Results\n")
    results.write("-------------------------\n")               
    results.write(f"Total Months: {totalvotes}\n")
    results.write("-------------------------\n") 
    results.write(f"{candidate_1_name}: {candidate_1_percentage}% ({candidate_1})\n")
    results.write(f"{candidate_2_name}: {candidate_2_percentage}% ({candidate_2})\n")
    results.write(f"{candidate_3_name}: {candidate_3_percentage}% ({candidate_3})\n")
    results.write("-------------------------\n")
    results.write(f"Winner: {winner}\n")
    results.write("-------------------------")