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


def process(someFile, isPreamble=True):
        retlist = []
        chickenTime = not isPreamble; #if there's no preamble, it's already chicken time
        for line in someFile:
                word = ""
                newline = ""

                #prechicken or postchicken?
                if not chickenTime: #begin document not yet seen
                        retlist.append(line)
                        if "begin{document}" in line:
                                chickenTime = True
                                print("beginning chickening process")
                elif "\\end{" in line or "\\begin{" in line or "\\pagestyle{" in line: #TODO width=
                #sorts of settings and graphics in general
                                retlist.append(line)
                                #chickenTime = False TODO logic?
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


#run stuff; fix thsi too
from sys import argv


if len(argv) < 2:
        print ("error: syntax is: chicken.py filename --nopreamble")
else:
        
        inFile = open(argv[1], 'r')
        out = open("chicken-"+argv[1], 'w')
        fileAsList = inFile.readlines()

        if len(argv) == 2:
                chickened = process(fileAsList, True)
        else: #assuming equals --nopreamble or --nopa; TODO is fix this assumption
                chickened = process(fileAsList, False)

        for line in chickened:
                out.write(line)




