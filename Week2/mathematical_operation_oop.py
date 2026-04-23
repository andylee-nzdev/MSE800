
class Calculator:
    def add(self, a, b):
        return a + b
    
    def suctract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("You cannot divide by zero")
        return a / b



def basic_operation_tests():
    c1 = 30
    c2 = 5
    cal = Calculator()
    print(f"{c1} + {c2} = {cal.add(c1, c2)}")
    print(f"{c1} - {c2} = {cal.suctract(c1, c2)}")
    print(f"{c1} * {c2} = {cal.multiply(c1, c2)}")
    print(f"{c1} / {c2} = {cal.divide(c1, c2,)}")
 

def complex_operation_tests():
    c1 = complex(2, 3) # 2 + 3j
    c2 = complex(1, 1) # 1 + 1j
    cal = Calculator()
    print(f"{c1} + {c2} = {cal.add(c1, c2)}")
    print(f"{c1} - {c2} = {cal.suctract(c1, c2)}")
    print(f"{c1} * {c2} = {cal.multiply(c1, c2)}")
    print(f"{c1} / {c2} = {cal.divide(c1, c2,)}")

def main():
    basic_operation_tests()
    complex_operation_tests()

if __name__ == "__main__":
    main()