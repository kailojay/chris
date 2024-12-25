import pickle
from preprocess import load_data, clean_text
from utils import calculate_accuracy, calculate_precision, calculate_recall

# Load the trained model
with open('../models/spam_classifier.pkl', 'rb') as model_file:
    classifier = pickle.load(model_file)

# Load the data
data = load_data('../data/ohshitimakebigshit.csv')

# Clean the text data
data['email'] = data['email'].apply(clean_text)

# Predict the labels for the data
predicted_labels = data['email'].apply(classifier.predict)

# Calculate evaluation metrics
accuracy = calculate_accuracy(data['label'], predicted_labels)
precision = calculate_precision(data['label'], predicted_labels)
recall = calculate_recall(data['label'], predicted_labels)

# Print the evaluation metrics
print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')