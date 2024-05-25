from sklearn.feature_selection import SelectKBest, f_classif

def extract_features(df, target, k=10):
    X = df.drop(columns=[target])
    y = df[target]
    selector = SelectKBest(score_func=f_classif, k=k)
    selector.fit(X, y)
    selected_features = X.columns[selector.get_support()]
    return df[selected_features]
