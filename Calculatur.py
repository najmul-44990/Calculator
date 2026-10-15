#১	Simple Calculator	Input, Output, If-Else, Functions
num1=float(input("Enter first number: "))
operator=input("Enter operator: ")
num2=float(input("Enter second number: "))

def calculation():
    if(operator=="+"):
     print(num1+num2)
    elif(operator=="-"):
       print(num1-num2)
    elif(operator=="*"):
        print(num1*num2)
    elif(operator=="/"):
       if(num2!=0):
           print(num1/num2)
       else:
             print("Cannot divide by zero!")
    else:
       print("Invalid operator!")


calculation()
