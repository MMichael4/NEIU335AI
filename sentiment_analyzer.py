"""
Assignment 5: Simple Sentiment Analyzer

Instructions:
1. Modify the `positive_words` and `negative_words` sets below:
   - **Add at least 15 positive words** and **15 negative words** of your choice.
   - Ensure words are lowercased and contain only alphabetic characters.
2. Print positive lexicon & negative lexicon
3. Compute simple sentiment score (hint: positive - negative count)
4. Print the output results
5. Add a short reflection as comments at the bottom:
   - Discuss **strengths** and **limitations** of this lexicon-based approach (2–3 sentences).

Deliverables:
- Completed Python script (`sentiment_analyzer.py`).
"""

import re

def clean_text(text):
    """
    Lowercase, remove punctuation, and split into tokens.
    """
    text = text.lower()
    text = re.sub(r"[^a-z\s]", '', text)
    tokens = text.split()
    return tokens

# 1. Add 15+ positive and 15+ negative words
positive_words = {
    'happy', 'joyful', 'love', 'excellent', 'great', 'fantastic', 'amazing', 'wonderful',
    'delightful', 'awesome', 'pleasant', 'enjoyable', 'blessed', 'cheerful', 'smile', 'good'
}

negative_words = {
    'sad', 'angry', 'hate', 'horrible', 'terrible', 'awful', 'worst', 'disgusting',
    'depressing', 'bad', 'painful', 'annoying', 'frustrating', 'upset', 'miserable', 'ugly'
}

# 2. Display lexicons
print("Positive Lexicon:", sorted(positive_words))
print("Negative Lexicon:", sorted(negative_words))

# --- Interactive Sentiment Testing ---
print("\nEnter sentences to analyze sentiment (type 'exit' to quit):")
while True:
    text = input('> ').strip()
    if text.lower() in ('exit', 'quit'):
        print("Goodbye!")
        break

    tokens = clean_text(text)
    pos_count = sum(1 for t in tokens if t in positive_words)
    neg_count = sum(1 for t in tokens if t in negative_words)
    total = len(tokens)

    # 3. Compute sentiment score
    score = pos_count - neg_count

    # Determine sentiment label
    if score > 0:
        sentiment = 'Positive'
    elif score < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    # 4. Print results
    print(f"Tokens: {tokens}")
    print(f"+ matches: {pos_count}, - matches: {neg_count}")
    print(f"Score: {score:.3f} => {sentiment}\n")


