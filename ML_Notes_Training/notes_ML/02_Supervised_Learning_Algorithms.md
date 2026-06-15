# Module 2: Supervised Learning Algorithms

Supervised Learning is the most common form of Machine Learning. We provide the algorithm with a dataset containing input features (`X`) and the correct output labels (`y`), and it learns the mapping function from `X` to `y`.

## The Two Main Branches

### 1. Regression (Predicting Numbers)
Used when the target variable is continuous (numeric).
*   *Examples:* Predicting house prices, stock market values, temperature, or a person's salary based on years of experience.

### 2. Classification (Predicting Categories)
Used when the target variable is discrete (categorical).
*   *Examples:* Predicting if an email is Spam/Not Spam, if a tumor is Malignant/Benign, or if a movie review is Positive/Negative/Neutral.

---

## Core Algorithms

Here are the most fundamental Supervised Learning algorithms you need to know.

### 1. Linear Regression
*   **Concept:** Tries to draw the "best fit" straight line through the data points.
*   **Type:** Regression.
*   **How it works:** It finds the relationship between independent variables (like square footage) and a dependent variable (like price) using the line equation `y = mx + b`. It adjusts `m` (slope) and `b` (intercept) to minimize the distance between the line and the actual data points.
*   **Best for:** Simple relationships where variables increase or decrease together linearly.

### 2. Logistic Regression
*   **Concept:** Despite the name, this is a **Classification** algorithm. It draws a straight line (decision boundary) to separate classes, and then maps the outputs into probabilities using an S-shaped curve (Sigmoid function).
*   **Type:** Classification (primarily Binary - 0 or 1).
*   **How it works:** It calculates the *probability* that a data point belongs to a certain class. If the probability is > 50%, it assigns it to Class 1. If < 50%, it assigns it to Class 0.
*   **Best for:** Binary classification like Credit Card fraud detection or Spam detection.

### 3. Support Vector Machines (SVM)
*   **Concept:** Finds the widest possible "street" (margin) that separates different classes of data.
*   **Type:** Classification (mainly) and Regression (SVR).
*   **How it works:** It plots data in high-dimensional space and finds a boundary line (hyperplane) that perfectly separates the categories while maintaining the maximum distance away from the nearest data points of each class (the "support vectors").
*   **Best for:** Complex datasets, high-dimensional spaces (like Text Classification / TF-IDF), and situations where a clear margin of separation exists.

### 4. Decision Trees
*   **Concept:** Makes decisions by answering a series of "Yes/No" questions, forming a tree-like structure.
*   **Type:** Classification and Regression.
*   **How it works:** It splits the data at "nodes" based on feature values that best separate the classes (e.g., "Is Age > 30?", "Is Salary < $50k?"). It continues splitting until it reaches a final decision (the "leaf" node).
*   **Best for:** Data with complex, non-linear relationships. Very easy for humans to interpret and visualize.
*   **Weakness:** Prone to "overfitting" (memorizing the training data instead of learning general patterns).

### 5. Random Forest (Ensemble Learning)
*   **Concept:** An "ensemble" (group) of many Decision Trees. "Wisdom of the crowd."
*   **Type:** Classification and Regression.
*   **How it works:** Builds dozens or hundreds of Decision Trees, each trained on a random, slightly different subset of the data. When asked to make a prediction, it asks all of its trees to vote, and the majority wins.
*   **Best for:** Almost everything! It fixes the overfitting problem of single Decision Trees and is incredibly accurate out-of-the-box.

### 6. Naive Bayes
*   **Concept:** Based purely on probability and Bayes' Theorem.
*   **Type:** Classification.
*   **How it works:** Calculates the probability of a data point belonging to a class based on prior knowledge. It is "Naive" because it assumes every feature is completely independent of every other feature (e.g., it assumes the word "Chicago" has no relationship to the word "Bulls").
*   **Best for:** Text Classification (Spam filtering, Sentiment analysis) with Bag of Words. Extremely fast and works well with small amounts of data.

---
> **Next Step:** Proceed to `03_Unsupervised_Learning_Algorithms.md` to explore how algorithms learn without answers.
