# CPSC 323 Programming Assignment # 3 Part 1
# Authors:
#       Kevin Nakashima
#
#   Write a program to read a statement and determine whether each token is a:
#   number, identifier, reserved word, or special character.
#
#   Created: 9/9/2017
#   Updated: -
#
#   Notes: Each reserved word, number, special character, or other must
#       be separated by spaces to work. 


def main():
    # given arrays
    resWords = ["cout<<", "for", "int", "while"]
    special = ["=", "*", "-", ";", "(", ")", "<", ">", "<=", ">=", "+"]

    while(True):
                identifiers = []
                dic = dict()
                # get statement from user
                statement = input("Enter a statement: ")
                statement = statement.split(' ')
                
                # check if reserved word
                for i in range(len(statement)):
                        if statement[i] in resWords:
                                dic[statement[i]] = "reserved word"
                # check if special symbol
                        elif statement[i] in special:
                                dic[statement[i]] = "special symbol"
                # check if number
                        elif statement[i].isdigit():
                                dic[statement[i]] = "number"
                # check if identifier
                        # check for <int> id <=> since int is only variable type for this project
                        elif (statement[i - 1] == "int" and statement[i + 1] == "=") or (statement[i] in identifiers):
                                identifiers.append(statement[i])
                                dic[statement[i]] = "identifier"
                        else:
                                dic[statement[i]] = "not identifier"
                                
                # print dictionary
                for word in statement:
                        print(word + " \t" + dic[word])
                        
                # promt for coninuation
                cont = input("\tContinue(y/n)? ")
                if(cont.lower() == 'n'):
                        break
    
if __name__ == '__main__':
    main()
