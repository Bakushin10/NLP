
import nltk
import re
import math
# how to load corpus
# from nltk.corpus import brown
# brown = brown.words()


class Tvalue:
    message = "hello"

    def printMessage(self):
        print(self.message)

    def findWord(self, word, text):
        text = list(text)
        i = 0
        for n in text:
            if word == n:
                i = i + 1

        return i

    def generateTvalue(self, w1, w2, W, text):
        c1 = self.findCollocation(w1, W, text)
        c2 = self.findCollocation(w2, W, text)
        numerator = c1 - c2
        denominator = math.sqrt(c1 + c2)
        tValue = numerator / denominator
        print(numerator, "/", denominator, "=", tValue)

    def findCollocation(self, targetWord, W, text):
        text = ' '.join(text)
        bigram = targetWord+" " + W
        count = 0
        # bigram = [bi]
        # for i in bigram:
        count = len(re.findall(bigram, text))
        print("'", bigram, "' : ", count, " times")
        return count


class chi_square:
    def getChiSquare(self, word1, word2, text):
        print("calculating...")
        w1 = self.singleWord(word1, text)
        w2 = self.singleWord(word2, text)
        w1w2 = self.bigram(word1, word2, text)
        w1Nw2 = self.w1_And_Not_w2(word1, text)
        Nw1w2 = self.not_w1_And_w2(word2, text)
        Nw1Nw2 = self.not_w1_and_not_w2(w1w2, text)
        print("C(w1) :          # ", w1)
        print("C(w2) :          # ", w2)
        print("C(w1w2):         # ", w1w2)
        print("C(w1 && !w2):    # ", w1Nw2)
        print("C(!w1 && w2):    # ", Nw1w2)
        print("C(!w1 && !w2):   # ", Nw1Nw2)

    def singleWord(self, word, text):
        text = ' '.join(text)
        count = len(re.findall(word, text))
        return count

    def bigram(self, w1, w2, text):
        text = ' '.join(text)
        bigrams = w1+' '+w2
        print(bigrams)
        count = len(re.findall(bigrams, text))
        return count

    def w1_And_Not_w2(self, w1, text):
        text = ' '.join(text)
        combination = re.compile('\s{1}'+w1+'\s{1}\w+\s{1}')
        count = len(re.findall(combination, text))
        return count

    def not_w1_And_w2(self, w2, text):
        text = ' '.join(text)
        combination = re.compile('\s{1}\w+\s{1}'+w2+'\s{1}')
        count = len(re.findall(combination, text))
        return count

    def not_w1_and_not_w2(self, w1w2, text):
        text = ' '.join(text)
        totalBigrams = nltk.word_tokenize(text)
        return len(totalBigrams) - w1w2


c = chi_square()
c.getChiSquare("new", "companies", brown)


t = Tvalue()
t.generateTvalue("have", "had", "to", brown)
