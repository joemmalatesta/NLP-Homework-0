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

  
I chose to remove punctuation because it helped some repeats in the high and low count words. Being able to run it with and without removing it helped me understand common words that end sentences or 

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



### Discussion
#### Findings

#### What I learned