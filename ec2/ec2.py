import glob
import codecs
import re
import nltk


class EC2:
    def loadFile(self):
        text = ""
        document = []
        for eachFile in glob.glob("Desktop/UF/Spring-2018/NLP/github-repo/NLP/ec2/Loebner-logs-2003/ALICE/*.log"):
            with codecs.open(eachFile, "r", encoding='utf-8', errors='ignore') as file:
                    print("opening...", eachFile)
                    text = file.read()
                    PROGRAM_list = self.trimPROGRAM(text)
                    JUDGE_list = self.trimJUDGE(text)
                    print("PROGRAM_list : ", len(PROGRAM_list))
                    print("JUDGE_list : ", len(JUDGE_list))

                    # build the document
                    for i in range(len(JUDGE_list)):
                        index = {
                             PROGRAM_list[i],
                             JUDGE_list[i]
                            }
                        document.append(index)
                    print(len(document))

        features = self.build_feature(document)

    # I need to create the feature based on the document
    # document contains the list of conversation
    # print(document)
    def build_feature(self, document):
        feature_set = [(p, j) for p, j in document]  # p = program, j = judge
        return feature_set

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
