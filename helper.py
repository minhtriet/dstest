def preprocess_text(series):
    """
    Preprocess the text column in data frame.
    """
    return series.str.lower()

def preprocess_df(df):
    return df.dropna()