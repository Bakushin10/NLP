
#"Desktop/UF/Spring-2018/NLP/github-repo/NLP/HW6/SBCorpus/TRN/SBC001.trn"
import glob
import codecs
import re

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
        # for a in token:
        #     print(a)
        print("Done")


    def getMatch(self, token, message):
        bigrams = nltk.bigrams(token)
        bigramList = list(bigrams)
        fdistForToken = nltk.FreqDist(token)
        fdistForBigram = nltk.FreqDist(bigramList)


    def trimm_text(self,token):
        # token = "0.00 2.98 #MONTOYA: What How [can you teach a three-year-old to] ta=p [2dance2]. (COUGH) by n[ow],"
        # token = nltk.word_tokenize(token)
        print(len(token))
        timeStamps = re.compile('(\d{1,}.\d{1,})')
        name = re.compile('(([A-Z]){2,})')
        #special = re.compile('({1})')

        trimmed = [w for w in token
                    if not name.match(w) and not timeStamps.match(w)]
        print("----------")

        print(len(trimmed))
        return trimmed


        # bigramList = nltk.bigrams(words)
        # fdist1 = nltk.FreqDist(text)
h = HW6()
h.loadFile()
