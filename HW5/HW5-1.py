import sys;
import string;

###
###
### pig_latin without using regular expression
###
###

class Pig_latin:
    __vowels = ['a', 'i', 'u', 'e', 'o']
    __latin = "ay"

    def pigLationForWord(self):
        word = input("enter a word") #reaplce with input
        keep = self.getPigLatin(word);
        if word != keep:
            newWord = word.replace(keep,"")
            keep = keep + self.__latin;
            newWord = newWord + keep;
            return newWord
        else:
            return keep

    def pigLationForText(self):
        text = input("enter a text")#reaplce with input
        textSplit = text.split()
        newText = []
        for txt in textSplit:
            keep = self.getPigLatin(txt);
            if keep != txt:
                newWord = txt.replace(keep,"")
                keep = keep + self.__latin;
                newWord = newWord + keep;
                newText.append(newWord)
            else:
                newText.append(keep)

        return newText

    def getPigLatin(self, word):
        keep = ""
        for i in word:
            for j in self.__vowels:
                if(i == j):
                    return keep;
                if(j == 'o' and i != j):
                    keep = keep + i
        return keep
    
###
###
### pig_latin using regular expression
###
###
class PigLatin:

    def getPigLatinInWord(self):
            word = "banana"#input("enter a word") #reaplce with input
            reg = re.compile(r'((a|i|u|e|o)\w*)')
            pig = re.findall(reg, word)
            if(pig != []):
                loop = len(word) - len(pig[0][0]) #pig[0][0] is the  longest string
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


pig = Pig_latin();

print(pig.pigLationForWord());
print(pig.pigLationForText());
