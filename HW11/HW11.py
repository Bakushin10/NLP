import nltk


class HW11:
    def noun_phrase(self):
        # sentence = input('\n\nPlease enter a sentence\n\n')
        sentence = "the assistant managing editor and the receiving end"
        sentence = nltk.word_tokenize(sentence)
        sentence = nltk.pos_tag(sentence)

        grammar = """
            NP: {<DT><VBG><NN>}
            ANP: {<NN><VBG><NN>}
        """
        cp = nltk.RegexpParser(grammar)
        result = cp.parse(sentence)
        print(result)


h = HW11()
h.noun_phrase()
