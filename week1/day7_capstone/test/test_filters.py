# test_filters.py - test all filter operator, edge cases, and error paths

import sys; sys.path.insert(0, '...')
import pytest
import pandas as pd
from filters import apply_filter
from exceptions import InvalidFilterExpressionError, ColumnNotFoundError


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie", "Diana"],
        "age": [32, 24, 45, 28],
        "city": ["Jakarta", "Bandung", "Jakarta", "Surabaya"],
        "salary": [8500.0, 4200.0, 12000.0, 6700.0]
    })


# Numeric operator
def test_gt(sample_df):
    result = apply_filter(sample_df, "age>28")
    assert len(result) == 2
    assert set(result["name"]) == {"Alice", "Charlie"}



def test_lt(sample_df):
    result = apply_filter(sample_df, "age<30")
    assert len(result) == 2
    assert set(result["name"]) == {"Bob", "Diana"}



