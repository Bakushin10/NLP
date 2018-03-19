
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
        xsquare = self.xSquare(w1w2, w1Nw2, Nw1w2, Nw1Nw2)
        print("C(w1) :          # ", w1)
        print("C(w2) :          # ", w2)
        print("C(w1w2):         # ", w1w2)
        print("C(w1 && !w2):    # ", w1Nw2)
        print("C(!w1 && w2):    # ", Nw1w2)
        print("C(!w1 && !w2):   # ", Nw1Nw2)
        print("\n\n'0.05% Baseline: 3.841'\nX^2# ", xsquare)

    def xSquare(self, w1w2, w1Nw2, Nw1w2, Nw1Nw2):
        if w1w2 == 0:
            w1w2 = 1
        # percentage
        w2_percent = (w1w2 + Nw1w2)
        Nw2_percent = (w1Nw2 + Nw1Nw2)
        total = w2_percent + Nw2_percent
        w2_percent = w2_percent / total
        Nw2_percent = Nw2_percent / total
        # total w1
        w1_total = w1w2 + w1Nw2
        Nw1_total = Nw1w2 + Nw1Nw2
        # expected value
        # w1w2_expected = w1_total * w2_percent
        # w1Nw2_expected = w1_total * Nw2_percent
        # Nw1w2_expected = Nw1_total * w2_percent
        # Nw1Nw2_expected = Nw1_total * Nw2_percent
        print("C(w1w2):         # ", w1w2)
        print("C(w1 && !w2):    # ", w1Nw2)
        print("C(!w1 && w2):    # ", Nw1w2)
        print("C(!w1 && !w2):   # ", Nw1Nw2)
        print("w2_percent :     # ", w2_percent)
        print("Nw2_percent :    # ", Nw2_percent)
        print("w1_total :       # ", w1_total)
        print("Nw1_total :       # ", Nw1_total)

        sum = 0
        i = 0
        observedValue = [
            w1w2,
            w1Nw2,
            Nw1w2,
            Nw1Nw2
        ]
        expectedValues = [
            w1_total * w2_percent,
            w1_total * Nw2_percent,
            Nw1_total * w2_percent,
            Nw1_total * Nw2_percent
        ]

        for i in range(4):

            numerator1 = (observedValue[i] - expectedValues[i])
            numerator2 = math.pow(numerator1, 2)  # x^2
            x = numerator2/observedValue[i]

            print(observedValue[i], ' - ', expectedValues[i])
            print(' X^2 ', math.pow(numerator1, 2))
            print('sum', numerator2/observedValue[i])
            print('\n\n')
            sum = sum + x

        return sum

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


from nltk.corpus import brown
brown = brown.words()
c = chi_square()
c.getChiSquare("new", "companies", brown)


# t = Tvalue()
# t.generateTvalue("have", "had", "to", brown)
