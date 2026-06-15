# Recurrent Neural Networks (RNN)

A **Recurrent Neural Network (RNN)** is a specialized Deep Learning architecture designed to process sequential data, where the order of the data matters.

## 1. The Problem with Standard ANNs
Standard Dense networks process inputs independently and have no "memory". If you feed a standard ANN a sentence, it treats each word in isolation.

## 2. How RNNs Work
RNNs possess an internal "loop". They maintain a **Hidden State** that represents the "memory" of everything they have processed in the sequence so far.
*   When an RNN processes step `t` in a sequence, it takes two inputs:
    1. The data at step `t` (e.g., the current word).
    2. The hidden state from step `t-1` (the memory of previous words).

## 3. Vanishing Gradient Problem and LSTMs
Standard RNNs suffer from the "vanishing gradient" problem. As the sequence gets longer, the network forgets the earlier parts of the sequence because the gradients used to update the weights become infinitesimally small.

To solve this, specialized RNN cells were created:
*   **LSTM (Long Short-Term Memory):** Uses "gates" (Forget, Input, Output) to control what information is kept in memory and what is thrown away.
*   **GRU (Gated Recurrent Unit):** A slightly simpler, faster alternative to LSTMs.

## 4. Common Use Cases
*   Natural Language Processing (Text Classification, Translation)
*   Time Series Forecasting (Stock prices, Weather prediction)
*   Speech Recognition

> **Next Step:** Proceed to `instructions.md` to understand the workflow for training an RNN, or open `RNN_workflow.ipynb` for the code implementation.
