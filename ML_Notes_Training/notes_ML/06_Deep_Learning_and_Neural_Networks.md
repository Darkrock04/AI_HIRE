# Module 6: Deep Learning and Neural Networks

Deep Learning is a subset of Machine Learning that ignores classical algorithms (Decision Trees, Linear Regressions) in favor of **Artificial Neural Networks**, architectures modeled loosely after the human brain.

## 1. What is an Artificial Neural Network (ANN)?

A Neural Network is composed of layers of nodes. We call these nodes "neurons".
*   **Input Layer:** The raw data goes in here.
*   **Hidden Layers:** The magic happens here. The data passes through multiple interconnected layers where intense mathematical transformations occur. If a network has many hidden layers, it is considered a "Deep" Neural Network.
*   **Output Layer:** The final prediction comes out here.

### Weights, Biases, and Activation
Every connection between two neurons has a **Weight** (a number acting as a multiplier). A **Bias** is added to adjust the output. 
Finally, the result passes through an **Activation Function** (like ReLU or Sigmoid), which decides if that particular neuron should "fire" or not.

### Backpropagation
When the Neural Net makes a prediction, it compares the answer to the truth. Usually, its first guess is terrible. 
It calculates the error (loss) and then physically travels *backwards* through the entire network, tweaking and adjusting every single weight connection to try and reduce that error for the next time. This process is called **Backpropagation**.

---

## 2. Specialized Neural Networks

A standard ANN (Dense Network) is not very good at handling images or sequences. To solve this, researchers developed specialized architectures.

### CNN (Convolutional Neural Networks)
**Used primarily for: Computer Vision (Image Recognition, Facial Detection).**
A CNN doesn't just stretch an image into a flat line of pixels. Instead, it slides "filters" across the 2D image matrix. These filters are hunting for specific patterns like vertical lines, edges, curves, and eventually entire shapes (like an eye or a car wheel). 

### RNN (Recurrent Neural Networks)
**Used primarily for: Sequence Data (Text, Audio, Time Series).**
A standard Neural Network suffers from "amnesia"—it processes inputs independently and has no memory. If you feed it a sentence, it has forgotten the first word by the time it reaches the third word.
RNNs possess an internal "loop" that allows information to persist. They maintain a hidden state that represents the "memory" of everything they have processed so far.

**Limitations of RNNs:** While brilliant for short sequences, RNNs suffer from the "vanishing gradient" problem. If a paragraph is too long, the RNN completely forgets what happened at the start. To fix this, architectures like **LSTMs** (Long Short-Term Memory) were invented. 

However, even LSTMs were fundamentally slow because they read sequences strictly word-by-word. This bottleneck led to the invention of the Transformer (which we will cover in `08_Large_Language_Models_and_ChatGPT.md`).

---

> **Next Step:** Proceed to `07_Evolution_of_NLP_and_Embeddings.md` to see how Deep Learning revolutionized the way computers read language.
