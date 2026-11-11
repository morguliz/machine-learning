from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["running", "runs", "connected", "connecting"]

stems = [stemmer.stem(word) for word in words]
print(stems)