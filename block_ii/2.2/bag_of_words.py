from sklearn.feature_extraction.text import CountVectorizer

reviews = ["good movie", "good acting"]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(reviews)
print(X.toarray())