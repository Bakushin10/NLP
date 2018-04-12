
import nltk
import random
from nltk.corpus import brown
from collections import defaultdict
from collections import Counter
from nltk.corpus import wordnet as wn


class HW10:
    def mostCommonPlural(self, corpus):
        tagged_word = nltk.pos_tag(corpus)
        dictionary = defaultdict(list)
        for word, tag in tagged_word:
            if tag == 'NNS':  # finding the plural
                tag_count = dictionary[word]
                tag_count.append(tag)
                dictionary[word] = tag_count
                # print(word, tag, tag_count)

        maxCount = 0
        mostCommonPlu = ""
        for word, tag in tagged_word:
            if len(dictionary[word]) > maxCount:
                maxCount = len(dictionary[word])
                mostCommonPlu = word
        print("The most common plural  '", mostCommonPlu, "' appears ", maxCount, "times")

    def mostDistinctTag(self, corpus):
        tagged_word = nltk.pos_tag(corpus)
        dictionary = defaultdict(list)
        for word, tag in tagged_word:
            tagList = dictionary[word]
            if tag not in tagList:
                tagList.append(tag)
                dictionary[word] = tagList

        maxCount = 0
        mostDistinctTaggedWord = ""
        taggedList = []
        for word, tag in tagged_word:
            if len(dictionary[word]) > maxCount:
                maxCount = len(dictionary[word])
                mostDistinctTaggedWord = word
                taggedList = dictionary[word]
        print("The most tagged word  '", mostDistinctTaggedWord, ": ", taggedList)

    def mostFrequestTag(self, corpus):
        tagged_word = nltk.pos_tag(corpus)
        tagList = [(tag) for word, tag in tagged_word]

        # Counter works like freqDist. and sotable
        sortedTagList = Counter(tagList).most_common()
        i = 0
        for each in sortedTagList:
            if i < 20:  # show 20 most frequesnt tag
                print((i+1), ":", each)
                i = i + 1

    def document_features(self, corpus):
        tagged_word = nltk.pos_tag(corpus)
        feature = [(self.create_feature(word), tag) for word, tag in tagged_word]
        for each in feature:
            print(each)

    def create_feature(self, word):
        return{"word": word,
               "synset": wn.synsets(word)}


corpus = brown.words(categories='news')
hw10 = HW10()

# question 1
hw10.mostCommonPlural(corpus)
hw10.mostDistinctTag(corpus)
hw10.mostFrequestTag(corpus)

# question 2
hw10.document_features(corpus)
