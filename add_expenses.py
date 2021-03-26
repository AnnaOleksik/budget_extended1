def main():
    infile=open("expenses.txt","r")
    num1=float(infile.readline())
    num2 = float(infile.readline())
    num3 =float(infile.readline())

    infile.close()
    total=num1+num2+num3
    print("Your monthly expenses so far: ",total)
main()