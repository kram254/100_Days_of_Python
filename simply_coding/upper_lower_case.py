def change_case(string, case):
    if case == 'upper':
        return string.upper()
    elif case == 'lower':
        return string.lower()
    else:
        return "Invalid case specified. Use 'upper' or 'lower'."

def main():
    input_string = input("Enter a stringP (word or sentence): ")
    input_case = input("Enter 'upper' or 'lower': ")

    result = change_case(input_string, input_case)
    print(result)

if __name__ == '__main__':
    main()
