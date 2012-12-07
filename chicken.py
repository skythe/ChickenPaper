def chicken(word):
        toReturn = "chicken"
        if "." not in word:
                #All caps?
                if word == word.upper():
                        toReturn = toReturn.upper()

                #first letter capped only
                elif word[0] == word[0].upper():
                        toReturn = "Chicken"
                
                #plural
                elif word[-1] == "s":
                        if not word[-2] == "'":
                                toReturn = toReturn + "s"
                        else:
                                toReturn = toReturn + "'s"

        else:
                toReturn = "C.H.I.C.K.E.N."

        
        return toReturn


def process(someFile):
        retlist = []
        chickenTime = False;
        for line in someFile:
                word = ""
                newline = ""

                #prechicken or postchicken?
                if not chickenTime: #begin document not yet seen
                        retlist.append(line)
                        if "begin{document}" in line:
                                chickenTime = True
                elif "end{document}" in line:
                                retlist.append(line)
                                chickenTime = False
                else: #chicken
                        for char in line:
                                if char.isalpha() or char == "\\":
                                        word += char
                                else:
                                        if len(word) > 0:
                                                if word[0] == "\\":
                                                        newline += word
                                                else:
                                                        newline += chicken(word)
                                                word = ""
                                        
                                        newline += char
                
                        if len(word) > 0:
                                newline += chicken(word)
                                word = ""

                        retlist.append(newline)

        return retlist


from sys import argv

inFile = open(argv[1], 'r')
out = open("chicken-"+argv[1], 'w')
fileAsList = inFile.readlines()

chickened = process(fileAsList)

for line in chickened:
        out.write(line)


