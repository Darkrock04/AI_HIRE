# Deep Learning (DL) 🧠

**What is Deep Learning?**
Deep Learning is a more advanced subset of Machine Learning. Instead of simple mathematical formulas, it uses **Artificial Neural Networks**—algorithms inspired by the structure of the human brain. We use Deep Learning when the data is incredibly complex, like large paragraphs of text or massive numerical datasets.

## How Does Training Work Here?
Training a Neural Network is more complex than traditional ML. It happens in cycles:
1. **Build the Brain:** We construct layers of "neurons". An Input Layer, several Hidden Layers, and an Output Layer.
2. **Forward Pass:** We feed data into the network. The network makes a random guess at the answer.
3. **Calculate Loss:** The network compares its guess to the actual correct answer and calculates how "wrong" it was (the Loss).
4. **Backpropagation (Learning):** The network goes backward and tweaks its internal connections (Weights) to be slightly less wrong next time.
5. **Epochs:** Steps 2-4 are repeated hundreds of times (called Epochs) until the network becomes highly accurate!

## Python Modules Used for DL
Because neural networks require massive mathematical power, we don't use `scikit-learn` here. Instead, we use:

*   **`TensorFlow` & `Keras`:** These are the industry-standard Deep Learning libraries created by Google. They allow us to easily stack layers of neurons together (using `keras.Sequential`) and tell the network how to learn (using Optimizers like `Adam`).
