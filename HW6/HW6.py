
#"Desktop/UF/Spring-2018/NLP/github-repo/NLP/HW6/SBCorpus/TRN/SBC001.trn"
import glob
import codecs
import re
import json
wordDict = nltk.corpus.words.words()
T9 ={
    'a':'abc', 'b':'abc', 'c':'abc', 'd':'def', 'e':'def', 'f':'def', 'g':'ghi', 'h':'ghi', 'i':'ghi',
    'j':'jkl', 'k':'jkl', 'l':'jkl', 'm':'mno', 'n':'mno', 'o':'mno', 'p':'pqrs', 'q':'pqrs', 'r':'pqrs',
    's':'pqrs','t':'tuv', 'u':'tuv', 'v':'tuv', 'w':'wxyz', 'x':'wxyz', 'y':'wxyz', 'z':'wxyz'
    }
class HW6:
    # with open('SBCorpus/TRN/SBC001.trn') as file:
    #         text = file.read()
        #print(glob.glob("SBCorpus/TRN/*.trn"))

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
        print(len(token))
        print("Done")

    def getMatch(self, token, message):
        message = nltk.word_tokenize(message)
        message = nltk.bigrams(message)
        messageList = list(message)
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
        print(newList)
        for w in list(newList):
            print(w)

        # bigrams = nltk.bigrams(token)
        # bigramList = list(bigrams)
        # fdistForToken = nltk.FreqDist(token)
        # fdistForBigram = nltk.FreqDist(bigramList)
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

        # bigramList = nltk.bigrams(words)
        # fdist1 = nltk.FreqDist(text)
h = HW6()
h.loadFile()
