import pandas as pd

def preprocess_data(file_path):
    # Load dataset
    df = pd.read_csv(file_path)
    
    # Prepare data for training
    data = []
    for index, row in df.iterrows():
        symptoms = ' '.join([str(row[f'Symptom_{i}']) for i in range(1, 18) if pd.notna(row[f'Symptom_{i}'])])
        data.append((symptoms, row['Disease']))
    
    return data

def save_processed_data(data, file_path):
    with open(file_path, 'w') as f:
        for symptoms, disease in data:
            f.write(f"{symptoms}\t{disease}\n")

if __name__ == "__main__":
    data = preprocess_data(r'C:\Users\preeti\OneDrive\Desktop\medical_chatbot\data\dataset.csv')
    save_processed_data(data,r'C:\Users\preeti\OneDrive\Desktop\medical_chatbot\data\processed_data.txt')
