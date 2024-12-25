def calculate_accuracy(true_labels, predicted_labels):
    # Calculate the number of correct predictions
    correct_predictions = sum(1 for true, pred in zip(true_labels, predicted_labels) if true == pred)
    # Calculate the accuracy as the ratio of correct predictions to the total number of labels
    return correct_predictions / len(true_labels) if len(true_labels) > 0 else 0

def calculate_precision(true_labels, predicted_labels):
    # Calculate the number of true positives
    true_positives = sum(1 for true, pred in zip(true_labels, predicted_labels) if true == 1 and pred == 1)
    # Calculate the number of predicted positives
    predicted_positives = sum(1 for pred in predicted_labels if pred == 1)
    # Calculate the precision as the ratio of true positives to predicted positives
    return true_positives / predicted_positives if predicted_positives > 0 else 0

def calculate_recall(true_labels, predicted_labels):
    # Calculate the number of true positives
    true_positives = sum(1 for true, pred in zip(true_labels, predicted_labels) if true == 1 and pred == 1)
    # Calculate the number of actual positives
    actual_positives = sum(1 for true in true_labels if true == 1)
    # Calculate the recall as the ratio of true positives to actual positives
    return true_positives / actual_positives if actual_positives > 0 else 0