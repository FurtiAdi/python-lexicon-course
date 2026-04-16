#-----------------------------------------------------------------------------
# Part 1 –  Previous Model
#-----------------------------------------------------------------------------

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
import re
from string import punctuation
import contractions
from sklearn.feature_extraction.text import CountVectorizer


movie_review = [
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

categories = [
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

test_sentences = [ "the movie was great", 
                  "i hated the film", 
                  "the movie was not good", 
                  "the acting was not bad", 
                  "visually impressive but boring", 
                  "i wanted to like it" ]

test_categories = [ "Positive", "Negative", "Negative", "Positive", "Negative", "Positive" ]

cleaned_corpus = [clean_text(t) for t in movie_review]
cleaned_test = [clean_text(t) for t in test_sentences]

vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(cleaned_corpus)

clf = SVC(kernel='linear') # support vector classification
clf.fit(vectors, categories)


X_test = vectorizer.transform(cleaned_test)

predictions = clf.predict(X_test)

print('\n-------------CountVectorizer Result-------------------\n')

print('\nPredictions:', predictions)
print('Accuracy with improvements:', clf.score(X_test, test_categories), end='\n \n')


#-----------------------------------------------------------------------------
# Part 2 – Hugging Face Model
#-----------------------------------------------------------------------------

from transformers import pipeline 

sentiment = pipeline("sentiment-analysis", 
                     model="distilbert-base-uncased-finetuned-sst-2-english")

print('\n-------------HuggingFace Result-------------------\n')
for review in test_sentences:
    result = sentiment(review)[0] # returns a list of dicts, we take the first one
    print(f"Review: {review}\n-> Label: {result['label']}, Score: {result['score']:.3f}\n")


#-----------------------------------------------------------------------------
# Part 3 - Compare Compare the results
#-----------------------------------------------------------------------------
"""

What does your model predict? 
  ->  Ans:
    The classical model (CountVectorizer + SVC) predicts the following:

    “the movie was great” → Positive

    “i hated the film” → Negative

    “the movie was not good” → Positive

    “the acting was not bad” → Negative

    “visually impressive but boring” → Negative

    “i wanted to like it” → Positive

    The model performs well on most sentences but makes a mistake on “the movie was not good,” 
    and “the acting was not bad” where it predicts Positive instead of Negative and Negative 
    instead of positive.

What does the Hugging Face model predict?
  ->  Ans:
    The Hugging Face model predicts:

    Review: the movie was great
    -> Label: POSITIVE, Score: 1.000

    Review: i hated the film
    -> Label: NEGATIVE, Score: 1.000

    Review: the movie was not good
    -> Label: NEGATIVE, Score: 1.000

    Review: the acting was not bad
    -> Label: POSITIVE, Score: 0.999

    Review: visually impressive but boring
    -> Label: POSITIVE, Score: 0.663

    Review: i wanted to like it
    -> Label: POSITIVE, Score: 1.000

The Hugging Face model correctly handles negation in “the movie was not good.” However, it predicts
“visually impressive but boring” as Positive, but with lower confidence (0.663), indicating some 
uncertainty when dealing with mixed sentiment.
"""

#-----------------------------------------------------------------------------
# Part 4 – Analysis
#-----------------------------------------------------------------------------

"""
Which model performed better overall?

        The Hugging Face model performed better overall. It correctly handled more complex sentences, 
        especially those involving negation, while the classical model made mistakes in such cases.

Which sentences were difficult for your first model?

        The sentences “the movie was not good” and “the acting was not bad” were difficult for the first 
        model, as it was incorrectly predicted as Positive and Negative.

        Some sentences with mixed sentiment, like “visually impressive but boring,” can also be challenging, 
        although the model predicted it correctly in this case.

Why is "the movie was not good" difficult?

        This sentence is difficult because the classical model does not understand negation. It mainly focuses 
        on individual words like “good,” which has a positive meaning, and ignores the effect of the word “not.” 
        As a result, it predicts the sentence as Positive instead of Negative.

Why is "the acting was not bad" difficult?

        This sentence is difficult because it contains a double meaning. The word “bad” is negative, but “not 
        bad” actually means something positive. The classical model may focus on the word “bad” and misinterpret 
        the sentence, since it does not fully understand context.

        Which model seems to better understand negation?

        The Hugging Face model better understands negation. It correctly predicts sentences like “the movie was 
        not good,” while the classical model fails.


Which model seems to better understand mixed sentiment?

        The Hugging Face model also handles mixed sentiment better, as it considers the full context of the sentence. 
        However, it is not perfect, as seen in “visually impressive but boring,” where it predicts Positive with lower 
        confidence (0.663), showing uncertainty. The classical model, on the other hand, predicts this sentence correctly 
        as Negative, even though it does not understand the full context and instead relies on individual words like “boring.”
"""


#-----------------------------------------------------------------------------
# Part 5 - Reflection
#-----------------------------------------------------------------------------

"""

What is the main difference between: CountVectorizer + classifier Hugging Face models?
When would you use each approach?
        The main difference between CountVectorizer with a classifier and Hugging Face models is how they 
        understand text. The CountVectorizer approach converts text into numerical features based on word 
        frequency, and the classifier makes predictions based on these features without understanding the 
        actual meaning of the sentence. In contrast, Hugging Face models are based on deep learning and are 
        trained on large datasets, allowing them to understand context, word relationships, and sentence meaning.

        The classical model is simpler, faster, and requires less computational power, but it struggles with things 
        like negation and mixed sentiment. Hugging Face models perform better in understanding complex language but 
        require more resources and are more advanced.

        I would use the CountVectorizer approach for simple tasks, small datasets, or when computational resources are 
        limited. On the other hand, I would use Hugging Face models when higher accuracy is needed, especially for tasks 
        involving complex language, context, or real-world applications.

"""