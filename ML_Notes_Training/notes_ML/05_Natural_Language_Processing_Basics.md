# Module 5: Natural Language Processing (NLP) Basics

Natural Language Processing (NLP) is the field that teaches computers to understand written and spoken human language. Because ML algorithms only understand numbers, the primary goal of NLP is to clean text and convert it into numerical representations.

## 1. Text Preprocessing 
Before doing anything, the text is extremely noisy.
*   **Lowercasing:** Converting "Apple" to "apple" so they count as the same word.
*   **Removing Stopwords:** Deleting common conjunctions ("the", "and", "is") that provide zero sentiment value.
*   **Tokenization:** Chopping a full string `"I love learning"` into an array of tokens: `["I", "love", "learning"]`.
*   **Stemming / Lemmatization:** Reducing a word to its base root format. E.g., converting "Running" -> "Run", "Better" -> "Good".

---

## 2. Text Vectorization: Bag of Words (BOW)

This is the most classical form of turning text into numbers.

**How it works:**
BOW converts each document into a large numerical vector, where each element of the vector is simply the **count** of a term in the document.

**Example Corpus (Dataset):**
*   `Doc-1`: we are learning machine learning
*   `Doc-2`: processing natural language data
*   `Doc-3`: machine learning algorithms

**Step 1: Build the Vocabulary (fit)**
The algorithm scans all the documents and extracts every unique word to create a master "vocabulary list":
`[we, are, learning, machine, processing, natural, language, data, algorithms]`

**Step 2: Transform Documents to Vectors**
Now, the algorithm looks at each document and places a count of 1 under words that are present, and a 0 under words that aren't.
For `Doc-1`: `[1, 1, 2, 1, 0, 0, 0, 0, 0]`
*   Notice there is a "2" under "learning" because the word appeared twice in Doc 1.

**Pros/Cons:**
BOW is fast and great for simple tasks, but it loses the *order* of the words (which destroys context) and turns huge libraries of text into incredibly massive, mostly-empty data tables (sparse arrays).

---

## 3. TF-IDF

To fix the core issue of Bag of Words (which treats the word "the" as the most important word in the world just because it appears frequently), we use TF-IDF: **Term Frequency - Inverse Document Frequency**.

*   **TF (Term Frequency):** How often does the word "learning" appear in *this one single document*? High frequency increases the score.
*   **IDF (Inverse Document Frequency):** How often does the word "learning" appear across the *entire dataset* (every document combined)? High frequency decreases the score!

TF-IDF realizes that a word is extremely important if it occurs frequently in one document but is incredibly rare across the rest of the dataset.

---

> **Next Step:** Proceed to `06_Deep_Learning_and_Neural_Networks.md` to see what lies beyond traditional NLP.
