import pickle
from preprocess import clean_text

# Load the trained model
with open('../models/spam_classifier.pkl', 'rb') as model_file:
    classifier = pickle.load(model_file)

# List of new emails to filter
new_emails = [
    "다음 주에 중요한 시험이 있어. 오늘부터 공부 시작해야겠다.",
    "당신의 계정에 대해 중요한 알림이 있습니다. 즉시 확인해 주세요.",
    "이번 주말에 여행 준비 잘 돼가? 어디로 가면 좋을까?",
    "오늘 한정 기회! 바로 확인하여 특별 할인 혜택을 받으세요.",
    "그 드라마 정말 재미있었어. 다음에 또 봐야겠다.",
    "긴급 공지! 계좌를 업데이트하지 않으면 거래가 제한될 수 있습니다.",
    "너 오늘 뭐하고 있어? 언제쯤 만날 수 있을까?",
    "경고! 계좌에 의심스러운 거래가 있습니다. 즉시 확인하세요!",
    "오늘 피자 먹고 싶어. 괜찮으면 같이 먹자!",
    "긴급 알림! 계좌에 대한 중요한 업데이트가 필요합니다. 즉시 확인하세요!",
    "오늘은 내가 좋아하는 음식 먹을 거야. 기대된다!",
    "지금 클릭하여 최대 50% 할인 혜택을 누리세요!",
    "다음 주에 중요한 회의가 있어. 준비 잘해야겠다.",
    "당신의 카드가 비활성화되었습니다. 즉시 복구 절차를 진행하세요.",
    "오늘 저녁 뭐 먹을지 고민 중이다. 너는?",
    "중요한 알림! 계좌에 이상이 있습니다. 즉시 확인하여 복구하세요.",
    "오늘 일찍 퇴근해서 친구랑 만나기로 했어. 재밌을 것 같아."
]

# Clean the new email data
cleaned_emails = [clean_text(email) for email in new_emails]

# Predict the labels for the new email data
predicted_labels = [classifier.predict(email) for email in cleaned_emails]

# Print the results
for email, label in zip(new_emails, predicted_labels):
    print(f"Email: {email}\nLabel: {label}\n")