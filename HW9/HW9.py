# Shin Nagai
# 4/6/2018
# HW9
import nltk
from nltk.corpus import brown

# Precision,
# which indicates how many of the items that we identified
# were relevant, is TP/(TP+FP).

# Recall,
# which indicates how many of the relevant items that we
# identified, is TP/(TP+FN).

# The F-Measure (or F-Score),
# which combines the precision and
# recall to give a single score, is defined to be the harmonic mean
# of the precision and recall:
# (2 × Precision × Recall) / (Precision + Recall).

class HW9:
    def precision(text, test):
        unigram_tagger_one = nltk.UnigramTagger(text)
        unigram_tagger_two = nltk.UnigramTagger(test)

        print(unigram_tagger_one.evaluate(test))
        print(unigram_tagger_two.evaluate(text))


















# text = brown.tagged_sents(categories='news')
# test = brown.tagged_sents(categories='romance')
h = HW9
h.precision(text, test)
