#
#   2/16/2018
#   HW 5.1 Pig_latin
#   Shin Nagai
#
#
#

import re

class PigLatin:

    def getPigLatinInWord(self):
            word = input("Enter : ")#input("enter a word") #reaplce with input
            reg = re.compile(r'((a|i|u|e|o)\w*)')
            pig = re.findall(reg, word)
            if(pig != []):
                loop = len(word) - len(pig[0][0])
                pig_latin = pig[0][0]
                for n in range(loop):
                     pig_latin += word[n]
                pig_latin += "ay"
                print(pig_latin)
            else:
                print(word)

    def getPigLatinInSentence(self):
        sentence = input("Enter : ")
        sentence = sentence.split();
        for word in sentence:
            reg = re.compile(r'((a|i|u|e|o)\w*)')
            pig = re.findall(reg, word)
            if(pig != []):
                loop = len(word) - len(pig[0][0])
                pig_latin = pig[0][0]
                for n in range(loop):
                     pig_latin += word[n]
                pig_latin += "ay"
                print(pig_latin)
            else:
                print(word)

p = PigLatin()
p.getPigLatinInSentence()
