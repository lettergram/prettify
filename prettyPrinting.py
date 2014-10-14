'''
Written by Austin Walters
For use on austingwalters.com
Feel free to use elsewhere, if link provided to,
http://austingwalters.com
'''

'''
Takes a phrase, and a line length and ensures
the text properly aligns with the margins (based on length).
'''
def prettify(phrase, length):

    phrase = phrase.replace("\n", " ")
    phrase = phrase.split(" ")

    prettyPhrase = []
    line = ""
    slack = 0

    for word in phrase:
        if len(line) + len(word) > length:
            prettyPhrase.append(line)
            slack += length - len(line)
            line = ""
        elif len(line) > 0:
            line += " "
        line += word 
    prettyPhrase.append(line)
    
    phrase = ""
    for line in prettyPhrase:
        phrase += line + "\n"    
    return phrase


'''
Loads a phrase/passage from a document
'''
def loadPhrase(filename):
    file = open(filename)
    phrase = ""
    for line in file:
        phrase += line
    return phrase

phrase = loadPhrase("testfile.txt")

print "\n\n\n---------- Phrase ----------\n\n" 
print phrase
print "\n---------- Prettify ----------\n\n"
print prettify(phrase, 39)



