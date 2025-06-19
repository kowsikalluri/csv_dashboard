import pandas as pd

def auto_clean(df):
    df = df.drop_duplicates()

    for col in df.select_dtypes(include='number'):
        df[col] = df[col].fillna(df[col].median())

    for col in df.select_dtypes(include='object'):
        if not df[col].mode().empty:
            df[col] = df[col].fillna(df[col].mode()[0])

    return df
