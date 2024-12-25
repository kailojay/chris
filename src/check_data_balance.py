from preprocess import load_data

# Load the data
data = load_data('../data/ohshitimakebigshit.csv')

# Count the number of spam and ham emails
spam_count = sum(1 for label in data['label'] if label == 'spam')
ham_count = sum(1 for label in data['label'] if label == 'ham')

# Print the counts
print(f'Spam emails: {spam_count}')
print(f'Ham emails: {ham_count}')