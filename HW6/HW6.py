
import glob
import codecs
import re
import json
import nltk
wordDict = nltk.corpus.words.words()
T9 ={
    'a':'abc', 'b':'abc', 'c':'abc', 'd':'def', 'e':'def', 'f':'def', 'g':'ghi', 'h':'ghi', 'i':'ghi',
    'j':'jkl', 'k':'jkl', 'l':'jkl', 'm':'mno', 'n':'mno', 'o':'mno', 'p':'pqrs', 'q':'pqrs', 'r':'pqrs',
    's':'pqrs','t':'tuv', 'u':'tuv', 'v':'tuv', 'w':'wxyz', 'x':'wxyz', 'y':'wxyz', 'z':'wxyz'
    }
class HW6:

    def loadFile(self):
        text = ""
        message = "I an really out me it. I lost ox bbq. Can wot bone un het of?"

        for eachFile in glob.glob("Desktop/UF/Spring-2018/NLP/github-repo/NLP/HW6/SBCorpus/TRN/*.trn"):
            with codecs.open(eachFile,"r",encoding='utf-8', errors='ignore') as file:
                    print("opening...", eachFile)
                    text = text + file.read()

        print("calculating token...")
        token = nltk.word_tokenize(text)
        token = self.trimm_text(token)
        self.getMatch(token,message)

    def getMatch(self, token, message):
        message = nltk.word_tokenize(message)
        message = nltk.bigrams(message)
        messageList = list(message)
        conversationCorpusText = token
        conversationCorpus = nltk.bigrams(token)
        conversationCorpus = list(conversationCorpus)
        newList = []
        for w in messageList:
            print(w)
            if w in conversationCorpus:
                print("in conversationCorpus")
                newList.append(w)
            else:
                print(w, " NOT in conversationCorpus")
                value = self.checkPossibleConbinations(w, conversationCorpus)
                if value is not None:
                    newList.append(value)
                else:
                    newList.append(w)

        incompletedSentense = ""
        print(newList)
        for i in range(len(newList)):
            print(newList[i][0]," ",newList[i][1])
            if i == 0:
                incompletedSentense = incompletedSentense + newList[i][0] + " " + newList[i][1]
            elif newList[i-1][1] == newList[i][0]:
                incompletedSentense = incompletedSentense + " " + newList[i][1]
            else:
                incompletedSentense = incompletedSentense + " "+ newList[i][0] + " " + newList[i][1]

        incompletedSentense = nltk.word_tokenize(incompletedSentense)
        finalSentence = self.trimIncompletedSentence(newList,conversationCorpusText, conversationCorpus, incompletedSentense)
        print("#\n#\n#words are...\n#\n#\n")
        print(finalSentence)

    def trimIncompletedSentence(self, bigrams,conversationCorpusText, conversationCorpusBigram, incompletedSentense):
        print("incompletedSentense"," : ", incompletedSentense)
        for i in range(len(bigrams)):
            if i+1 < len(bigrams):
                bi1 = bigrams[i]
                bi2 = bigrams[i][0] +" "+ bigrams[i+1][0]
                bi2 = nltk.word_tokenize(bi2)
                bi2 = nltk.bigrams(bi2)

                print("-------------------")
                print(bi1)
                for a in bi2:
                    print(a)
                    bi2 = a

                if bi1 != bi2:
                    fdist1 = nltk.FreqDist(conversationCorpusText)
                    fdist2 = nltk.FreqDist(conversationCorpusBigram)
                    ratioNum1 = float(fdist2[bi1])
                    ratioNum2 = float(fdist2[bi2])
                    ratioDen1 = fdist1[bi1[0]] + fdist1[bi1[1]]
                    ratioDen2 = fdist1[bi2[0]] + fdist1[bi2[1]]
                    ratio1 = ratioNum1 / ratioDen1;
                    ratio2 = ratioNum2 / ratioDen2;
                    print(bi1, "  ", bi2)
                    print(ratio1, "  ", ratio2)
                    searchWord = bigrams[i][0] +" "+ bigrams[i][1]
                    searchWord = nltk.word_tokenize(searchWord)

                    wordBegin = 0
                    for i in range(len(incompletedSentense)):
                        if i+1 < len(incompletedSentense):
                            compare = incompletedSentense[i] + " " + incompletedSentense[i+1]
                            compare = nltk.word_tokenize(compare)
                            if searchWord == compare:
                                wordBegin = i
                                print(searchWord," ", compare)
                                print("find! at wordBegin:"," ", wordBegin)
                    for i in range(2):
                        if ratio1 > ratio2:
                            incompletedSentense[wordBegin + i] = bi1[i]
                        else:
                            incompletedSentense[wordBegin + i] = bi2[i]
                    print(incompletedSentense)
                    incompletedSentense = incompletedSentense[:wordBegin+2] + incompletedSentense[wordBegin+3:]
                    print(incompletedSentense)
                print("-------------------")
        return incompletedSentense

    def checkPossibleConbinations(self, w, conversationCorpus):
        w = json.dumps(w)
        words = re.findall(r'(\b[a-z]{1,}\b)', w)

        for i in range(len(words)):
            reModel = ""
            for letter in words[i]:
                reModel = reModel+'[' + T9[letter] + ']' #generate regular expression for possible words
            print(reModel)
            possibleWords = re.findall(r'\b%s\b'%reModel, json.dumps(wordDict))
            if i == 0:
                firstList = possibleWords
            if i == 1:
                print("possibleWords are...")
                print(firstList)
                print(possibleWords)
                secondList = possibleWords
                return self.calculateWordFrequency(firstList, possibleWords, conversationCorpus)

    def calculateWordFrequency(self, firstList, secondList, conversationCorpus):
        for f in firstList:
            for s in secondList:
                bigrams = f+" "+s
                bigrams = nltk.word_tokenize(bigrams)
                bigrams = nltk.bigrams(bigrams)
                for a in bigrams:
                    print(a)
                    if a in conversationCorpus:
                        print(a, "in conversationCorpus\n")
                        return a;

    def trimm_text(self,token):
        timeStamps = re.compile('(\d{1,}.\d{1,})')
        name = re.compile('(([A-Z]){2,})')
        special = re.compile('\W')

        trimmed = [w for w in token
                    if not name.match(w) and not timeStamps.match(w) and not special.match(w)]
        return trimmed

h = HW6()
h.loadFile()
