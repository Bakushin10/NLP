# Shin Nagai
# 4/8/2018
# HW9
import nltk
from nltk.corpus import brown

class HW9:
    def precision(gold, test, tag):
        TN, TP, FP, FN = 0, 0, 0, 0
        for i in range(len(test)):
            if (gold[i][1] == tag) and (test[i][1] == tag):
                TP += 1
            elif (gold[i][1] != tag) and (test[i][1] == tag):
                FP += 1
            elif (gold[i][1] == tag) and (test[i][1] != tag):
                FN += 1
            elif (gold[i][1] != tag) and (test[i][1] != tag):
                TN += 1
        print(TN, TP, FP, FN)
        return (TP)/(TP+FP)

    def recall(gold, test, tag):
        TN, TP, FP, FN = 0, 0, 0, 0
        for i in range(len(test)):
            if (gold[i][1] == tag) and (test[i][1] == tag):
                TP += 1
            elif (gold[i][1] != tag) and (test[i][1] == tag):
                FP += 1
            elif (gold[i][1] == tag) and (test[i][1] != tag):
                FN += 1
            elif (gold[i][1] != tag) and (test[i][1] != tag):
                TN += 1
        return (TP)/(TP+FN)

    def fMeasure(gold, test, tag):
        p = precision(gold, test, tag)
        r = recall(gold, test, tag)
        if(p == 0 or r == 0):
            return 0
        return (2*p*r)/(p*r)

    # def confusinMatrixCategories(gold, test, tag, TN, TP, FP, FN, i):
    #     if (gold[i][1] == tag) and (test[i][1] == tag):
    #         TP += 1
    #     elif (gold[i][1] != tag) and (test[i][1] == tag):
    #         FP += 1
    #     elif (gold[i][1] == tag) and (test[i][1] != tag):
    #         FN += 1
    #     elif (gold[i][1] != tag) and (test[i][1] != tag):
    #         TN += 1


gold = brown.tagged_words(categories='news')
test = brown.tagged_words(categories='editorial')
tag = "NN-HL"
precision(gold, test, tag)
recall(gold, test, tag)
fMeasure(gold, test, tag)
