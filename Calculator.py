def calculator(num_1:float = 0, num_2:float = 0, operator = '+'):
    if operator == '+':
        return (num_1 + num_2)
    elif operator == '-':
        return (num_1 - num_2)
    elif operator == '*':
        return (num_1 * num_2)
    elif operator == '/':
        return (num_1 / num_2)
    elif operator == '%':
        return (num_1 % num_2)
    else:
        return (num_1 // num_2)


while True:
    try_again = input("Do you want  to use the Calculator?: (Yes/No)").lower()

    if try_again in ('yes', 'y'):
        try:
            num_1 = float(input("Enter first number: "))
            num_2 = float(input("Enter second number: "))
            operator = input("Enter operator: (for Example: +, -, *, /, //, %): )")
            if operator not in ('+', '-', '*', '/', '//', '%'):
                print("Invalid Operator, Please Try Again")
                continue
            if operator in ('/', '//') and num_2 == 0:
                print("Cannot divide by Zero.")
                continue

            result = calculator(num_1 = num_1, num_2 = num_2, operator = operator)
            print(f"{num_1} {operator} {num_2} = {result}")
        except Exception as e:
            print(f"Input Value is not Valid: {e}")

    elif try_again in ('no', 'n'):
        print("Thank You For Using our Calculator. Please Rate below 1-5")
        input("Rating: ")
        break
    else:
        print("Invalid Input")
        continue

