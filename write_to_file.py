def main():

    num_expenses = int(input('How many expenses do you want to give? '))
    expenses_file = open('expenses.txt', 'w')
    for count in range(1, num_expenses + 1):
        total=0
        expenses = float(input('Expense number ' +str(count) + ': '))

        expenses_file.write(str(expenses) + '\n')

main()