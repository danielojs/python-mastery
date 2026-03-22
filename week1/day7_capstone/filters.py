# filters.py - Parse and apply filter expressions like "age>25" or "name=Alice"

import pandas as pd
import re
from pandas._typing import Scalar
from exceptions import InvalidFilterExpressionError, ColumnNotFoundError

OPERATORS = {
    ">=": lambda col, val: col >= val,
    "<=": lambda col, val: col <= val,
    "!=": lambda col, val: col != val,
    ">" : lambda col, val: col > val,
    "<" : lambda col, val: col < val,
    "=" : lambda col, val: col == val,
}

PATTERN = re.compile(r"^(\w+)\s*(>=|<=|!=|>|<|=)\s*(.+)$")


def _cast_value(series: pd.Series, raw: str) -> Scalar:
    """Try to cast the filter value to match the column's dtype."""
    try:
        if pd.api.types.is_numeric_dtype(series):
            return float(raw) if "." in raw else int(raw)
    except ValueError:
        pass
    return raw


def apply_filter(df: pd.DataFrame, expression: str) -> pd.DataFrame:
    """
    Filter DataFrame rows using an expression like 'age>25' or 'city=Jakarta'.
    Raises InvalidFilterExpressionError or ColumnNotFoundError on bad input.
    """
    match = PATTERN.match(expression.strip())
    if not match:
        raise InvalidFilterExpressionError(expression)

    column, operator, raw_value = match.groups()

    if column not in df.columns:
        raise ColumnNotFoundError(column, list(df.columns))

    value = _cast_value(df[column], raw_value)

    try:
        mask = OPERATORS[operator](df[column], value)
    except TypeError:
        raise InvalidFilterExpressionError(
            expression + f" (type mismatch: column '{column}' is {df[column].dtype})"
        )

    result = df[mask]
    print(f" Filter '{expression}' -> {len(result)} rows matched (from {len(df)})")
    return result.reset_index(drop=True)

