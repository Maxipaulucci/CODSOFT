#--------------------------------------------------------------------------------------------------------------
# FUNCTIONS
#--------------------------------------------------------------------------------------------------------------
def askNums(_inputMsg, _errorMsg):
    try:
        num = int(input(_inputMsg))

    except ValueError:
        print(_errorMsg)
        num = int(input(_inputMsg))
    return num

def askOptions(_inputMsg, _errorMsg):
    try:
        num = int(input(_inputMsg))

        if num < 0 or num > 4:
            print(_errorMsg)
            num = int(input(_inputMsg))
    except ValueError:
        print(_errorMsg)
        num = int(input(_inputMsg))
    return num

#--------------------------------------------------------------------------------------------------------------
# MAIN
#--------------------------------------------------------------------------------------------------------------
def main():
    inputMsg = "Insert the first number of the operation: "
    errorMsg = "Invalid number, try again!"
    num1 = askNums(inputMsg, errorMsg)

    inputMsg = "Insert the second number of the operation: "
    errorMsg = "Invalid number, try again!"
    num2 = askNums(inputMsg, errorMsg)

    inputMsg = "Insert the what operation you want to do [1 for + | 2 for - | 3 for * | 4 for /]: "
    errorMsg = "Invalid number, try again!"
    option = askOptions(inputMsg, errorMsg)

    if option == 1:
        result = num1 + num2
    elif option == 2:
        result = num1 - num2
    elif option == 3:
        result = num1 * num2
    try:
        if option == 4:
            result = num1 / num2
    except ZeroDivisionError:
        print("You can't divide by 0. Try again.")
        print()
        main()

    print(f"The result of the operation is: {result}")

main()