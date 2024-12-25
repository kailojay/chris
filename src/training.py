import pandas as pd
from preprocess import load_data, clean_text
from classifier import SpamClassifier
import pickle

# Load the data
data = load_data('../data/ohshitimakebigshit.csv')

# Print the columns of the loaded data to debug
print("Columns in the dataset:", data.columns)

# Print the first few rows of the dataset to understand its structure
print(data.head())

# Clean the text data
data['email'] = data['email'].apply(clean_text)

# Initialize and train the classifier
classifier = SpamClassifier()
classifier.train(data)

# Save the trained model to a file
with open('../models/spam_classifier.pkl', 'wb') as model_file:
    pickle.dump(classifier, model_file)

print("Training completed and model saved.")