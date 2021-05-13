import numpy as np

def null_count(df):
    return df.isna().sum().sum()

def train_test_split(df, frac):
    train, test = np.split(df, [int(round(frac*len(df)))])
    return(train, test)

def randomize(df, seed):
    df = df.copy()
    np.random.seed(seed)

    #df = df.iloc[np.random.permutation(len(df))]
    #df.reset_index(drop=True, inplace=True)

    df.apply(np.random.shuffle, axis=0)
    df = df.T
    df.apply(np.random.shuffle, axis=0)
    df = df.T
    return df

