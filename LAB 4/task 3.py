from enum import Enum

class actions(Enum):
    Plus = 1
    Minus = 2
    Division = 3
    Multiplication = 4


def calculator(firstNumber, secondNumber, operation):
    result = 0
    match operation:
        case actions.Plus:
            result = firstNumber+secondNumber
        case actions.Minus:
            result = firstNumber-secondNumber
        case actions.Division:
            result = firstNumber/secondNumber
        case actions.Multiplication:
            result = firstNumber*secondNumber
    return firstNumber, secondNumber, operation, result


firstNumber = int(input("Введите первое число: "))
secondNumber = int(input("Введите второе число: "))
operation = actions[input("Введите операцию (Plus,Minus,Division,Multiplication): ")]
print(calculator(firstNumber, secondNumber, operation))