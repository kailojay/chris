import re

def load_data(file_path):
    import pandas as pd
    # Load the data from a CSV file
    data = pd.read_csv(file_path)
    return data

def clean_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove digits from the text
    text = re.sub(r'\d+', '', text)
    # Remove non-word characters from the text, but keep Korean characters
    text = re.sub(r'[^\w\sㄱ-ㅎㅏ-ㅣ가-힣]', ' ', text)
    # Remove leading and trailing whitespace
    return text.strip()