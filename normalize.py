import requests
from itertools import islice
import nltk
from nltk.stem import PorterStemmer
import string
import matplotlib.pyplot as plt


# Get list of stopWords NLTK's Gist (Code provided in issues)
stopwords_list = requests.get(
    "https://gist.githubusercontent.com/rg089/35e00abf8941d72d419224cfd5b5925d/raw/12d899b70156fd0041fa9778d657330b024b959c/stopwords.txt").content
stopWords = set(stopwords_list.decode().splitlines())


# ~78,000 token count
with open("plaintext.txt", "r") as plainText:
    text = plainText.read().split()


def normalizeText(lowerCase = False, removeStopWords=False, stemming = False, removePunctuation = False ):
    tokenCount = 0
    tokens = {}
    for word in text:
        # Lowercase all words in the text.
        if lowerCase:
            word = word.lower()

        # Optional punctuation removal
        if removePunctuation:
            word = word.translate(str.maketrans("", "", string.punctuation))


        # Skip over stopWords if selected. Use lower because thats what the dataset is in
        if removeStopWords and word.lower() in stopWords:
            continue

        # Optional stemming
        if stemming:
            stemmer = PorterStemmer()
            word = stemmer.stem(word)
        

        if word in tokens:
            tokens[word] += 1
        else:
            tokens[word] = 1
        tokenCount += 1
    # Sort the dictionary by values in descending order - From ChatGPT
    sortedTokens = dict(
        sorted(tokens.items(), key=lambda item: item[1], reverse=True))
    return [tokenCount, sortedTokens]







# If name = main whatever. MAIN FUNCTION
lowercaseText = input('Would you like to lowercase text? (y/n)')
if lowercaseText.lower() == 'y':
    lowercaseText = True
else:
    lowercaseText = False

removeStopWords = input('Would you like to remove stop words? (y/n)')
if removeStopWords.lower() == 'y':
    removeStopWords = True
else:
    removeStopWords = False

stemming = input('Would you like to stem words? (y/n)')
if stemming.lower() == 'y':
    stemming = True
else:
    stemming = False

removePunctuation = input('Would you like to remove punctuation? (y/n)')
if removePunctuation.lower() == 'y':
    removePunctuation = True
else:
    removePunctuation = False


tokenCount, sortedTokens = normalizeText(lowerCase=lowercaseText, removeStopWords=removeStopWords, stemming=stemming, removePunctuation=removePunctuation)
# Output just top 5 most common words, code provided by ChatGPT.
for word, count in islice(sortedTokens.items(), 5):
    print(f"{word}: {count}")
print("TokenCount ", tokenCount)


# Plot here.
words = list(sortedTokens.keys())
counts = list(sortedTokens.values())

plt.figure(figsize=(10, 6))
plt.plot(words [:100], counts[:100])  
plt.xlabel('Words')
plt.ylabel('Counts')
plt.title('Top 100 Words and Their Counts')
plt.xticks(rotation=45, ha='right')
plt.show()

