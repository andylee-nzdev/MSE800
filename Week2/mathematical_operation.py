
def calculate_basic(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Error: cant not be 0"
        return a / b
    else:
        return "Not support operator"


def main():
    c1 = complex(2, 3) # 2 + 3j
    c2 = complex(1, 1) # 1 + 1j
    print(f"{c1} + {c2} = {calculate_basic(c1, c2, '+')}")
    print(f"{c1} - {c2} = {calculate_basic(c1, c2, '-')}")
    print(f"{c1} * {c2} = {calculate_basic(c1, c2, '*')}")
    print(f"{c1} / {c2} = {calculate_basic(c1, c2, '/')}")
 

if __name__ == "__main__":
    main()