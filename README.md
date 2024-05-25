# cleanPyData

An awesome Python package for data cleaning and preprocessing.

cleanPyData is a robust and easy-to-use Python package designed to streamline the data cleaning and preprocessing phase of your data science projects. It provides essential functionalities for handling missing values, normalizing data, extracting important features, and detecting outliers, ensuring that your data is ready for analysis or machine learning.

## Features

- Handle Missing Values: Clean your dataset by filling in missing values using various strategies (mean, median, mode) or by dropping them entirely.
- Normalize Data: Apply normalization techniques such as Min-Max scaling and Z-score normalization to standardize your data.
- Feature Extraction: Select the most important features from your dataset to improve model performance and reduce overfitting.
- Outlier Detection: Detect and remove outliers using methods like Z-score and Interquartile Range (IQR).

### Built With

- Python
- Pandas
- NumPy
- sklearn

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- Python 3.x

### Installation

```sh
pip install cleanPyData
```

## Usage

```sh
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
```

## Roadmap

- [ ] Add more cleaning and preprocessing functionalities
- [ ] Improve performance and efficiency
- [ ] Add more examples and documentation

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [MIT License](https://opensource.org/licenses/MIT) for more information.

## Contact

Kaddu Livingstone - kaddulivingston@gmail.com

Project Link: [https://github.com/Livingston-k/cleanPyData](https://github.com/Livingston-k/cleanPyData)

## Follow Me

- [Follow me on X](https://x.com/KadduLivingston)
- [Follow me on LinkedIn](https://www.linkedin.com/in/kaddu-livingstone/)
