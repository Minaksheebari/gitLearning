#refer PDF Advance CHallenge String from python Notes folder
#Code Academy Challange 2 for python Strings Advance
#Check if name exist in sentence or not
def checkName(sentance,name):
    if name.lower() in sentance.lower():
        return True
    return False

print(checkName("My name is minu",'si'))

#Every other letter extraction

def Eol(word):
    stringHolder = ""
    for i in range(0,len(word),2):
        stringHolder += word[i]
    return stringHolder

print(Eol("Minakshee"))

#Reverse

def reverse(word):
    reverseString = ""
    for i in range(len(word)-1,-1,-1):
        reverseString += word[i]
    return reverseString
print(reverse("RAJ"))


#make spoonerism

def spoon(firstword,secondword):
    return secondword[0]+firstword[1:] + " " + firstword[0]+secondword[1:]

print(spoon('Jelly','Beans'))
print(spoon('Fix','Bench'))

#Add exclamation

def exclamation(sentence):
    while len(sentence)<20: 
        sentence += '!'
    return sentence

print(exclamation("Hello minu"))