import numpy as np
from pandas import DataFrame


# extending DataFrame class, no need for a constructor

class LambDataframe(DataFrame):

    def null_count(self):
        total_null = self.isna().sum().sum()
        return total_null

    def train_test_split(self, frac):
        train, test = np.split(self, [int(round(frac * len(self)))])
        return (train, test)

    def randomize(self, seed):
        df = self.copy()
        np.random.seed(seed)

        # self = self.iloc[np.random.permutation(len(self))]
        # self.reset_index(drop=True, inplace=True)

        df.apply(np.random.shuffle, axis=0)
        df = df.T
        df.apply(np.random.shuffle, axis=0)
        df = df.T
        return df
