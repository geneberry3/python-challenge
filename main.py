#import os module
import os

#import module to read csv
import csv

#source path for csv and define
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter, ",")

monthly = budget_csv[0]
profits = budget_csv[1]



# print(f'monthly)
# # Reading using CSV module
# with open(csvpath) as csvfile:

#     # CSV reader specifies delimiter and variable that holds contents
#     csvreader = csv.reader(csvpath, delimiter=',')

#     # print(csvreader)
#     for row in csvreader
        

        # total_months = months.
        # total_profit=0
# for row in csvreader:

#     profit=0
# #     loss=0

# #     # profit = int(row[1])
        
# #     if profit > 0:
# #         total_profit= total_profit + profit
# #         print(total_profit)

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

# print("Financial Analysis")
# print("----------------------------")
# print(f"Total Months: " + months)
# # print("Total: " + )
# # print("Average Change: " + )
# # print("Greatest Increase in Profits: " + )
# # print("Greatest Decrease in Profits: " + )