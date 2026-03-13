import pandas as pd

def analyze_csv(file):
    df = pd.read_csv(file.file)
    summary = df.describe(include="all").to_string()
    columns = list(df.columns)

    return {
        "columns":columns,
        "summary":summary
    }