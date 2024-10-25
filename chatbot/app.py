from flask import Flask, render_template, request, jsonify
import csv
import pandas as pd
from src.chatbot import load_classifier, get_response  # Importing from chatbot.py

app = Flask(__name__)

# Load the pre-trained model for chatbot
classifier = load_classifier("data/medical_chatbot_model")  # Adjust path to your model file

# Load the precautions data
precautions_df = pd.read_csv('data/updated_symptom_precaution.csv')  # Adjust the path to your updated CSV file

# Home route
@app.route('/')
def home():
    return render_template('index.html')  # Render the homepage

# About Us page route
@app.route('/about')
def about():
    return render_template('about.html')  # Render the About Us page

# Chatbot page route
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')  # Render the chatbot UI

# Contact Us page route
@app.route('/contact')
def contact():
    return render_template('contact.html')  # Render the Contact Us page

# Route to handle contact form submission
@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Save data to a CSV file
    with open('contact_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, message])

    # Redirect to the contact page with a success message
    return render_template('contact.html', message="Thank you for your message. We will get back to you soon!")

# Chatbot interaction route
@app.route('/get-response', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    response = get_response(user_message, classifier, precautions_df)  # Pass precautions_df here
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
