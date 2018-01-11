# SentSem

SentSem is a Python script used for the semantics comparison between two sentences. The script's `sentsem()` function accepts two sentences as an input, and outputs the overall similarity between those two sentences.

## Getting Started

The main library used for the project is `nltk` for Python. `NumPy` is also used. NLTK may be downloaded using pip.

```
> pip install nltk
```

```
import nltk

nltk.download() # Download all the required corpora and tools
```

## Running the Script

```
from sentsem import sentsem

sent1 = 'Hello, I like to play football!'
sent2 = 'Greetings, I love playing soccer!'

print(sentsem(sent1, sent2))
# 0.798

```
