import nltk, random, operator
from nltk.corpus import brown
from collections import defaultdict
from collections import Counter
from nltk.corpus import wordnet as wn

#
# python HashMap(dictionary)
#
# Usually, a Python dictionary throws a KeyError if you try to get an item with
# a key that is not currently in the dictionary. The defaultdict in contrast
# will simply create any items that you try to access (provided of course they do
# not exist yet). To create such a "default" item, it calls the function object
# that you pass in the constructor (more precisely, it's an arbitrary "callable"
# object, which includes function and type objects).


class HW10:
    def mostCommonPlural(self, corpus):
        tagged_word = nltk.pos_tag(corpus)
        dictionary = defaultdict(int)
        for word, tag in tagged_word:
            if tag == 'NNS':  # finding the plural
                tag_count = dictionary[word]
                tag_count += 1
                dictionary[word] = tag_count
                # print(word, tag, tag_count)

        maxCount = 0
        mostCommonPlu = ""
        for word, tag in tagged_word:
            if dictionary[word] > maxCount:
                maxCount = dictionary[word]
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

    def mostFrequentTag(self, corpus):
        tagged_word = nltk.pos_tag(corpus)
        tagList = [(tag) for word, tag in tagged_word]

        # Counter works like freqDist. and Counter is sortable
        sortedTagList = Counter(tagList).most_common()
        i = 0
        for each in sortedTagList:
            if i < 20:  # show 20 most frequent tag
                print((i+1), ":", each)
                i = i + 1

    def mostCommonTagAfterNoun(self, corpus):
        tagged_word = nltk.pos_tag(corpus)
        dictionary = defaultdict(int)
        size = len(tagged_word)
        for i in range(size):
            if tagged_word[i][1] == "NN" and i+1 < size:
                count = dictionary[tagged_word[i+1][1]]
                count += 1
                dictionary[tagged_word[i+1][1]] = count
        sortedDict = reversed(sorted(dictionary.items(), key=operator.itemgetter(1)))
        for each in sortedDict:
            print(each)

    def document_features(self, corpus):
        tagged_word = nltk.pos_tag(corpus)
        feature = [(self.create_feature(word), tag) for word, tag in tagged_word]
        print("printing out first 50 features...")
        i = 0
        for each in feature:
            if i < 50:
                print(each)
                i += 1

    def create_feature(self, word):
        return{"word": word,
               "synset": wn.synsets(word)}


corpus = brown.words(categories='news')
hw10 = HW10()

# question 1
hw10.mostCommonPlural(corpus)
hw10.mostDistinctTag(corpus)
hw10.mostFrequentTag(corpus)
hw10.mostCommonTagAfterNoun(corpus)

# question 2
hw10.document_features(corpus)
