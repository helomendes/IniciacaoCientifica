import csv
import numpy as np
from sklearn.metrics import f1_score

class KNearstNeighbors:
    #iniciliziador
    def __init__(self, neighbors):
        self.k = neighbors

    def fit_Train(self, xtrain, ytrain):
        self.X_train = xtrain
        self.y_train = ytrain

    def fit_Test(self, xtest, ytest):
        self.X_test = xtest
        self.y_test = ytest
    
    def fit_scaling(self, coluna_train):
        self.min = np.min(coluna_train)
        self.max = np.max(coluna_train)

    def scaler(self, x):
        y = (x - self.min) / (self.max - self.min)
        return y

    def scalingCols(self, i):
        self.fit_scaling(self.X_train[:, i])
        if (self.max == self.min):
            self.X_train[:, i] = np.zeros_like(self.X_train[:, i])
            self.X_test[:, i] = np.zeros_like(self.X_test[:, i])
        else:
            self.X_train[:, i] = self.scaler(self.X_train[:, i])
            self.X_test[:, i] = self.scaler(self.X_test[:, i])
    
    def euclidian_distance(self, test):
        return np.linalg.norm(self.X_train - test, axis=1)
    
    def predict_single(self, test):
        dists = self.euclidian_distance(test)
        k_distances = np.argpartition(dists, self.k)[:self.k]
        #vetor com as classes dos k pontos mais proximos
        k_labels = self.y_train[k_distances]
        most_commom = np.bincount(k_labels.astype(int)).argmax()
        return most_commom

    def predict(self):
        predicts = np.apply_along_axis(self.predict_single, 1, self.X_test)
        return predicts

    def KNN(self, csv_train, csv_test):
        train = np.loadtxt(csv_train, delimiter=',', skiprows=1)
        test = np.loadtxt(csv_test, delimiter=',', skiprows=1)

        X_train = train[:, 1:]
        y_train = train[:, 0]
        X_test = test[:, 1:]
        y_test = test[:, 0]

        self.fit_Train(X_train, y_train)
        self.fit_Test(X_test, y_test)

        for i in range (X_train.shape[1]):
            self.scalingCols(i)

        predicts = self.predict()

        #compara as previsoes de cada teste com o conjunto y_test (gabarito)
        accuracy = np.mean(predicts == y_test)
        print("\t\tAccuracy: ", accuracy)    

        f1 = f1_score(y_test, predicts, average='weighted')
        print("\t\tF1 Score: ", f1)

        return accuracy, f1