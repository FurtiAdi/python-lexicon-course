from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC


corpus = [
    'i love the book',
    'the book is great',
    'i hate the movie',
    'the movie is boring'
]

books = 'Books'
movies = 'Movies'

categories = [books, books, movies, movies]

vectorizer = CountVectorizer(ngram_range=(1, 2))

vectors = vectorizer.fit_transform(corpus)

#print(vectorizer.get_feature_names_out())
#print(vectors.toarray())


clf = SVC(kernel='linear') # support vector classification
clf.fit(vectors, categories)

test_corpus = [
    'i love this read',
    'the movie is great',
    'i hate the book',
    'the movie is boring'
]

test_categories = [books, movies, books, movies]

test_x = vectorizer.transform(test_corpus)

predicted = clf.predict(test_x)
print(predicted)
print(clf.score(test_x, test_categories))



