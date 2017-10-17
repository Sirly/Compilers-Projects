# CPSC 323 Programming Assignment # 4
# Authors:
#       Kevin Nakashima
#
#   Write a program to parse a file with multiple statements for readability
#
#   Created: 9/16/2017
#   Updated: 9/19/2017
#
#   Notes: data.txt must be in local folder
#       in data.txt format for words are as:
#       <statement1>;
#   or  <statement2>; <statement3>;
#   or  //  ....

def main():
    # given arrays
    resWords = ["cout<<", "for", "int", "while"]
    special = ["=", "*", "-", "(", ")", ";", "<=", ">=", "+"]
    words = []
    newLines = []
    
    # read words from file
    with open("data.txt") as f:
        words = f.readlines()

    # traverse array in reverse order for deletion simplification
    for i in range(len(words)-1, -1, -1):
        # remove all lines with only a '\n' character and comments
        if words[i] == "\n" or words[i].startswith("//"):
            del words[i]
        else:
            temp = words[i]
            temp = temp.split("//")
            words[i] = temp[0]
        # give special characters space between them
        for c in special:
            words[i] = words[i].replace(c," "+c+" ")
        # remove extra white space
        while "  " in words[i]:
            words[i] = words[i].replace("  "," ")
        # remove \s at beginning of string
        while words[i].startswith(" "):
            words[i] = words[i][1:]
        # remove \n since they'll be printed by print() to file
        words[i] = words[i].replace('\n', '')
        # remove \t
        words[i] = words[i].replace('\t', '')

    # separate by semicolon if more than one statement per line
    for i in range(len(words)):
        if words[i].count(';') > 1:
            temp = words[i].split(';')
            del temp[-1]
            for l in temp:
                # remove \s at beginning of string
                while l.startswith(" "):
                    l = l[1:]
                newLines.append(l+';\n')
        else:
            newLines.append(words[i]+'\n')

    # print new lines to 'newdata.txt'
    with open("newdata.txt", 'w') as f:
        for line in newLines:
            f.write(line)

    
if __name__ == '__main__':
    main()
