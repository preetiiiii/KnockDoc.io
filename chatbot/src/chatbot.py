import pickle
from nltk.tokenize import word_tokenize
import pandas as pd

def extract_features(text):
    words = word_tokenize(text)
    return {word: True for word in words}

def load_classifier(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)

def load_precautions(file_path):
    return pd.read_csv(file_path)

def get_response(user_input, classifier, precautions_df):
    features = extract_features(user_input)
    prediction = classifier.classify(features)

    # Fetch precautions, doctor link, and description based on the predicted disease
    disease_info = precautions_df[precautions_df['Disease'] == prediction]
    if not disease_info.empty:
        precautions = disease_info.iloc[0, 1:5].dropna().values  # Get all precaution columns
        doctor_link = disease_info.iloc[0]['Doctor_Link']  # Get the doctor link
        description = disease_info.iloc[0]['Description']  # Get the doctor description
        
        # Debugging output
        print(f"Predicted Disease: {prediction}")
        print(f"Precautions: {precautions}")
        print(f"Doctor Link: {doctor_link}")
        print(f"Description: {description}")

        precautions_list = ', '.join(precautions)  # Join precautions in a readable format
        return (f"Based on the symptoms, it seems you might have: {prediction}. "
                f"To help manage your condition, it's advisable to: {precautions_list}. "
                f"For specialized assistance, you can visit: {doctor_link}. "
                f"Description: {description}")
    else:
        return f"Based on the symptoms, it seems you might have: {prediction}. However, no precautions or doctor links are available."
