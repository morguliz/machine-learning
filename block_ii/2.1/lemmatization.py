from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()


words = ["running", "went", "eating", "played"]

lemmatized = [lemmatizer.lemmatize(word, pos="v") for word in words]
print(lemmatized)