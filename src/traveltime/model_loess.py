import json

import scipy.interpolate
import statsmodels.nonparametric.smoothers_lowess


class Loess:
    def __init__(self, frac=0.01):
        self.frac = frac
        self.y_sm = None
        self.fnc = None

    def is_fitted(self):
        return self.fnc is not None

    def fit(self, X, y):
        # y_sm is a Nx2-array of X and y_hat
        self.y_sm = statsmodels.nonparametric.smoothers_lowess.lowess(
            y, X, frac=self.frac)
        self.fnc = scipy.interpolate.interp1d(self.y_sm[:,0], self.y_sm[:,1])
        return self

    def predict(self, X):
        if not self.is_fitted():
            raise ValueError("Model needs to be fitted before prediction")
        return self.fnc(X)

    def save(self, conn):
        json.dump(self.y_sm.tolist(), conn)

    @classmethod
    def load(cls, conn):
        self = cls()  # Instanciate a new Loess object
        self.y_sm = numpy.array(json.load(conn))  # load the fitted array
        self.fnc = scipy.interpolate.interp1d(self.y_sm[:,0], self.y_sm[:,1])
        return self
