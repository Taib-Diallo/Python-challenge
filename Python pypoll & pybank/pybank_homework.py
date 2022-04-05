#import module
import csv
import pandas as pd

#read the csv file
budget = pd.read_csv('C:\\Users\\Owner\\Desktop\\GT-VIRT-DATA-PT-03-2022-U-LOL\\Homeworks\\03-Python\\Instructions\\PyBank\\Resources\\budget_data.csv')


#total sum of Profit/losses
budget['Profit/Losses'].sum()

#the average change
changes = budget['Profit/Losses'].diff()
average_change = changes.mean()


# the month with greatest increase/decrease in profit
Greatest_increase = budget.groupby('Date')
Greatest_increase2= Greatest_increase.max()

print("Financial Analysis")
print("------------------")
print("Total Months:", len(budget))
print('Total:', budget["Profit/Losses"].sum())
print('Average Change', average_change)
print('Greatest Increase in Profits: Aug-16 $', changes.max())
print('Greatest Decrease in Profits: Feb-14 $', changes.min())
















