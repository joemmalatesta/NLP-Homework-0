# NLP Homework 0
Chat GPT aided in some of the code generation for library's I had little experience with and with array manipulation.


### Setup
- Clone repo
- `pip install nltk`
- `pip install requests`
- `pip install matplotlib`

### Run
- `python normalize.py`
- Instead of doing `-stopwords`, you will be given four options in the terminal upon running the program.
- The program will complete once you close the plot of the words.


##  Report
### Data
My selected text was [Frankenstein](https://www.gutenberg.org/files/84/84-h/84-h.htm) from Project Gutenberg. There wasn't anything that stood out to me about this text besides that the beginning was letters so it would have more possessive writing. (~78k tokens)

### Methodology
I combined all of my normalization into one function, with each being toggled by a simple if/else condition. I put the normalization techniques in an order that I thought built on each other. I will present each method of normalization here as it appears in my code
- lowercase
-  punctuation
- stop words
- stemming

  
I chose to remove punctuation because it helped remove some repeats in the high and low count words. Being able to run it with and without removing it helped me understand common words that end sentences or 

### Sample output
This is made with lowercasing and removal of punctuation but no stemming or stop word removal.
This will show in the terminal after each run and will change based on your selection of normalization.


Most common 10 words:
the: 4343
and: 3025
i: 2766
of: 2760
to: 2169
my: 1751
a: 1439
in: 1183
was: 1022
that: 1019

Least common 10 words:
hart: 1
originator: 1
forty: 1
network: 1
volunteer: 1
edition: 1
main: 1
pg: 1
subscribe: 1
newsletter: 1



## Discussion
#### Findings
- It was interesting to me that the most frequent words, no matter how I normalized the text all trended towards the story being personal. Without stop words removed "I" was an uncommonly overused word (in comparison) and even with stop words removed and stemming added, you could still get a sense that this story was written in first person and explaining their personal experiences. Words like "Feel", "thought", "friend", and "love" give insight into the story even after normalization. The most uncommon words, however, seemed to be much more random, with each one just being a one off word that could be common in some stories but not here ("network", "web"). It was still slightly interesting that words like "main" did not show up more than once.
#### Zipf's Law
- My results are slightly differing from Zipf's law (after lowercasing and removing punctuation). While I expected the numbers of the law to differ which they do (4343,3025,2766,2760), I did expect the most common words to be the same. There is one difference in my top four words though which is "I". This was an interesting finding because I wrote beforehand that there may be more possessive writing due to there being letters included in the text.
#### Removing stop words
- After removing stop words, the token count drops from 78k to 32k. This means that there are more stop words in the text than regular content. While I did use a larger corpus of stopwords than the one provided by `nltk`, it is still substantial and strange to think about actually.

### What I learned
In completing this assignment, I used many libraries that I had previous experience with for formatting and outputting data, but I got more experience with what went into normalizing tokens as well as the `nltk` library. It was interesting to see how much you could remove and still retain most of the message. In addition, it was cool to see the math and thought behind it with Zipf's law. Overall, it was a good introduction to the basis of which NLP is built.