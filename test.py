# Import necessary libraries

from urllib.parse import urlparse
import re
import whois
import datetime

# Function to extract features from URL
def extract_features(url):
    # Initialize an empty feature vector
    features = []

    # Extract the domain from the URL using urlparse
    domain = urlparse(url).netloc

    # Feature 1: Length of the domain
    features.append(len(domain))

    # Feature 2: Presence of 'https' in the URL
    features.append(1 if 'https' in url else 0)

    # Feature 3: Presence of '@' in the domain (possible phishing indicator)
    features.append(1 if '@' in domain else 0)

    # Feature 4: Number of dots in the domain
    features.append(domain.count('.'))

    # Feature 5: Presence of IP address in the domain
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    features.append(1 if re.search(ip_pattern, domain) else 0)

    # Feature 6: Age of the domain
    try:
        w = whois.whois(domain)
        if w.creation_date:
            domain_creation_date = w.creation_date
            if isinstance(domain_creation_date, list):
                domain_creation_date = domain_creation_date[0]
            age = (datetime.datetime.now() - domain_creation_date).days
            features.append(age)
        else:
            features.append(0)
    except whois.parser.PywhoisError:
        features.append(0)

    return features


# Function to train and predict using decision tree classifier
def train_and_predict(X_train, y_train, X_test):
    clf = tree.DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    return clf.predict(X_test)

# Sample training data
training_data = [
    ['https://www.google.com', 0],
    ['https://www.openai.com', 0],
    ['https://www.paypal.com', 0],
    ['https://www.fake-phishing.com', 1],
    ['https://www.unsecurewebsite.net', 1]
]

# Preprocessing the training data
X_train = []
y_train = []
for data in training_data:
    url = data[0]
    label = data[1]
    features = extract_features(url)
    X_train.append(features)
    y_train.append(label)

# Sample testing data
testing_data = [
    ['https://www.test-phishing.com', 1],
    ['https://www.test-legitimate.com', 0]
]

# Preprocessing the testing data
X_test = []
y_test = []
for data in testing_data:
    url = data[0]
    label = data[1]
    features = extract_features(url)
    X_test.append(features)
    y_test.append(label)

# Train the classifier and predict the labels for the test data
predictions = train_and_predict(X_train, y_train, X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)

# Print the evaluation metrics
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
