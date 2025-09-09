import json
import pandas as pd

def categorize_trans(df: pd.DataFrame, config_path: str) -> pd.DataFrame:
    with open(config_path, "r") as f:
        categories = json.load(f)

    def find_category(description: str) -> str:
        desc = description.lower()
        for category, keywords in categories.items():
            if any(keyword in desc for keyword in keywords):
                return category
        return "uncategorized"
    
    df["Category"] = df["description"].apply(find_category)
    return df