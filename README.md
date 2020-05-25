# nlp-learning
My notes from NLP Learning from LinkedIn Learning

## Different Phases
1. Convert raw text to Structured Data: This might involve:
  * Regex parsing
  * Stripping out html
  * Splitting out into Pandas DataFrames based on delimiters

* Data Exploration: Understand how the data is organized, what are we looking at

## Machine Learning Pipeline
1. Convert raw text to tokens (`tokenize`)
1. Remove Stop Words to allow pipeline to focus on the text that is really important.
  1. This also helps reduce number of tokens to read
1. Stemming and Lemmatization can help reduce complexity:
  1. Learn vs Learning
1. Vectorization:
  1. Counting occurrences of each word into a matrix
1. Fit it into ML Model
  1. Select a few candidate models and try them out

## Python Notes

Filter a DataFrame

```
spamCount = len(fullCorpus[fullCorpus['isSpam'] == 'spam'])
hamCount = len(fullCorpus[fullCorpus['isSpam'] == 'ham'])

```

https://jupyter.readthedocs.io/en/latest/install.html
