class SpamClassifier:
    def __init__(self):
        self.word_probs = {}
        self.class_probs = {}
        self.vocab = set()

    def train(self, data):
        total_spam = sum(1 for label in data['label'] if label == 'spam')
        total_ham = sum(1 for label in data['label'] if label == 'ham')
        total_emails = total_spam + total_ham

        self.class_probs['spam'] = total_spam / total_emails
        self.class_probs['ham'] = total_ham / total_emails

        spam_words = {}
        ham_words = {}

        for index, row in data.iterrows():
            words = row['email'].split()
            if row['label'] == 'spam':
                for word in words:
                    spam_words[word] = spam_words.get(word, 0) + 1
                    self.vocab.add(word)
            else:
                for word in words:
                    ham_words[word] = ham_words.get(word, 0) + 1
                    self.vocab.add(word)

        total_spam_words = sum(spam_words.values())
        total_ham_words = sum(ham_words.values())

        for word in self.vocab:
            spam_count = spam_words.get(word, 0)
            ham_count = ham_words.get(word, 0)

            self.word_probs[word] = {
                'spam': (spam_count + 1) / (total_spam_words + len(self.vocab)),
                'ham': (ham_count + 1) / (total_ham_words + len(self.vocab))
            }

    def predict(self, email):
        words = email.split()
        spam_score = self.class_probs['spam']
        ham_score = self.class_probs['ham']

        for word in words:
            if word in self.word_probs:
                spam_score *= self.word_probs[word]['spam']
                ham_score *= self.word_probs[word]['ham']

        return 'spam' if spam_score > ham_score else 'ham'