"""
Chapter 6: Strings
AI concept: a tiny bag-of-words sentiment scorer -- the same core idea
behind real sentiment-analysis systems, just checking for a handful of
words instead of thousands. Built entirely with the "in" operator and
string methods from this chapter (no lists needed yet).
"""
sentence=input("Type a sentence about a movie: ")
sentence=sentence.lower()

score=0

if "great" in sentence:
    score=score+1
if "good" in sentence:
    score=score+1
if "love" in sentence:
    score=score+1
if "amazing" in sentence:
    score=score+1

if "bad" in sentence:
    score=score-1
if "terrible" in sentence:
    score=score-1
if "hate" in sentence:
    score=score-1
if "boring" in sentence:
    score=score-1

print("Sentiment score:",score)

if score>0:
    print("Overall: POSITIVE")
elif score<0:
    print("Overall: NEGATIVE")
else:
    print("Overall: NEUTRAL")