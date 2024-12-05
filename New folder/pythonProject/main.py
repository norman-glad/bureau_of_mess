# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 14:15:36 2024

@author: Michael
"""

import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import numpy as np

# Load the data
# data = pd.read_csv(r'C:\Users\Jerin Gogi\Downloads\Youtube05-Shakira.csv')

# Display the first few rows of the dataset
print(data.head())
# Display basic information about the dataset
print(data.info())

# Display summary statistics
print(data.describe())

# Check for missing values
print(data.isnull().sum())

# Select only the 'content' and 'class' columns for this project
data = data[['CONTENT', 'CLASS']]

vectorizer = CountVectorizer()

# Fit and transform the content column
X = vectorizer.fit_transform(data['CONTENT'])
y = data['CLASS']

# Shape of the data
print(X.shape)
print(y.shape)

# Feature names
print(vectorizer.get_feature_names_out()[:10])  # Display the first 10 feature names

# Initialize the TfidfTransformer
tfidf_transformer = TfidfTransformer()

# Fit and transform the data
X_tfidf = tfidf_transformer.fit_transform(X)

# Display the shape of the transformed data
print(X_tfidf.shape)

# Shuffle the dataset
data = data.sample(frac=1).reset_index(drop=True)

# Split the dataset into training and testing sets
train_size = int(0.75 * len(data))
train_data = data[:train_size]
test_data = data[train_size:]

# Separate the features and the class
X_train = vectorizer.fit_transform(train_data['CONTENT'])
y_train = train_data['CLASS']
X_test = vectorizer.transform(test_data['CONTENT'])
y_test = test_data['CLASS']

# Initialize the classifier
clf = MultinomialNB()

# Fit the model
clf.fit(X_train, y_train)

# Perform 5-fold cross-validation
cv_scores = cross_val_score(clf, X_train, y_train, cv=5)
print(cv_scores)

# Print the mean accuracy
print(f'Mean cross-validation accuracy: {cv_scores.mean()}')

# Predict the test data
y_pred = clf.predict(X_test)

# Print the confusion matrix
print(confusion_matrix(y_test, y_pred))

# Print the accuracy
print(f'Test accuracy: {accuracy_score(y_test, y_pred)}')

############################################

# New comments (just for checking)
new_comments = [
    "This movie was fantastic! I loved every moment.",
    "Great acting and storyline. Highly recommend!",
    "What a waste of time. Terrible movie.",
    "Loved the cinematography and the plot twists.",
    "Click here to win a free iPhone!",
    "Congratulations! You've won a free trip to the Bahamas!",
    "Hey i have to repeat this movie"
]

# Transform the new comments
new_comments_transformed = vectorizer.transform(new_comments)

# Predict the class of the new comments
new_comments_pred = clf.predict(new_comments_transformed)

# Print the results
for comment, pred in zip(new_comments, new_comments_pred):
    print(f'Comment===> {comment}\nPredicted Class===> {"Spam" if pred == 1 else "Non-Spam"}\n')

######################################

my_data = pd.read_csv(r'C:\Users\Jerin Gogi\Downloads\Comp 237\Project\Youtube04-Eminem.csv')
my_comments = my_data['CONTENT']

# Transform the new comments
my_comments_transformed = vectorizer.transform(my_comments)

# Predict the class of the new comments
my_comments_pred = clf.predict(my_comments_transformed)

# Print the results
for comment, pred in zip(my_comments, my_comments_pred):
    print(f'Comment===> {comment}\nPredicted Class===> {"Spam" if pred == 1 else "Non-Spam"}\n')

'''
DATA VISULIZATION
'''

# Class distribution
class_counts = data['CLASS'].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(class_counts.index, class_counts.values, color=['green', 'red'], tick_label=['Non-Spam', 'Spam'])
plt.title('Distribution of Classes')
plt.xlabel('Class')
plt.ylabel('Count')
plt.show()

# Feature importance (Top 20 features by TF-IDF score)
tfidf_weights = np.asarray(X_tfidf.mean(axis=0)).flatten()
feature_names = vectorizer.get_feature_names_out()
num_top_features = min(20, len(feature_names))  # Use the smaller of 20 or the number of features
top_indices = np.argsort(tfidf_weights)[::-1][:num_top_features]

# Ensure no out-of-bounds indices
top_indices = top_indices[top_indices < len(feature_names)]  # Filter out any out-of-bounds indices

# Plot the top features
plt.figure(figsize=(10, 6))
plt.barh([feature_names[i] for i in top_indices], tfidf_weights[top_indices], color='skyblue')
plt.title('Top 20 Features by TF-IDF Weight')
plt.xlabel('TF-IDF Weight')
plt.ylabel('Feature')
plt.gca().invert_yaxis()  # Invert y-axis for descending order
plt.show()

# Cross-validation scores
plt.figure(figsize=(6, 4))
plt.bar(range(1, len(cv_scores) + 1), cv_scores, color='orange', tick_label=range(1, len(cv_scores) + 1))
plt.title('Cross-Validation Accuracy Scores')
plt.xlabel('Fold')
plt.ylabel('Accuracy')
plt.ylim(0, 1)
plt.show()

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 5))
plt.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.colorbar()
tick_marks = np.arange(2)
plt.xticks(tick_marks, ['Non-Spam', 'Spam'])
plt.yticks(tick_marks, ['Non-Spam', 'Spam'])
plt.xlabel('Predicted Class')
plt.ylabel('True Class')

# Add text annotations for matrix values
for i in range(conf_matrix.shape[0]):
    for j in range(conf_matrix.shape[1]):
        plt.text(j, i, conf_matrix[i, j], ha='center', va='center', color='black')
plt.show()




