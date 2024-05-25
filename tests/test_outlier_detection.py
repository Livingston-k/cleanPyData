import pandas as pd
from cleanPyData.outlier_detection import detect_outliers

def test_detect_outliers_zscore():
    df = pd.DataFrame({'A': [1, 2, 3, 100], 'B': [4, 5, 6, 200]})
    result = detect_outliers(df, method='zscore', threshold=3)
    assert len(result) == 3

def test_detect_outliers_iqr():
    df = pd.DataFrame({'A': [1, 2, 3, 100], 'B': [4, 5, 6, 200]})
    result = detect_outliers(df, method='iqr')
    assert len(result) == 3
