
try:
    user_input_x = input("Please input x: ")
    user_input_y = input("Please input y: ")

    x = float(user_input_x)
    y = float(user_input_y)

    result_pow = x ** y
    print(f"{x} to the power of {y} is {result_pow}")
except ValueError:
    
    print("Invalid input")
