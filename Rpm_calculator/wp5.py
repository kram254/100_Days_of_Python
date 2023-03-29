from rpn_calculator import RPNCalculator

def main():
    with open('input.rpn', 'r') as f:
        expressions = f.readlines()
    calculator = RPNCalculator()
    results = []
    for expression in expressions:
        try:
            result = calculator.evaluate(expression.strip())
            results.append(result)
        except IndexError as e:
            print(f"Error: {str(e)} - skipping expression: {expression.strip()}")
    with open('output.txt', 'w') as f:
        for result in results:
            f.write(str(result) + '\n')

if __name__ == '__main__':
    main()
