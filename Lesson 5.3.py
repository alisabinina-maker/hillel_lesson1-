import string

# Step 1: get text from user
text = input("Enter your text: ")

# Step 2: remove all punctuation marks
for symbol in string.punctuation:
    text = text.replace(symbol, "")

# Step 3: split into words (this also removes extra spaces)
words = text.split()

# Step 4: make each word start with a capital letter
words = [w.capitalize() for w in words]

# Step 5: join words and add '#' at the beginning
hashtag = "#" + "".join(words)

# Step 6: limit to 140 characters
if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)