# CPSC 323 Programming Assignment # 3 Part 2
# Authors:
#       Kevin Nakashima
#
#   Write a program to determine whether a word is accepted for a given Language
#
#   Created: 9/24/2017
#   Updated: -
#
#   Notes: input format:
#       <word1>$

def main():
    # declarations
    L = "a*(a+b)c*"
    stateTable = [[2,1,-1],
                [-1,-1,1],
                [2,1,1]]
    print("For Language L = " + L)
    while(True):
        # get word(s) from user or quit
        word = input("enter a word in <word>$ format, or 'q' to quit: ")
        if(word.lower() == 'q'):
            break
        # re-set col and state to 0
        col = 0
        state = 0
        for i in range(len(word)):
            if word[i] == 'a':
                col = 0
            elif word[i] == 'b':
                col = 1
            elif word[i] == 'c':
                col = 2
            elif word[i] == '$':
                if(state == 1 or state == 2):
                    print("word: " + word + " accepted")
                else:
                    print("word: " + word + " NOT accepted")
            elif word[i] not in L:
                print("word: " + word + " NOT accepted, " + word[i] + " not in L")
                break
            if stateTable[state][col] == -1:
                print("word: " + word + " NOT accepted")
                break
            else:
                state = stateTable[state][col]
            
if __name__ == '__main__':
    main()
