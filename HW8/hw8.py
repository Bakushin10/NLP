import nltk, re
from nltk.corpus import brown, treebank


class POS_Tag_Data:
    # given a corpus,
    # place the tuples of word/tag pairs into tagged
    # make the words in tagged / words lists lower case
    # use the punctuation selection provided
    def __init__(self, corpus, punctuation=False, universal=True):
        if universal:
            tagged = corpus.tagged_words(tagset='universal')
        else:
            tagged = corpus.tagged_words()
        tags = [(pos) for (word, pos) in tagged if word.isalpha()]
        tags = set(tags)
        words = [(word) for (word, pos) in tagged if word.isalpha()]
        # when punctuation is False, take it out
        # when universal is True, use the universal tagset
        self.tagged = tagged
        self.tags = tags
        self.words = words

    # find all index positions of the tag provided
    def all_tag_inds(self, tag):
        inds = [(word) for (word, _tag) in self.tagged if _tag == tag]
        # print(inds[:50])
        return inds

    # find all index positions of the word provided
    def all_word_inds(self, word):
        inds = [(i) for (i) in range(len(self.tagged)) if self.tagged[i][0] == word]
        # print(inds[:50])
        return inds


ptd_brown = POS_Tag_Data( brown )
noun_inds = ptd_brown.all_tag_inds( 'NOUN' )
work_inds = ptd_brown.all_word_inds( 'work' )

ptd_treebank = POS_Tag_Data( treebank, universal=False )
nnp_inds = ptd_treebank.all_tag_inds( 'NNP' )
work_inds = ptd_treebank.all_word_inds( 'work' )
