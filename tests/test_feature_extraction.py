import pandas as pd
from cleanPyData.feature_extraction import extract_features

def test_extract_features():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [2, 3, 4, 5],
        'C': [5, 6, 7, 8],
        'target': [1, 0, 1, 0]
    })
    result = extract_features(df, target='target', k=2)
    assert list(result.columns) == ['A', 'B']
