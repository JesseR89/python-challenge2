import os
import csv


#File to Load
csvpath = os.path.join("Resources", "budget_data.csv")
analysis_output = os.path.join("Analysis", "budget_output.txt")

#change in months variable 
change_in_months = []
greatest_increase = ['', 0]
greatest_decrease = ['', 10000000]
total_change = []
total_amount = 0 
with open(csvpath) as data:
    csvreader = csv.reader(data)
    header = next(csvreader)
    
#skip the header row
next (csv_reader)

#Initialize a variable to keep track of the total months
total_months = 0 

#Read through each row of data after the headers by creating a for loop   
    for row in csvreader:
#Go through each row and add to the total months

    first_row = next(csvreader)
    total_months = total_months += 1 
    total_amount = total_amount + int(first_row[1])
    previous_amount =  int(first_row[1])
    
#print total months
print('Total Months:' , total_months)
#calculate the net total of "profit/loses" column
#create a for loop , then convert to a float 
net_total = 0

#go through each row and add to the net_total 

for row in csv_reader:
    net_total += float(row[1])
    
#Print the net total
print(f'Net Total: ${net_total}')
#calculate the changes in "profit/losses" over the entire period, and the average of the changes
data = list(reader)
column = [float(row[1]) for row in data]

change = [column[i+1] - [column[i] for i in range(len(column)-1)]]
average_change = sum(change)/ len(change)

print('changes over the entire column:' change)
print('Average change:' average_change)
#calculate the greatest increase in profits (date and amount) over the entire period

profits = [float(row[1]) for row in data]  

greatest_increase = max(profits)
greatest_increase_index = profits.index(greatest_increase)
date_of_greatest_increase = data[greatest_increase_index][0]

print("Greatest Increase in Profits:")
print("Date:", date_of_greatest_increase)
print("Amount:", greatest_increase)
#the greatest decrease in profits(date and amount over the entire period)
profits_two = [float(row[1]) for row in data]  

greatest_decrease = min(profits_two)
greatest_decrease_index = profits.index(greatest_decrease)
date_of_greatest_decrease = data[greatest_increase_index][0]

print("Greatest Decrease in Profits:")
print("Date:", date_of_greatest_decrease)
print("Amount:", greatest_decrease)
#print the financial analysis that aligns with the previous results

print('Financial Analysis')
print("----------------------")
print('Total Months: ' total_months)
print('Total:' net_total)
print('Average Change:' average_change)
print('Greatest Increase in Profits: ' greatest_increase)
print('Greatest Decrease in Profits: ' greatest_decrease)