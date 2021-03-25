sum = 0
income = float(input("Give monthly income: "))
exp = float(input("Expense : "))
while exp != 0:
    sum += exp
    exp = float(input("Give another expence or 0 to quit"))

left = income - sum #
print("Your expenses so far {} \nYour monthly balance is {}".format(sum, left))