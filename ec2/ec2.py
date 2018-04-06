import glob
import codecs
import re
import nltk


class EC2:
    def loadFile(self):
        text = ""
        humanWords = []
        robotsWords = []
        for eachFile in glob.glob("Desktop/UF/Spring-2018/NLP/github-repo/NLP/ec2/Loebner-logs-2003/ALICE/*.log"):
            with codecs.open(eachFile, "r", encoding='utf-8', errors='ignore') as file:
                    print("opening...", eachFile)
                    text = file.readlines()
                    PROGRAM_list = self.trimPROGRAM(text, humanWords, robotsWords)
                    # print(humanWords)
                    # print("______________________________\n\n\n")
                    # print(robotsWords)
        humanWords = self.joinList(humanWords)
        robotsWords = self.joinList(robotsWords)
        features = humanWords + robotsWords
        print(features)
        print(len(features))
        # self.build_feature(humanWords)
    # I need to create the feature based on the document
    # document contains the list of conversation
    # print(document)
    def build_feature(self, document):
        features = {}
        for list in document:
            features = [(word, entity) for word, entity in list]
        print(features)
        # feature_set = [(p, j) for p, j in document]  # p = program, j = j
        # return feature_set

    def trimPROGRAM(self, text, humanWords, robotsWords):
        findHuman = re.compile('CONFEDERATE')
        findHuman2 = re.compile('JUDGE')
        extractText = re.compile('[A-Z]*: .*\r')
        for line in text:
            fh = findHuman.findall(line)
            fh2 = findHuman2.findall(line)

            if fh == [] and fh2 == []:
                message = extractText.findall(line)
                onlyText = self.removeCapitalSequence(message)
                newList = self.label_word(onlyText, "ROBOTS")
                robotsWords.append(newList)
                # print("ROBOTS:", onlyText)
            else:
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
