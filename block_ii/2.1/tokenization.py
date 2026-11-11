import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

review = "The movie was amazing. I loved the acting!"

tokens = word_tokenize(review.lower())
print(tokens)
