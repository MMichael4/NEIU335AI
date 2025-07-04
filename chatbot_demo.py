#you will need to 'pip install sentence-transformers transformers' first
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import numpy as np

# Knowledge base
knowledge_base = [
    "CS 335 is a class about AI and how to use it effectively in the real-world",
    "Professor Omeed has had a cat since 2021, and his name is Dino. He is 5 years old now",
    "Professor Omeed has worked for Google since June 2022."
]

# Embedding model
embedder = SentenceTransformer('all-MiniLM-L6-v2')
kb_vectors = embedder.encode(knowledge_base)

# Text2Text model for generation
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-small")

# chatbot is looking for you to ask it a question
print("🤖 Chatbot is ready! Type your question or type 'exit' to quit.\n")

while True:
    question = input("You: ")

    if question.strip().lower() in ["exit", "quit"]:
        print("👋 Chatbot says goodbye!")
        break

    # trying to find the most relevant context
    q_vector = embedder.encode([question])
    scores = np.inner(q_vector, kb_vectors)
    best_index = np.argmax(scores)
    context = knowledge_base[best_index]

    # for the question and answer
    prompt = f"Answer the question using this information:\n{context}\nQuestion: {question}"
    response = qa_pipeline(prompt, max_new_tokens=100)[0]['generated_text']

    print("\n🤖 Chatbot says:\n", response.strip(), "\n")
