import pandas as pd
from cleanPyData.cleaning import handle_missing_values

def test_handle_missing_values_mean():
    df = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
    result = handle_missing_values(df, strategy='mean')
    assert result.isnull().sum().sum() == 0

def test_handle_missing_values_drop():
    df = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
    result = handle_missing_values(df, strategy='drop')
    assert len(result) == 1
