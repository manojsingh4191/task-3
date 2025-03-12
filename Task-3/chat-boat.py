import nltk
import spacy
import random
import re

# Load spaCy model for Named Entity Recognition (NER)
nlp = spacy.load("en_core_web_sm")

# Predefined responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey, how can I help you today?"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["Sorry, I don't understand that.", "Could you please clarify?", "I didn't get that."]
}

# Sample queries and associated intents
patterns = {
    "greeting": [r"\b(hello|hi|hey)\b", r"\b(howdy|good morning|good evening)\b"],
    "bye": [r"\b(bye|goodbye|see you|later)\b"],
}

# Function to process text
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"\s+", " ", text)  # Remove extra spaces
    return text

# Function to match intent based on user input
def match_intent(text):
    for intent, pattern_list in patterns.items():
        for pattern in pattern_list:
            if re.search(pattern, text):
                return intent
    return "default"

# Function to get response based on intent
def get_response(intent):
    return random.choice(responses.get(intent, responses["default"]))

# Main chatbot function
def chatbot():
    print("Hello! I am your chatbot. Ask me anything or type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() in ["bye", "goodbye", "exit"]:
            print("Chatbot: Goodbye!")
            break
        
        # Preprocess input and match intent
        user_input = preprocess_text(user_input)
        intent = match_intent(user_input)
        
        # Get and display the response
        response = get_response(intent)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
