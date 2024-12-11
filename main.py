import tkinter as tk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
import nltk

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Text preprocessing
def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    processed = [lemmatizer.lemmatize(word) for word in tokens if word.isalpha() and word not in stop_words]
    return processed

# Sentiment analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    if blob.sentiment.polarity > 0.2:
        return "positive"
    elif blob.sentiment.polarity < -0.2:
        return "negative"
    else:
        return "neutral"

# Generate chatbot response
def generate_response(user_text):
    sentiment = analyze_sentiment(user_text)
    if sentiment == "positive":
        return "That's great! Tell me more about what's making you feel this way."
    elif sentiment == "negative":
        return "I'm sorry to hear that. why don't you try writing it out here, it might help you feel better about the situation."
    else:
        return "uhuh, do carry on"

# Respond to user input
def respond():
    user_text = user_input.get("1.0", tk.END).strip()
    if user_text:
        chat_display.configure(state='normal')
        chat_display.insert(tk.END, f"You: {user_text}\n")
        
        bot_response = generate_response(user_text)
        chat_display.insert(tk.END, f"Bot: {bot_response}\n")
        chat_display.configure(state='disabled')
        
        user_input.delete("1.0", tk.END)

# Clear the chat display
def clear_chat():
    chat_display.configure(state='normal')
    chat_display.delete("1.0", tk.END)
    chat_display.configure(state='disabled')

# Create GUI
root = tk.Tk()
root.title("Journaling Buddy Chatbot")

user_input = tk.Text(root, height=5, width=50)
user_input.pack(pady=10)

chat_display = tk.Text(root, height=20, width=60, state='disabled', bg="lightyellow")
chat_display.pack(pady=10)

scrollbar = tk.Scrollbar(root, command=chat_display.yview)
chat_display['yscrollcommand'] = scrollbar.set
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

submit_button = tk.Button(root, text="Submit", command=respond)
submit_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear Chat", command=clear_chat)
clear_button.pack(pady=5)

root.mainloop()
