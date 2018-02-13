import sys;
import string;

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
        textSplitted = text.split()
        newText = []
        for txt in textSplitted:
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


pig = Pig_latin();

print(pig.pigLationForWord());
print(pig.pigLationForText());
