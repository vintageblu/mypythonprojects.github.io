import re

print("Simple mathematical calculator")
print("Type 'quit' to exit")

previous = 0
run = True


def performMath():
  global run
  global previous
  equation = ""
  
  #idk what i'm doing 😭, let's do if else
  if previous == 0:
    equation = input("Enter Equation:")
  else:
    equation = input(str(previous))
    

  if equation == 'quit':
    print("Goodbye")
    run = False
  else:
    equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
    

    if previous == 0:
      previous = eval(equation)
    else:
      previous = eval(str(previous) + equation)


while run:
  performMath()
