import pandas as pd
from cleanPyData.normalization import normalize_data

def test_normalize_data_minmax():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    result = normalize_data(df, method='minmax')
    assert result.min().min() == 0
    assert result.max().max() == 1

def test_normalize_data_zscore():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    result = normalize_data(df, method='zscore')
    assert round(result.mean().mean(), 6) == 0
    assert round(result.std().std(), 6) == 1
