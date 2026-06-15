# Module 1: Introduction to Machine Learning

## What is Machine Learning?
Machine Learning (ML) is a subset of Artificial Intelligence (AI). In traditional programming, humans write code (rules) that takes in data and outputs answers. In Machine Learning, humans provide the computer with **data and answers**, and the computer figures out the **rules**.

### The Traditional Programming Paradigm
`Data + Rules (Code) -> Traditional Program -> Output`

### The Machine Learning Paradigm
`Data + Output (Answers) -> Machine Learning Algorithm -> Rules (Model)`

Once the ML algorithm has "learned" the rules (creating a trained model), we can use those rules on new, unseen data to generate new predictions.

---

## Types of Machine Learning

Machine Learning algorithms are generally split into three main categories based on the type of data they receive and how they learn.

### 1. Supervised Learning
The model is trained on **labeled data**. This means the "answers" are already provided in the training set.
*   **Analogy:** A teacher showing a student flashcards with pictures of animals. The teacher says "This is a cat," "This is a dog." The student eventually learns to recognize them on their own.
*   **Key Tasks:** 
    1.  **Classification:** Predicting a category (e.g., Is this email Spam or Not Spam?).
    2.  **Regression:** Predicting a continuous number (e.g., What will the price of this house be?).

### 2. Unsupervised Learning
The model is trained on **unlabeled data**. The computer receives data without any output/answers and is asked to find hidden patterns, structures, or relationships within it.
*   **Analogy:** Giving a child a box of mixed Legos. Without any instructions, the child might group them by color, or by size, or by shape.
*   **Key Tasks:**
    1.  **Clustering:** Grouping similar data points together (e.g., Customer segmentation for marketing).
    2.  **Dimensionality Reduction:** Compressing complex data into fewer features while retaining the most important information.

### 3. Reinforcement Learning
The model learns by interacting with an **environment** and receiving **rewards or penalties** for its actions.
*   **Analogy:** Training a dog to sit. When it sits, you give it a treat (reward). When it ignores you, it gets nothing (penalty). Over time, the dog figures out that sitting maximizes its treats.
*   **Key Tasks:** Making sequence of decisions, Game playing (Chess, AlphaGo), Robotics, Self-Driving Cars.

---

## The Machine Learning Pipeline

Whether you are building a simple housing price predictor or a massive language model, almost all Machine Learning projects follow this standard workflow:

1.  **Data Collection:** Gathering the raw information.
2.  **Exploratory Data Analysis (EDA):** Checking for missing values, outliers, and understanding the distribution of your data.
3.  **Data Preprocessing:** Cleaning the data, handling missing values, scaling numbers, and translating text/categories into numerical formats the computer can understand.
4.  **Train/Test Split:** Splitting the data into a training set (to teach the model) and a testing set (to evaluate it later). The test set must remain entirely unseen during training.
5.  **Model Selection & Training:** Choosing an algorithm (e.g., Random Forest, Neural Network) and feeding the training data through it so it can learn patterns.
6.  **Evaluation:** Using the unseen Test Set to see how accurate the model's predictions are.
7.  **Hyperparameter Tuning:** Tweaking the internal "settings" of the algorithm to improve the evaluation score.
8.  **Deployment:** Putting the trained model into production (like a website API) so users can interact with it.

---
> **Next Step:** Proceed to `02_Supervised_Learning_Algorithms.md` to explore Classification and Regression models in depth.
