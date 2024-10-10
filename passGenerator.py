#--------------------------------------------------------------------------------------------------------------
# MODULES
#--------------------------------------------------------------------------------------------------------------
import random
import string

#--------------------------------------------------------------------------------------------------------------
# FUNCTIONS
#--------------------------------------------------------------------------------------------------------------
def askLength(_inputMsg, _errorMsg):
    try:
        length = int(input(_inputMsg))

        if length < 0 or length > 30:
            print(_errorMsg)
            length = int(input(_inputMsg))
    except ValueError:
        print(_errorMsg)
        length = int(input(_inputMsg))
    return length

def askComplexity(_inputMsg, _errorMsg):
    try:
        complexity = int(input(_inputMsg))

        if complexity < 0 or complexity > 3:
            print(_errorMsg)
            complexity = int(input(_inputMsg))
    except ValueError:
        print(_errorMsg)
        complexity = int(input(_inputMsg))
    return complexity

def createPassword(_letters, _numbers, _signs, _password):
    
    inputMsg = "Insert the length of the password (30 max): "
    errorMsg = "Invalid number, try again!"
    length = askLength(inputMsg, errorMsg)

    inputMsg = "Insert the level of complexity of the password [1 for easy (only letters) | 2 for intermediate (letters and numbers) | 3 for difficult (letters, numbers and signs)]: "
    errorMsg = "Invalid number, try again!"
    complexity = askComplexity(inputMsg, errorMsg)

    if complexity == 1:
        for i in range(length):
            _password.append(random.choice(_letters))

    elif complexity == 2:
        for i in range(length):
            num = random.randint(1,2)

            if num == 1:
                _password.append(random.choice(_letters))
            else:
                _password.append(random.choice(_numbers))

    elif complexity == 3:
        for i in range(length):
            num = random.randint(1,3)

            if num == 1:
                _password.append(random.choice(_letters))
            elif num == 2:
                _password.append(random.choice(_numbers))
            else:
                _password.append(random.choice(_signs))

    return _password

def showPassword(_password):
    _password = ''.join(_password)  
    print(_password)

#--------------------------------------------------------------------------------------------------------------
# MAIN
#--------------------------------------------------------------------------------------------------------------
def main():
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    signs = list("!@#$%^&*()-_+=")
    password = []

    createPassword(letters, numbers, signs, password)
    showPassword(password)

main()