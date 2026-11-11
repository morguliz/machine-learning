import re

# re.sub(pattern, replacement, text)
review = "<p>The movie was amazing!</p><br>I loved the acting."

clean_review = re.sub(r"<[^>]+>", " ", review)
print(clean_review)