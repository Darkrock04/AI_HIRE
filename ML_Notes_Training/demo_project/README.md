# Sentiment Analysis using Bag of Words (BoW)

Welcome to your first practical Machine Learning project!

## The Goal
In this project, we are training a model to understand human emotion in text. Given a sentence (like a movie review or a tweet), the model will predict whether the sentiment is **Positive** or **Negative**.

## The Data
We are using the `sentiment_data.csv` dataset, which contains text samples labeled with their sentiment. 
*Note: This is a large dataset (~23MB), which gives our model plenty of examples to learn from!*

## The Approach: Bag of Words (BoW)
Machine learning models only understand numbers, not words. The **Bag of Words** technique solves this by:
1. Creating a "vocabulary" of all unique words in the dataset.
2. Converting each sentence into an array of numbers, where each number represents how many times a specific word from the vocabulary appears in that sentence.

## Getting Started
Open the `Sentimental_Analysis_Using_BOW.ipynb` notebook to walk through the code step-by-step. You will see how we load the data, apply the BoW transformation, train a classification model, and evaluate its accuracy!
