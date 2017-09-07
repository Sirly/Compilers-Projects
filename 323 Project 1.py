# Postfix mathematical operation
# Created: 8/30/2017
# Updated: 8/31/3017
#
# Author(s):    Kevin Nakashima
#               Patrick Ryan
#               Marek Sautter



def isOperand(c):
    if c == '+' or c == '-' or c == '/' or c == '*' or c =='^':
        return False
    else:
        return True

def Evaluate(num1,num2, operator):
    if(operator == "+"):
        return num1 + num2
    if(operator == "-"):
        return num1 - num2
    if(operator == "*"):
        return num1 * num2
    if(operator == "/"):
        return num1 / num2
    if(operator == "^"):
        return pow(num1,num2)

def main():
     
    goOn = True
    
    while(goOn):
         # declare/reset variables
         stack = []
         alpha = []
         dic = dict()
         
         # get string from user
         expression = input("Enter postfix expression followed by a '$': ")         

         # remove $
         expression = expression[:-1]
         
         # parse string for alpha variables without duplicates
         for char in expression:
             if char.isalpha() and char not in alpha:
                 alpha.append(char)

         # prompt for variable values
         for char in alpha:
             dic[char] = eval(input("input value for " + char + " : "))
             
         # operate
         for char in expression:
             if isOperand(char):
                stack.append(dic.get(char))
             else:
                # operand 2 is popped first, then operand 1
                op2 = stack.pop()
                op1 = stack.pop()
                # variable is the operator in function below
                answer = Evaluate(int(op1), int(op2), char) 
                stack.append(answer)

         # print final value or error
         if len(stack) == 1:
             print("Final Value: " + str(stack[0]))
         else:
             print("Error with Postfix expression")
             print(stack)

         # prompt for continuation
         cont = input("\tContinue(y/n)? ")
         if cont.lower() == 'n':
            goOn = False

if __name__ == "__main__":
    # calling main function
    main()
