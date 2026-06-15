# The RNN Training Workflow: Sequential Data Mastery

Training a Recurrent Neural Network (RNN) or LSTM involves steps specifically tailored for sequential data (like text or time series).

## Step 1: Sequential Data Preparation
Unlike tabular data, sequential data needs special formatting:
*   **Tokenization (for text):** Converting words into numbers (tokens).
*   **Padding:** Neural networks require uniform input sizes. We "pad" short sequences with zeros and "truncate" long sequences to a fixed length.
*   **3D Tensors:** RNNs expect data in the shape `[batch_size, time_steps, features]`.

## Step 2: The Embedding Layer (For Text)
Instead of feeding raw token numbers to the RNN, we usually start with an `Embedding` layer. 
*   It converts simple word indices into dense vectors of fixed size, capturing semantic meaning (words with similar meanings have similar vectors).

## Step 3: Designing the Sequence Architecture
1.  **Input/Embedding:** Process the initial sequence.
2.  **RNN/LSTM/GRU Layers:** The core sequence processors. You can stack them. If you stack RNN layers, you must set `return_sequences=True` for all but the last RNN layer.
3.  **Dense Layers:** We typically add standard Dense layers at the end to make the final prediction based on the RNN's output.

## Step 4: Compiling and Training
Similar to ANNs, we compile using an Optimizer (Adam) and a Loss function.
*   Training RNNs is computationally expensive and slow compared to standard ANNs because sequences must be processed step-by-step.

## Step 5: Evaluation
We evaluate performance. For text generation, we might look at Perplexity; for sequence classification, standard metrics like Accuracy and F1-Score apply.

---
> 👉 **Next Step:** Open `RNN_workflow.ipynb` to see how an LSTM is built for text classification!
