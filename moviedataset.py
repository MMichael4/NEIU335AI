# Required libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# === Sample Movie Dataset ===
data = pd.DataFrame({
    'title': [
        'Finding Nemo',
        'The Dark Knight',
        'The Notebook',
        'Avengers: Endgame',
        'Coco'
    ],
    'description': [
        'After his son is captured in the Great Barrier Reef and taken to Sydney, a timid clownfish sets out on a journey to bring him home.',
        'Batman faces the Joker, a criminal mastermind who seeks to plunge Gotham City into anarchy.',
        'A poor yet passionate young man falls in love with a rich young woman, giving her a sense of freedom.',
        'After the devastating events of Infinity War, the Avengers assemble once more to reverse Thanos’s actions.',
        'Aspiring musician Miguel enters the Land of the Dead to find his great-great-grandfather, a legendary singer.'
    ],
    'genre': [
        'Animation',
        'Action',
        'Romance',
        'Action',
        'Animation'
    ]
})

# === Vectorize the Descriptions ===
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(data['description'])
y = data['genre']

# === Train the Classifier ===
model = MultinomialNB()
model.fit(X, y)

# === User Input ===
print("🎬 Welcome to the Movie Genre Predictor!")
while True:
    user_input = input("\nEnter a short movie description (or type 'exit' to quit):\n> ")

    if user_input.lower() == 'exit':
        print("👋 Goodbye!")
        break

    input_vector = vectorizer.transform([user_input])
    prediction = model.predict(input_vector)
    print(f"🤖 Predicted Genre: **{prediction[0]}**")