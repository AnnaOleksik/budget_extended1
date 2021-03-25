def main():

    num_exp = int(input('Podaj liczbę wydatków,które mają zostać utworzone: '))
    exp_file = open('expen_choice.txt', 'w')

    for count in range(1, num_exp + 1):

        print('Give expence ', count, sep='')
        value = input('Amount:')
        category = input('Category: ')


        exp_file.write(value + '\n')
        exp_file.write(category + '\n')

        print()

    exp_file.close()
    print('Expenses are written in file expen_choice.txt.')
main()