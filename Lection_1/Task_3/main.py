#calculation

#input number

firstNumber = int(input("Input a first number: "))
secondNumber = int(input("Input a second number: "))

#actions of the numbers

actionsOfTheNumbers = input("Please, select actions on numbers: -, +, *, /: ")

#match 

match actionsOfTheNumbers:
     case "+":
          print("Your sum: " + str(firstNumber + secondNumber))
     case "-":
          print("Your diferense:" + str(firstNumber - secondNumber))
     case "*":
          print("Your multiplication:" + str(firstNumber * secondNumber))
     case "/":
          print("Your division: " + str(firstNumber / secondNumber))
     case _:
          print("You don`t select actions.")

#end ^_^