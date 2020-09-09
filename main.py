#import os module
import os
#import module to read csv
import csv
total_month = 0
total_profit= 0

# loss=0
#source path for csv and define
budget_csv = os.path.join('..','Resources', 'budget_data.csv')
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile)
    csv_header = next(csv_reader)
    for row in csv_reader:
        total_month += 1
profit = int(row[1])        
profit=0    
net_profit = budget_csv['profit'].value_counts()

# if profit > 0:
    # total_profit= total_profit + profit
# print(f'{total_month}')
# print(f'{total_profit}')     




# # #read file using CSV module
# # with open(csvpath) as csvfile:


# #     #read header row first
# #     csv_header = next(csvreader)
# #     print(f"CSV Header: {csv_header}")

# #     #read each row after header
# #     for row in csvreader:
# #         print(row)

# with open(budget_csv, 'r') as csvfile:

#     csvreader = csv.reader(csvfile, delimiter=',')

#     header = next(csvreader)
  
#     #Summary

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {total_month}')
print(f'Total: + {net_profit}')
# # print("Average Change: " + )
# # print("Greatest Increase in Profits: " + )
# # print("Greatest Decrease in Profits: " + )