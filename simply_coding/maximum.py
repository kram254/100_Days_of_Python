def main():
    print("Enter three numbers: ")
 
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    num3 = float(input("Third number: "))
 
    if (num1 >= num2) and (num1 >= num3):
       largest = num1
    elif (num2 >= num1) and (num2 >= num3):
       largest = num2
    else:
       largest = num3
 
    print("The largest number is", largest)

if __name__ == '__main__':
    main()
