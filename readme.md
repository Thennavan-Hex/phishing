# Phishing Website Detection by Machine Learning Techniques

## Objective
Phishing websites pose a significant threat in today's digital landscape, often masquerading as legitimate entities to deceive users. The aim of this project is to employ machine learning models and deep neural networks to predict phishing websites effectively.

## Data Collection
- Phishing URLs are sourced from the open-source service , which provides regularly updated datasets in various formats such as CSV and JSON.
- Legitimate URLs are obtained from the open datasets provided by the University of New Brunswick. Specifically, the benign URL dataset is utilized for this project.

## Feature Extraction
Features are extracted from the URL data across three categories:
1. **Address Bar-based Features:** Extracting features related to the URL itself.
2. **Domain-based Features:** Incorporating features derived from the domain of the URL.
3. **HTML & JavaScript-based Features:** Extracting features from the HTML and JavaScript content of the website.

## Models & Training
The dataset is split into 80-20 for training and testing purposes. Supervised machine learning models considered for training include:
- Decision Tree
- Random Forest
- Multilayer Perceptrons
- XGBoost
- Autoencoder Neural Network
- Support Vector Machines

## Presentation
A concise video presentation of the project is available, accompanied by presentation slides.

## End Results
The XGBoost Classifier exhibited the highest performance among the models. Future developments of this project may include creating a browser extension for real-time phishing website detection and developing a user-friendly GUI application for predicting the nature of URLs.

This project utilizes machine learning techniques to combat phishing attacks effectively. If you require any additional clarification, feel free to reach out.