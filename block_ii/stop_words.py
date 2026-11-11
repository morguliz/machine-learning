from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

english_stopwords = set(stopwords.words("english"))
print(len(english_stopwords))

# filtering tokens
tokens = ["the", "movie", "was", "amazing", "and", "fun"]
filtered_tokens = [x for x in tokens if x not in english_stopwords]
print(filtered_tokens)