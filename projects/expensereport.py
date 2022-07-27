#Import Modules
from matplotlib import pyplot as plt

#create empty lists
<<<<<<< HEAD
month = []
=======
months = []
>>>>>>> 0d8aeff0017ae72bff91fbe4db081edc54e800f9
income = []
expense = []
profit = []

#open the file
<<<<<<< HEAD
file = open("expense_report.csv", "r")

#loop through the file line by line and populate the lists apropriately
for x in file:
    line[] = x.readline().split(",")
    month.add(line[0])
    income.add(line[1])
    expense.add(line[2])
    profit.add(line[1] - line[2])
=======
file = open('files/expense_report.csv','r')

#loop through the file line by line and populate the lists apropriately
for line in file:
    row = line.split(',')
    months.append(row[0])
    income.append(int(row[1]))
    expense.append(int(row[2]))
    profit.append(int(row[1])-int(row[2]))

>>>>>>> 0d8aeff0017ae72bff91fbe4db081edc54e800f9
#create the plot
plt.plot(months,income, 'g', months, expense, 'r', months, profit)
plt.show()
