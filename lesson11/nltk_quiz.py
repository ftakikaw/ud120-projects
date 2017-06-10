from nltk.corpus import stopwords

sw = stopwords.words("english")

print "no stopwords: ", len(sw)

from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

stem = stemmer.stem("responsiveness")

print "Stem: ", stem