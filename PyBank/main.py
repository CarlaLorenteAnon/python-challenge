import csv
import os
csvpath = os.path.join("..","PyBank","Resources","budget_data.csv")
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) #reads the head row first
    total_months = 0
    net_total_amount_profit = 0
    total_change = 0
    for row in csvreader:
        total_months += 1
        if (total_months ==1): #Set the values the first time
            greatest_increase = int(row[1])
            greatest_decrease = int(row[1])
            greatest_increase_month = row[0]
            greatest_decrease_month = row[0]
            previous_month_value = int(row[1])
            #total_change = int(row[1])
        elif int(row[1])-previous_month_value > greatest_increase:
            greatest_increase = int(row[1])-previous_month_value
            greatest_increase_month = row[0]
        elif int(row[1])-previous_month_value < greatest_decrease:
            greatest_decrease = int(row[1])-previous_month_value
            greatest_decrease_month = row[0]
        net_total_amount_profit += int(row[1])
        total_change += (int(row[1]) - previous_month_value)
        previous_month_value = int(row[1])
    average_profit = total_change / (total_months -1)

#Print to the terminal
print("Financial Analysis")
print("--------------------")
print("Total Months: {}".format(total_months))
print("Total: ${}".format(net_total_amount_profit))
print("Average Change: $%.2f" % (average_profit))
print("Greatest Increase in Profits: {} (${})".format(greatest_increase_month, greatest_increase))
print("Greatest Decrease in Profits: {} (${})".format(greatest_decrease_month, greatest_decrease))

# #Print analysis to the file
#output_path = os.path.join("..","output_PyBank.txt")
#print(output_path)
with open("output_PyBank.txt", 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("--------------------\n")
    txtfile.write("Total Months: {}\n".format(total_months))
    txtfile.write("Total: ${}\n".format(net_total_amount_profit))
    txtfile.write("Average Change: $%.2f\n" % (average_profit))
    txtfile.write("Greatest Increase in Profits: {} (${})\n".format(greatest_increase_month, greatest_increase))
    txtfile.write("Greatest Decrease in Profits: {} (${})\n".format(greatest_decrease_month, greatest_decrease))
