#calculation

#input number

firstNumber = int(input("Input a first number: "))
secondNumber = int(input("Input a second number: "))

#actions of the numbers

actionsOfTheNumbers = input("Please, select actions on numbers: -, +, *, /: ")

if actionsOfTheNumbers == "+":
    print("Your sum: " + str(firstNumber + secondNumber))
elif actionsOfTheNumbers == "-":
     print("Your diferense:" + str(firstNumber - secondNumber))
elif actionsOfTheNumbers == "*":
     print("Your multiplicatio:" + str(firstNumber * secondNumber))
elif actionsOfTheNumbers == "/":
     print("Your division: " + str(firstNumber / secondNumber))
else:
    print("You don`t select actions.")

#end ^_^