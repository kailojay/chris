# Spam Mail Classifier

This project implements a spam mail classifier using the Naive-Bayesian theorem. The classifier is trained on a dataset of labeled emails to distinguish between spam and non-spam messages.

## Project Structure

```
spam-mail-classifier
├── data
│   └── ohshitimakebigshit.csv  # Sample data for training and testing
├── src
│   ├── classifier.py           # Implementation of the Naive-Bayesian classifier
│   ├── preprocess.py           # Data preprocessing functions
│   └── utils.py                # Utility functions for metrics calculation
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd spam-mail-classifier
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Preprocess the data:
   - Use the `preprocess.py` script to load and clean the data from `data/ohshitimakebigshit.csv`.

2. Train the classifier:
   - Use the `classifier.py` script to create an instance of the `SpamClassifier` class and call the `train` method with the preprocessed data.

3. Make predictions:
   - Use the `predict` method of the `SpamClassifier` class to classify new emails.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.# chris
