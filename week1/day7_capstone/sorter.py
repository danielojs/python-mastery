# sorter.py - Sort DataFrame by a column, ascending or descending

import pandas as pd
from exceptions import ColumnNotFoundError


def sort_data(df: pd.DataFrame, column: str, descending: bool = False) -> pd.DataFrame:
    """
    Sort the DataFrame by the given column.
    Raises ColumnNotFoundError if the column doesn't exist.
    """
    if column not in df.columns:
        raise ColumnNotFoundError(column, list(df.columns))

    direction = "descending" if descending else "ascending"
    result = df.sort_values(by=column, ascending=not descending).reset_index(drop=True)

    print(f"  Sorted by '{column}' ({direction})")
    return result
