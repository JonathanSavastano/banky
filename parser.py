import pandas as pd 

def load_statement(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)

    df = df.iloc[:, [0, 1, 4]] # only want columns 1, 2, 5
    df.columns = ["date", "amount", "description"]
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    return df