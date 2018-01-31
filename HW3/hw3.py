Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> from nltk.book import *
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
>>> 
>>> 
>>> 
>>> 
>>> # problem 1
>>> from nltk.corpus import state_union
>>> cfd = nltk.ConditionalFreqDist((text, word)
			       for text in state_union.fileids()
			       for word in state_union.words( fileids = text ))

>>> text = state_union.fileids()
>>> contexts = ['men', 'women', 'people']
>>> cfd.tabulate(condition = text, samples = contexts)
                       men  women people 
    1945-Truman.txt      2      2     10 
    1946-Truman.txt     12      7     49 
    1947-Truman.txt      7      2     12 
    1948-Truman.txt      4      1     22 
    1949-Truman.txt      2      1     15 
    1950-Truman.txt      6      2     15 
    1951-Truman.txt      8      2      9 
1953-Eisenhower.txt      3      0     17 
1954-Eisenhower.txt      2      0     15 
1955-Eisenhower.txt      4      0     26 
1956-Eisenhower.txt      2      2     30 
1957-Eisenhower.txt      5      2     11 
1958-Eisenhower.txt      2      1     19 
1959-Eisenhower.txt      4      1     11 
1960-Eisenhower.txt      2      0     10 
   1961-Kennedy.txt      6      0     10 
   1962-Kennedy.txt      6      2     10 
   1963-Johnson.txt      0      0      3 
   1963-Kennedy.txt      8      5     12 
   1964-Johnson.txt      3      1      3 
 1965-Johnson-1.txt      7      0     16 
 1965-Johnson-2.txt     11      3     14 
   1966-Johnson.txt     12      1     35 
   1967-Johnson.txt     11      1     25 
   1968-Johnson.txt      4      0     17 
   1969-Johnson.txt      5      2      6 
     1970-Nixon.txt      2      0     23 
     1971-Nixon.txt      1      0     31 
     1972-Nixon.txt      1      0      7 
     1973-Nixon.txt      0      0      9 
     1974-Nixon.txt      0      0     19 
      1975-Ford.txt      0      0     13 
      1976-Ford.txt      3      1     18 
      1977-Ford.txt      2      1     17 
    1978-Carter.txt      0      1     26 
    1979-Carter.txt      0      1     15 
    1980-Carter.txt      1      2     11 
    1981-Reagan.txt      1      1     11 
    1982-Reagan.txt      1      1     17 
    1983-Reagan.txt      3      7     19 
    1984-Reagan.txt      3      5     23 
    1985-Reagan.txt      1      1     12 
    1986-Reagan.txt      2      2     14 
    1987-Reagan.txt      1      0     24 
    1988-Reagan.txt      1      0     16 
      1989-Bush.txt      2      3     13 
      1990-Bush.txt      3      2      9 
    1991-Bush-1.txt      2      2     13 
    1991-Bush-2.txt      7      7     13 
      1992-Bush.txt      4      4     26 
   1993-Clinton.txt      1      2     45 
   1994-Clinton.txt      1      1     63 
   1995-Clinton.txt      1      3     73 
   1996-Clinton.txt      2      3     40 
   1997-Clinton.txt      1      2     30 
   1998-Clinton.txt      2      2     22 
   1999-Clinton.txt      2      3     22 
   2000-Clinton.txt      5      6     41 
  2001-GWBush-1.txt      3      3     14 
  2001-GWBush-2.txt      1      2     12 
    2002-GWBush.txt      3      5     14 
    2003-GWBush.txt      6      4     33 
    2004-GWBush.txt      6      8     21 
    2005-GWBush.txt      8     11     18 
    2006-GWBush.txt      7      7     22 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> # problem 2
>>> 
>>> 
>>> from nltk.corpus import wordnet as wn
>>> def percentOfNounOfNoHypnoym():
	return len(list(filter(lambda ss: len(ss.hypernyms()) == 0,wn.all_synsets('n')))) / len(list(wn.all_synsets('n')))
>>> percentOfNounOfNoHypnoym()
0.09408756012908726
>>> 
>>> 
>>> 
>>> 
>>> 
>>> # problem 3
>>> 
>>>
>>> 
>>> from nltk.corpus import brown
>>> brown.categories()
['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']
>>> cfd = nltk.ConditionalFreqDist((genre, word)
			       for genre in brown.categories()
			       for word in brown.words( categories = genre ))
>>> genres = brown.categories()
>>> words = ['love', 'god', 'kiss', 'intimate', 'friendship', ‘sex’]
SyntaxError: invalid character in identifier
>>> words = ['love', 'god', 'kiss', 'intimate', 'friendship', 'sex']
>>> cfd.tabulate(condition = genres, samples = words)
                      love        god       kiss   intimate friendship        sex 
      adventure          9          0          5          2          0          3 
 belles_lettres         68          3          0          2         13         32 
      editorial         13          0          0          0          1          2 
        fiction         16          0          6          3          0          2 
     government          1          0          0          0          0          1 
        hobbies          6          0          0          1          1          0 
          humor          4          1          0          1          1          1 
        learned         13          0          1          0          6          9 
           lore         19          3          1          2          2         22 
        mystery          7          0          0          2          0          0 
           news          3          0          0          0          0          2 
       religion         13          5          0          1          1          0 
        reviews          7          0          0          4          2          1 
        romance         32          5          3          3          0          4 
science_fiction          3          0          0          0          0          2 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #problem 4
>>> 
>>> 
>>> 
>>> bad_words = [ 'hell', 'Queequeg', 'dumpling' ]
>>> better_words = [ 'heck', 'Tony', 'core' ]
>>> sample_text = 'In one word , Queequeg , said I , rather digressively ; hell is an idea first born on an undigested apple - dumpling'
>>> def censor(bad_words, better_words, sample_text):
	for i in sample_text.split():
		for j in range(len(bad_words)):
			if i == bad_words[j]:
				sample_text = sample_text.replace(i , better_words[j])
	return sample_text

>>> print( censor( bad_words, better_words, sample_text ) )

In one word , Tony , said I , rather digressively ; heck is an idea first born on an undigested apple - core
>>> 
