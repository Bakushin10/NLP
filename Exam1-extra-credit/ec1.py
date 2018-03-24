
import nltk
import re
import math
# how to load corpus
# from nltk.corpus import brown
# brown = brown.words()


class Chi_square:
    def chi_square(self, word1, word2, originaltext):
        print("calculating...")
        text = []
        totalWord = 0
        for a in originaltext:
            text.append(a.lower())
            totalWord = totalWord + 1
        w1 = self.singleWord(word1, text)
        w2 = self.singleWord(word2, text)
        w1w2 = self.bigram(word1, word2, text)
        w1Nw2 = self.w1_And_Not_w2(word1, text)
        Nw1w2 = self.not_w1_And_w2(word2, text)
        Nw1Nw2 = self.not_w1_and_not_w2(w1w2, w1Nw2, totalWord)
        xsquare = self.xSquare(w1w2, w1Nw2, Nw1w2, Nw1Nw2)
        print("C(w1) :          # ", w1)
        print("C(w2) :          # ", w2)
        print("C(w1w2):         # ", w1w2)
        print("C(w1 && !w2):    # ", w1Nw2)
        print("C(!w1 && w2):    # ", Nw1w2)
        print("C(!w1 && !w2):   # ", Nw1Nw2)
        print("total Word:      # ", totalWord)
        print("\n\n'0.05% Baseline: 3.841'\nX^2# ", xsquare)
        if(xsquare > 3.841):
            print("Reject null hypothesis :", word1, " and ", word2, "collocation")
        else:
            print("Accept null hypothesis :", word1, " and ", word2, "NOT collocation")

    def xSquare(self, w1w2, w1Nw2, Nw1w2, Nw1Nw2):
        # percentage
        w2_percent = (w1w2 + Nw1w2)
        Nw2_percent = (w1Nw2 + Nw1Nw2)
        total = w2_percent + Nw2_percent
        w2_percent = w2_percent / total
        Nw2_percent = Nw2_percent / total
        # total w1
        w1_total = w1w2 + w1Nw2
        Nw1_total = Nw1w2 + Nw1Nw2
        # print("C(w1w2):         # ", w1w2)
        # print("C(w1 && !w2):    # ", w1Nw2)
        # print("C(!w1 && w2):    # ", Nw1w2)
        # print("C(!w1 && !w2):   # ", Nw1Nw2)
        # print("w2_percent :     # ", w2_percent)
        # print("Nw2_percent :    # ", Nw2_percent)
        # print("w1_total :       # ", w1_total)
        # print("Nw1_total :       # ", Nw1_total)

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
            x = numerator2/expectedValues[i]

            # print(observedValue[i], ' - ', expectedValues[i])
            # print(' X^2 ', math.pow(numerator1, 2))
            # print('sum', numerator2/expectedValues[i])
            # print('\n\n')
            sum = sum + x

        return sum

    def singleWord(self, word, text):
        freqDist = nltk.FreqDist(text)
        return freqDist[word]

    def bigram(self, w1, w2, text):
        text = ' '.join(text)
        bigrams = w1+' '+w2
        count = len(re.findall(bigrams, text))
        return count

    def w1_And_Not_w2(self, w1, text):
        text = ' '.join(text)
        combination = re.compile('\s{1}?'+w1+'\s{1}\w+\s{1}?')
        count = len(re.findall(combination, text))
        return count

    def not_w1_And_w2(self, w2, text):
        text = ' '.join(text)
        combination = re.compile('\w+\s{1}'+w2)
        count = len(re.findall(combination, text))
        return count

    def not_w1_and_not_w2(self, w1w2, w1Nw2, total):
        return total - w1w2 - w1Nw2


from nltk.corpus import brown
brown = brown.words()
c = Chi_square()
c.chi_square("new", "companies", brown)
