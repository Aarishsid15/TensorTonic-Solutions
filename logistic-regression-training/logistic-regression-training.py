import numpy as np

def _sigmoid(z):
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):

    w = np.zeros(X.shape[1])
    b = 0

    for _ in range(steps):

        # linear combination
        z = np.dot(X, w) + b

        # sigmoid
        y_pred = _sigmoid(z)

        # gradients
        m = X.shape[0]
        dw = (1/m) * np.dot(X.T, (y_pred - y))
        db = (1/m) * np.sum(y_pred - y)

        # update parameters
        w = w - lr * dw
        b = b - lr * db

    return w, b