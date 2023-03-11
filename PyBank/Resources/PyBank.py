import csv
import os 

# Open the CSV file and read its contents
with open(r"C:\Users\aspen\osu\homework\python-challenge\PyBank\Resources\budget_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    next(csvreader)

    # Initialize variables
    total_months = 0
    total_profit_losses = 0
    previous_profit_losses = None
    profit_losses_changes = []
    greatest_increase_date = None
    greatest_increase_amount = 0
    greatest_decrease_date = None
    greatest_decrease_amount = 0

    # Loop through each row in the CSV file
    for row in csvreader:
        # Get the month and profit/loss value for the current row
        month = row[0]
        profit_losses = int(row[1])

        # Increment the total number of months
        total_months += 1

        # Add the profit/loss value to the total
        total_profit_losses += profit_losses

        # Calculate the change in profit/losses from the previous row
        if previous_profit_losses is not None:
            profit_losses_change = profit_losses - previous_profit_losses
            profit_losses_changes.append(profit_losses_change)

            # Check if this is the greatest increase or decrease in profit/losses so far
            if profit_losses_change > greatest_increase_amount:
                greatest_increase_amount = profit_losses_change
                greatest_increase_date = month
            elif profit_losses_change < greatest_decrease_amount:
                greatest_decrease_amount = profit_losses_change
                greatest_decrease_date = month

        # Save the current profit/loss value for the next iteration
        previous_profit_losses = profit_losses

    # Calculate the average change in profit/losses
    average_profit_losses_change = sum(profit_losses_changes) / len(profit_losses_changes)

    # Print the results
    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_losses}")
    print(f"Average Change: ${average_profit_losses_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

    # Export the results to a text file
with open(r"C:\Users\aspen\osu\homework\python-challenge\PyBank\Resources\budget_data.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${average_profit_losses_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n")
