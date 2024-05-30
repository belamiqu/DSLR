import numpy as np
import matplotlib.pyplot as plt

""" Definition of a logistic regression classifier using the OVR strategy.
 They allow for training, prediction, and evaluation of the model."""

class LogisticRegressionOVR:
    def __init__(self, data, w=[], eta= 0.01, n_iter=300, v=True, prediction=False):
        self.eta = eta
        self.n_iter = n_iter
        self.w = w
        self.v = v
        self.X = None
        self.y = None
        self._processing(data, prediction)

    """Mean normalization"""

    def _scaling(self, X):
        for i in range(len(X)):
            X[i] = (X[i] - X.mean()) / X.std()
        return X
    
    """Removing certain columns and applying scaling."""

    def _processing(self, hptrain, pred=True):

        hptrain = hptrain.drop(['Astronomy', 'Care of Magical Creatures', 'Transfiguration'], axis=1)
        if pred == False:

            hp_features = np.array((hptrain.iloc[:, 1:]))
            hp_labels = np.array(hptrain.loc[:, "Hogwarts House"])
            np.apply_along_axis(self._scaling, 0, hp_features)
            hp_features = np.insert(hp_features, 0, 1, axis=1)
            self.X = hp_features
            self.y = hp_labels
            return hp_features, hp_labels
        else:
            hptrain = hptrain.iloc[:, 1:]
            hp_features = np.array(hptrain)
            np.apply_along_axis(self._scaling, 0, hp_features)
            hp_features = np.insert(hp_features, 0, 1, axis=1)
            self.X = hp_features
            return hp_features, None
    
    """Returns the output of the sigmoid function."""

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    """This method trains model using gradient descent. It iterates over each class,
      computes the output, calculates the error, updates the weights, and repeats 
      It also optionally visualizes the training progress and cost over iterations."""
    
    def fit(self):
        f, axs = plt.subplots(2, 2, figsize=(10, 8))
        X, y = self.X, self.y
        cost = []
        index = []
        for (n, i) in enumerate(np.unique(y)):
            print(f' Training against : {i}')
            y_copy = np.where(y == i, 1, 0)
            w = np.ones(X.shape[1]) 
            for _ in range(self.n_iter):
                output = X.dot(w)
                sig = self._sigmoid(output)
                errors = y_copy - sig
                if self.v == True:
                    index.append(_)
                    cost.append(abs(errors.mean()))
                gradient = np.dot(X.T, errors) / X.shape[1]
                w += self.eta * gradient
                if ((_ * 100) / self.n_iter) % 5 == 0:
                    print(f'training progress {"{:.2f}".format((_ * 100) / self.n_iter)}%', end='\r')

            self.w.append((w, i))
            if self.v == True:
                if n == 0:
                    xx = 0
                    yy = 0
                elif n == 1:
                    xx = 0
                    yy = 1
                elif n == 2:
                    xx = 1
                    yy = 0
                else:
                    xx = 1
                    yy = 1
                axs[xx, yy].set_title(i)
                axs[xx, yy].plot(index, cost, 'b-')
                cost = []
                index = []
        if self.v == True:
            plt.show()

        return self.w
    
    """This method predicts the class label for a single input"""

    def _predict_one(self, x, weights=None):
        if weights is None:
            weights = self.w

        if isinstance(weights, dict):
            return max((x.dot(w), c) for c, w in weights.items())[1]
        else:
            return max((x.dot(w), c) for w, c in weights)[1]

    """This method returns a list of the class labels""" 

    def predict(self, weights=None):

        if weights == None:
            weights = self.w
        X, y = self.X, self.y
        return [self._predict_one(i, weights) for i in X]
    
    """This method calculates the accuracy of the model """
    
    def score(self):
        return sum(self.predict() == self.y) / len(self.y)