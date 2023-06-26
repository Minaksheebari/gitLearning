#two inputs of num1 & num2
#input operator + - * / % **

num1 = int(input("Enter first number: "))
if(num1==0):
    print("Please enter value other than zero")
    num1 = int(input("Enter first number: "))

num2 = int(input("Enter second number: "))
if(num2==0):
    print("Please enter value other than zero")
    num2= int(input("Enter second number: "))
operator = input("Enter operator to perform operation(+ - * / %): ")

if(operator=="+"):
    print("Addition of",num1,"+",num2, "is: ", num1+num2)
elif(operator=="-"):
    print("Suntraction of",num1,"-",num2, "is: ", num1-num2)
elif(operator=="*"):
    print("Multiplication of",num1,"*",num2, "is: ", num1*num2)
elif(operator=="/"):
    print("Division of",num1,"/",num2, "is: ", num1/num2)
elif(operator=="%"):
    print("Modulus of",num1,"%",num2, "is: ", num1%num2)
else:
    print("Check if you have entered wrong input & try again...")

# if(operator=="+" and num1>=1 and num2>=1):
#     print("Addition of",num1,"+",num2, "is: ", num1+num2)
# elif(operator=="-" and num1>=1 and num2>=1):
#     print("Suntraction of",num1,"-",num2, "is: ", num1-num2)
# elif(operator=="/" and num1>=1 and num2>=1):
#     print("Division of",num1,"/",num2, "is: ", num1/num2)
# elif(operator=="*" and num1>=1 and num2>=1):
#     print("Multiplication of",num1,"*",num2, "is: ", num1*num2)
# elif(operator=="%" and num1>=1 and num2>=1):
#     print("Modulus of",num1,"%",num2, "is: ", num1%num2)
# else:
#     print("Check if you have entered zero & try again...")


