#import os module
import os
#import module to read csv
import csv
total_month = 0
profit = 0

# loss=0
#source path for csv and define
budget_csv = os.path.join('..','Resources', 'budget_data.csv')
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile)
    csv_header = next(csv_reader)
    for row in csv_reader:
        total_month += 1
    def total_profit(csv_reader):
        profit = int(csv_reader[1])
        for profit in csv_reader:
            total_profit += profit


print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {total_month}')
print(f'Total: {total_profit}')
# # print("Average Change: " + )
# # print("Greatest Increase in Profits: " + )
# # print("Greatest Decrease in Profits: " + )