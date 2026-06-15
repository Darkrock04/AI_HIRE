# Machine Learning (ML) 🤖

**What is Machine Learning?**
In traditional programming, you write the rules (code) to get an answer. In Machine Learning, you give the computer the data and the answers, and it figures out the rules! We use ML to find patterns in data (like predicting a house price or categorizing an email as spam).

## How Does Training Work Here?
Training a classic Machine Learning model is surprisingly simple and usually follows this 4-step process:
1. **Load Data:** We load a dataset (usually a CSV spreadsheet) containing examples.
2. **Preprocess:** We clean the data and split it into a "Training Set" (to teach the model) and a "Testing Set" (to quiz the model later).
3. **Fit:** We tell the model to study the training data using a simple command like `model.fit(X_train, y_train)`. 
4. **Predict:** We ask the model to guess the answers for the testing set using `model.predict(X_test)` and see how accurate it is!

## Python Modules Used for ML
When you look at the code in this folder, you will see us using these specific Python libraries:

*   **`pandas`:** This is our data manipulation tool. We use it to open CSV files and view the data exactly like an Excel spreadsheet.
*   **`scikit-learn` (`sklearn`):** This is the ultimate Machine Learning library. It contains all the algorithms (like Linear Regression or Random Forest) and the tools to train and evaluate them.
*   **`nltk` (Natural Language Toolkit):** If our data is text (like movie reviews), we use this library to clean the words before feeding them to the model.
