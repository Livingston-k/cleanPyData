import pandas as pd
from cleanPyData import (
    handle_missing_values,
    normalize_data,
    extract_features,
    detect_outliers
)

# Example DataFrame
data = {
    'A': [1, 2, None, 4],
    'B': [4, None, 6, 8],
    'C': [5, 6, 7, 8],
    'target': [1, 0, 1, 0]
}
df = pd.DataFrame(data)

# Handle missing values
df = handle_missing_values(df, strategy='mean')

# Normalize data
df = normalize_data(df, method='minmax')

# Extract features
df = extract_features(df, target='target', k=2)

# Detect outliers
df = detect_outliers(df, method='zscore', threshold=3)

print(df)
