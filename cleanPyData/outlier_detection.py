import numpy as np
import pandas as pd

def detect_outliers(df, method='zscore', threshold=3):
    if method == 'zscore':
        z_scores = np.abs((df - df.mean()) / df.std())
        return df[(z_scores < threshold).all(axis=1)]
    elif method == 'iqr':
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        return df[((df >= (Q1 - 1.5 * IQR)) & (df <= (Q3 + 1.5 * IQR))).all(axis=1)]
    else:
        raise ValueError("Invalid method. Use 'zscore' or 'iqr'.")
