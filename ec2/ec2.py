import glob
import codecs
import re
import nltk
import random


class EC2:
    def loadFile(self):
        text = ""
        humanWords = []
        robotsWords = []
        for eachFile in glob.glob("Desktop/UF/Spring-2018/NLP/github-repo/NLP/ec2/Loebner-logs-2003/*/*.log"):
            with codecs.open(eachFile, "r", encoding='utf-8', errors='ignore') as file:
                    print("opening...", eachFile)
                    text = file.readlines()
                    PROGRAM_list = self.trimPROGRAM(text, humanWords, robotsWords)

        # creating the feature...
        humanWords = self.joinList(humanWords)
        robotsWords = self.joinList(robotsWords)
        wordList = humanWords + robotsWords
        features = self.createFeature(wordList)
        random.shuffle(features)
        print(len(features))
        train_set, test_set = features[:3000], features[3000:]
        classifier = nltk.NaiveBayesClassifier.train(train_set)
        print(nltk.classify.accuracy(classifier, test_set))
        print(classifier.show_most_informative_features(10))

    def createFeature(self, wordList):
        features = [(self.word_feature(word), entity) for (word, entity) in wordList]
        return features

    def word_feature(self, word):
        return {"word": word}

    def trimPROGRAM(self, text, humanWords, robotsWords):
        findHuman = re.compile('CONFEDERATE')
        findHuman2 = re.compile('JUDGE')
        extractText = re.compile('[A-Z]*: .*\r')
        for line in text:
            fh = findHuman.findall(line)
            fh2 = findHuman2.findall(line)

            if fh == [] and fh2 == []:  # if the message is written by a robot
                message = extractText.findall(line)
                onlyText = self.removeCapitalSequence(message)
                newList = self.label_word(onlyText, "ROBOTS")
                robotsWords.append(newList)
                # print("ROBOTS:", onlyText)
            else:  # if the message is written by a human
                message = extractText.findall(line)
                onlyText = self.removeCapitalSequence(message)
                newList = self.label_word(onlyText, "HUMAN")
                humanWords.append(newList)
                # print("HUMAN:", onlyText)

    def label_word(self, text, entity):
        text = nltk.word_tokenize(text)
        labeled_word = [(word, entity) for word in text]
        return labeled_word

    def joinList(self, lists):
        mergeList = []
        for list in lists:
            mergeList = mergeList + list
        return mergeList

    def removeCapitalSequence(self, message):
        removed = False
        removeWord = ""
        message = ''.join(message)
        message = message.replace('\r', "")
        trimmedMessage = ""
        for c in message:
            if c == ':' and removed is False:
                removeWord = removeWord + c
                trimmedMessage = message.replace(removeWord, "")
                removed = True
            elif c.isupper() and removed is False:
                removeWord = removeWord + c
        return trimmedMessage


ec = EC2()
ec.loadFile()
