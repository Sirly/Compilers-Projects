# CPSC 323 Programming Assignment # 3 Part 2
# Authors:
#       Kevin Nakashima
#
#   Write a program to determine whether a word is accepted for a given Language
#
#   Created: 9/9/2017
#   Updated: 9/10/2017
#
#   Notes: data.txt must be in the local folder
#       in data.txt, format for words are:
#       <word1>$
#       <word2>$

def main():
    words = []
    # read words from file
    with open("data.txt") as f:
        words = f.readlines()
    
    # strip off \n
    for i in range(len(words)):
        words[i] = words[i][:-1]
        
    # declarations
    L = "aa*b+bb*"
    stateTable = [[1,3],
             [1,2],
             [-1,-1],
             [-1,3]]
    print("For Language L = " + L)
    
    for w in words:
        col = 0
        state = 0
        for i in range(len(w)):
            if w[i] == 'a':
                col = 0
            elif w[i] == 'b':
                col = 1
            elif w[i] == '$':
                if(state == 2 or state == 3):
                    print("word: " + w + " accepted")
                else:
                    print("word: " + w + " NOT accepted")
            elif w[i] not in L:
                print("word: " + w + " NOT accepted, " + w[i] + " not in L")
                break
            state = stateTable[state][col]
            
    
    
if __name__ == '__main__':
    main()
