import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

nltk.download('punkt')

def extract_features(text):
    words = word_tokenize(text)
    return {word: True for word in words}

def load_data(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    data = []
    for line in lines:
        symptoms, disease = line.strip().split('\t')
        features = extract_features(symptoms)
        data.append((features, disease))
    
    return data

def train_classifier(train_data):
    return NaiveBayesClassifier.train(train_data)

def evaluate_model(classifier, test_data):
    test_features, test_labels = zip(*test_data)
    predictions = [classifier.classify(features) for features in test_features]
    accuracy = accuracy_score(test_labels, predictions)
    return accuracy

if __name__ == "__main__":
    # Load and split the data
    data = load_data(r'C:\Users\preeti\OneDrive\Desktop\medical_chatbot\data\processed_data.txt')
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
    
    # Train the classifier
    classifier = train_classifier(train_data)
    
    # Evaluate the classifier on the test data
    accuracy = evaluate_model(classifier, test_data)
    print(f'Test Accuracy: {accuracy:.2f}')
    
    # Save the trained model
    with open(r'C:\Users\preeti\OneDrive\Desktop\medical_chatbot\data\medical_chatbot_model', 'wb') as f:
        pickle.dump(classifier, f)

    # To visualize the accuracy over multiple runs (if you want to run it multiple times)
    accuracies = []
    for i in range(10):  # For example, run 10 times
        train_data, test_data = train_test_split(data, test_size=0.2, random_state=i)
        classifier = train_classifier(train_data)
        accuracy = evaluate_model(classifier, test_data)
        accuracies.append(accuracy)

    # Plotting accuracy
    plt.plot(range(1, 11), accuracies, marker='o')
    plt.title('Model Accuracy Over Multiple Runs')
    plt.xlabel('Run Number')
    plt.ylabel('Accuracy')
    plt.ylim(0, 1)  # Set y-axis limit from 0 to 1
    plt.xticks(range(1, 11))
    plt.grid()
    plt.show()
