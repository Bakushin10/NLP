import glob
import codecs
import re
import nltk


class EC2:
    def loadFile(self):
        text = ""
        features = {}
        for eachFile in glob.glob("Desktop/UF/Spring-2018/NLP/github-repo/NLP/ec2/Loebner-logs-2003/ALICE/*.log"):
            with codecs.open(eachFile, "r", encoding='utf-8', errors='ignore') as file:
                    print("opening...", eachFile)
                    text = file.read()
                    PROGRAM_list = self.trimPROGRAM(text)
                    JUDGE_list = self.trimJUDGE(text)
                    print("PROGRAM_list : ", len(PROGRAM_list))
                    print("JUDGE_list : ", len(JUDGE_list))
                    # features = self.build_feature(features, PROGRAM_list, JUDGE_list)
                    document = []
                    for i in range(len(JUDGE_list)):

                        index = {
                            'PROGRAM': PROGRAM_list[i],
                            'JUDGE': JUDGE_list[i]
                            }
                        document.append(index)

                    print(document)
                    # I need to create the feature based on the document
                    # document contains the list of conversation

    def build_feature(self, features, PROGRAM_list, JUDGE_list):
        # PROGRAM_words = set(PROGRAM_list)
        # JUDGE_words = set(JUDGE_list)
        for word in PROGRAM_list:
            features['contain({})'.format(word)]  # = (word in PROGRAM_list)
        for word in PROGRAM_list:
            features['contain({})'.format(word)]  # = (word in JUDGE_list)
        print("feature")
        print(features)
        return features

    def trimPROGRAM(self, text):
        findProgram = re.compile('PROGRAM: .*\r')
        trimmed = findProgram.findall(text)
        newTrimmed = []
        for word in trimmed:
            sent = word.replace("PROGRAM: ", "")  # removing 'PROGRAM :'
            sent = sent.replace("\r", "")         # removing '\r'
            newTrimmed.append(sent)
        return newTrimmed  # return the list of program

    def trimJUDGE(self, text):
        findProgram = re.compile('JUDGE: .*\r')
        trimmed = findProgram.findall(text)
        newTrimmed = []
        for word in trimmed:
            sent = word.replace("JUDGE: ", "")
            sent = sent.replace("\r", "")
            newTrimmed.append(sent)
        return newTrimmed  # return the list of program


ec = EC2()
ec.loadFile()
