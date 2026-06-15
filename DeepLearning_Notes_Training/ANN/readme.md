# Artificial Neural Networks (ANN)

An **Artificial Neural Network (ANN)** is a computational model inspired by the human brain's biological neural networks. It is the foundation of Deep Learning.

## 1. Core Architecture

An ANN consists of layers of nodes (neurons):
*   **Input Layer:** Receives the raw data features.
*   **Hidden Layers:** Intermediate layers where the network learns complex representations through mathematical transformations.
*   **Output Layer:** Produces the final prediction (e.g., probability of a class, or a continuous value).

### Weights, Biases, and Activation
*   **Weights:** Determine the strength of the connection between neurons.
*   **Biases:** Act as an offset to help the model fit the data better.
*   **Activation Functions:** Introduce non-linearity into the network (e.g., ReLU, Sigmoid, Tanh). Without them, the network would just be a linear regression model, no matter how many layers it has.

## 2. How ANNs Learn

The learning process involves two main phases:

### Forward Propagation
Data is passed from the input layer, through the hidden layers, to the output layer to make a prediction.

### Backpropagation
The network calculates the error (Loss) by comparing its prediction to the actual truth. It then propagates this error backwards through the network, adjusting the weights and biases using an optimizer (like Adam or SGD) to minimize the error.

## 3. Common Use Cases
Standard ANNs (also known as Dense or Fully Connected Networks) are typically used for:
*   Tabular data classification (e.g., predicting diabetes, customer churn).
*   Regression tasks (e.g., predicting house prices based on multiple features).

> **Next Step:** Proceed to `instructions.md` for a step-by-step guide on how we train an ANN, or open `ANN_workflow.ipynb` to see the code in action.
