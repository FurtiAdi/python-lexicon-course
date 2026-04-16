import contractions
import re
from string import punctuation


def clean_text(text):

    # remove contractions
    text = contractions.fix(text)
    
    # remove lowercasing
    text = text.lower()

    # remove punctuation
    text = re.sub('[%s]' % re.escape(punctuation), '', text)

    # remove numbers
    text = re.sub(r'\w*\d\w*', '', text)

    # remove stop words
    stopwords = [stopword.strip() for stopword in open('./data/stopwords_en.txt', 'r')]
    text = ' '.join([word for word in text.split() if word not in stopwords])

    return text

text = "I read this book for the first time in 1987, and it's still one of my favorites!"

cleaned_text = clean_text(text)
print(cleaned_text)