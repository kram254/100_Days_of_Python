class RPNCalculator:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            raise IndexError("Stack is empty")
        return self.stack.pop()

    def evaluate(self, expression):
        tokens = expression.split()
        for token in tokens:
            if token.isdigit():
                self.push(int(token))
            elif token in ['+', '-', '*', '/']:
                operand2 = self.pop()
                operand1 = self.pop()
                if token == '+':
                    self.push(operand1 + operand2)
                elif token == '-':
                    self.push(operand1 - operand2)
                elif token == '*':
                    self.push(operand1 * operand2)
                elif token == '/':
                    self.push(operand1 / operand2)
            else:
                raise ValueError("Invalid token: {}".format(token))
        return self.pop()
