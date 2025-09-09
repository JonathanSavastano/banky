from parser import load_statement
from categorizer import categorize_trans
import pandas as pd

def main():
    df = load_statement("data/Checking1.csv")
    categorized_df = categorize_trans(df, "config/categories.json")
    summary = categorized_df.groupby("Category")["amount"].sum().sort_values(ascending=False)

    print("\n Spending Summary: ")
    print(summary)


if __name__ == "__main__":
    main()