#Import Modules
from matplotlib import pyplot as plt

#create empty lists
month = []
income = []
expense = []
profit = []

#open the file
file = open("expense_report.csv", "r")

#loop through the file line by line and populate the lists apropriately
for x in file:
    line[] = x.readline().split(",")
    month.add(line[0])
    income.add(line[1])
    expense.add(line[2])
    profit.add(line[1] - line[2])
#create the plot
