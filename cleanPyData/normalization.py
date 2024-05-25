from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd

def normalize_data(df, method='minmax'):
    if method == 'minmax':
        scaler = MinMaxScaler()
    elif method == 'zscore':
        scaler = StandardScaler()
    else:
        raise ValueError("Invalid method. Use 'minmax' or 'zscore'.")
    
    return pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
