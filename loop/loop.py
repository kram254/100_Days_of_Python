def main():
    print("~~~~~~~~~~~~~~~~~~~ Lakhwinder Singh ~~~~~~~~~~~~~~~~~~")
    while True:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        num3 = int(input("Enter the third number: "))
        if num1 > 0 and num2 > 0 and num3 > 0:
            sum = num1 + num2 + num3
            
            print("The sum of the three numbers is:", sum)
            
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        else:
            print("Only positive numbers are accepted.")
        repeat = input("Do you wish to perform the operation again? (yes/no) ")
        
        if repeat.lower() == "no":
            break

if __name__ == "__main__":
    main()