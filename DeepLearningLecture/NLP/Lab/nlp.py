from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
import re
from string import punctuation
import contractions
from sklearn.feature_extraction.text import CountVectorizer

# Without Improvements
corpus = [
    "the movie was fantastic and i loved every part of it", 
    "an absolute masterpiece with brilliant acting", 
    "the film was boring and too long", 
    "i really enjoyed the story and the visuals", 
    "the plot was terrible and the acting was even worse", 
    "what a wonderful experience, highly recommend", 
    "not worth my time, very disappointing", 
    "a truly great film, i will watch it again", 
    "the script was weak and the characters were flat", 
    "an amazing journey from start to finish"
]


categories = [ "Positive", "Positive", "Negative", "Positive", "Negative", 
              "Positive", "Negative", "Positive", "Negative", "Positive" ]



vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(corpus)

print('\nFeature Names:', vectorizer.get_feature_names_out())
print('Vectors:', vectors.toarray(), end='\n\n')


clf = SVC(kernel='linear') # support vector classification
clf.fit(vectors, categories)

test_corpus = [ "the movie was great", "i hated the film", "a boring and bad story", "absolutely loved it" ]
test_categories = [ "Positive", "Negative", "Negative", "Positive" ]

test_x = vectorizer.transform(test_corpus)

predicted = clf.predict(test_x)
print('Predicted:', predicted)
print('Accuracy without improvements:', clf.score(test_x, test_categories), end='\n\n')

# Add Improvement
# Improvement — Clean the Text Before Vectorizing, Use Bigrams, add at least 6 new movie reviews

new_corpus = [
    "the movie was fantastic and i loved every part of it",
    "an absolute masterpiece with brilliant acting",
    "the film was boring and too long",
    "i really enjoyed the story and the visuals",
    "the plot was terrible and the acting was even worse",
    "what a wonderful experience, highly recommend",
    "not worth my time, very disappointing",
    "a truly great film, i will watch it again",
    "the script was weak and the characters were flat",
    "an amazing journey from start to finish",

    # new reviews
    "the movie was excellent and very enjoyable",
    "i hated the acting and the story was awful",
    "a beautiful film with a great soundtrack",
    "the movie was slow and very boring",
    "an outstanding performance by the actors",
    "the film was disappointing and poorly written"
]

new_categories = [
    "Positive","Positive","Negative","Positive","Negative",
    "Positive","Negative","Positive","Negative","Positive",

    # labels for new reviews
    "Positive",
    "Negative",
    "Positive",
    "Negative",
    "Positive",
    "Negative"
]

def clean_text(text):

    # remove contractions
    text = contractions.fix(text)

    # lowercase
    text = text.lower()

    # remove punctuation
    text = re.sub('[%s]' % re.escape(punctuation), '', text)

    # remove numbers
    text = re.sub(r'\w*\d\w*', '', text)

    # remove stop words
    stopwords = [stopword.strip() for stopword in open('../Lecture/data/stopwords_en.txt', 'r')]
    text = ' '.join([word for word in text.split() if word not in stopwords])

    return text


cleaned_corpus = [clean_text(t) for t in new_corpus]
cleaned_test = [clean_text(t) for t in test_corpus]

vectorizer = CountVectorizer(ngram_range=(1, 2))
vectors = vectorizer.fit_transform(cleaned_corpus)

clf = SVC(kernel='linear') # support vector classification
clf.fit(vectors, new_categories)


X_test = vectorizer.transform(cleaned_test)

predictions = clf.predict(X_test)

print('Predictions:', predictions)
print('Accuracy with improvements:', clf.score(X_test, test_categories))


# Part 4
limitation_sentences = [
    "the movie was not good",
    "the acting was not bad",
    "visually impressive but boring",
    "i wanted to like it"
]

cleaned_limitation = [clean_text(s) for s in limitation_sentences]

X_limitation = vectorizer.transform(cleaned_limitation)

limitation_predictions = clf.predict(X_limitation)

print("\nLimitation Test Predictions:")
for i in range(len(limitation_sentences)):
    print(limitation_sentences[i], "->", limitation_predictions[i])
