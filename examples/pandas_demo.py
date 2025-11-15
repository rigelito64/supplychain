import pandas as pd
from io import StringIO

CSV = """order_id,customer,amount,date
1,Alice,120.50,2025-11-01
2,Bob,75.00,2025-11-02
3,Alice,35.25,2025-11-03
4,Charlie,200.00,2025-11-04
5,Bob,25.00,2025-11-05
"""


def load_data():
    """Load example CSV data into a DataFrame."""
    return pd.read_csv(StringIO(CSV), parse_dates=["date"])


def summarize(df: pd.DataFrame):
    """Return several simple summaries and a transformed DataFrame.

    - total_by_customer: sum of `amount` per customer
    - avg_amount: overall average order amount
    - df_with_tax: original df plus a new `amount_with_tax` column (10% tax)
    - recent: rows with date >= 2025-11-03
    """
    total_by_customer = (
        df.groupby("customer", as_index=False)["amount"].sum().rename(columns={"amount": "total_amount"})
    )
    avg_amount = df["amount"].mean()
    df_with_tax = df.copy()
    df_with_tax["amount_with_tax"] = df_with_tax["amount"] * 1.10
    recent = df[df["date"] >= pd.Timestamp("2025-11-03")]
    return total_by_customer, avg_amount, df_with_tax, recent


def main():
    df = load_data()
    total_by_customer, avg_amount, df_with_tax, recent = summarize(df)

    print("Raw data:")
    print(df)

    print("\nTotal by customer:")
    print(total_by_customer)

    print(f"\nAverage order amount: {avg_amount:.2f}")

    print("\nData with 10% tax column:")
    print(df_with_tax)

    print("\nRecent orders (from 2025-11-03):")
    print(recent)


if __name__ == "__main__":
    main()
