# loader.py - Load and validate CSV files

import pandas as pd
from exceptions import FileNotFoundError, InvalidCSVEror
import os


def load_csv(filepath: str) -> pd.DataFrame:
    """
    Load a CSV file into DataFrame.
    Raise FileNotFoundError or InvalidCSVEror on failure.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(filepath)

    try:
        df = pd.read_csv(filepath)
    except pd.errors.EmptyDataError:
        raise InvalidCSVEror(filepath, "file is empty")
    except pd.errors.ParserError as e:
        raise InvalidCSVEror(filepath, str(e))
    except Exception as e:
        raise InvalidCSVEror(filepath, str(e))

    if df.empty:
        raise InvalidCSVEror(filepath, "no data rows found")

    return df


def display_summary(df: pd.DataFrame) -> None:
    """Print a human-readable summary of the DataFrame."""
    print("\n CSV Summary")
    print("-" * 40)
    print(f"  Rows   : {len(df)}")
    print(f"  Column : {len(df.columns)}")
    print("\n Column Info:")
    for col in df.columns:
        dtype = str(df[col].dtype)
        nulls = df[col].isnull().sum()
        print(f"   - {col:<20} {dtype:<12} ({nulls} nulls)")
    print("-" * 40 + "\n")

