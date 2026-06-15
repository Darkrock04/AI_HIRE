# Module 7: Evolution of NLP and Embeddings

Historically, computers struggled tremendously to understand the nuances, sarcasm, and profound context of human language. However, incredible breakthroughs have evolved NLP rapidly.

## 1. Evolution of AI Language Processing (Timeline)
The journey from basic pattern matching to reasoning engines:

*   **1966 - ELIZA:** Pattern-matching therapist chatbot. This was fundamentally a sequence of clever "If-Then" rules.
*   **1998 - Statistical NLP:** Language through math using *n-grams* (calculating the statistical probability of which word comes next).
*   **2013 - Word2Vec:** The invention of words with meaning & direction (Word Embeddings). This changed everything.
*   **2017 - Transformers:** The legendary "Attention is all you need" paper was released.
*   **2018 - BERT:** An encoder developed by Google that "reads both ways", giving deep context to words.
*   **2020 - GPT-3:** An AI that successfully "writes like a human."
*   **2023 - GPT-4:** A model that sees, writes, solves, and *reasons*.

---

## 2. Word Embeddings and Word2Vec (2013)
As covered in Module 5, Bag of Words and TF-IDF completely ignore the *meaning* of words. Google fixed this in 2013 by inventing Word2Vec.

Instead of counting words, Word2Vec maps every single word into an algebraic multi-dimensional space (an **Embedding**). 
If two words have similar mathematical coordinates, the computer knows they mean similar things.
Because they are algebraic coordinates, you can literally do math on language:
`King - Man + Woman = Queen`

---

## 3. Encoders: Upgrading from Words to Sequences
Word2Vec was amazing, but it mapped single, isolated words. But human language relies on sequences. The word "Bank" means something entirely different in "River Bank" versus "Bank Account".

This is where **Encoders** come in.
An **Encoder** is a deep learning model that converts an entire sequence of words into an embedding (vector representation).

### How Encoders Work
If you pass the sequence `["They", "sent", "me", "a"]` into an Encoder, it outputs a dense array of vectors. 
For example:
*   `[sentence]` -> `<-0.44, ..., -1.1>` (A vector representing the whole sentence)
*   `They` -> `<-0.27, ..., 4.31>`
*   `sent` -> `<1.54, ..., -2.92>`
*   `me` -> `<0.91, ..., -1.78>` 
*   `a` -> `<-0.71, ..., 2.45>`

Notice that these are not 1s and 0s like Bag of Words. They are highly complex dense vectors containing deep semantic meaning.

### Famous Encoder Examples
*   **BERT** (Bidirectional Encoder Representations from Transformers): The most famous encoder. It reads the whole sentence at once (left-to-right AND right-to-left) to capture perfect context.
*   **MiniLM**
*   **RoBERTa**
*   **DistilBERT** (A lighter, faster version of BERT)
*   **SBERT** (Sentence-BERT for sentence similarity)

### Primary Uses
Encoders are primarily used for embedding tokens, entire sentences, and whole documents. Once you have an embedded document, you can perform highly complex tasks like Semantic Search (finding documents that *mean* the same thing, even if they don't share any of the same words).

---

> **Next Step:** Proceed to the final block, `08_Large_Language_Models_and_ChatGPT.md`, where we look at the ultimate evolutionary form of NLP.
