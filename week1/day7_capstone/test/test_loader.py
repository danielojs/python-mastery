# test_loader.py - test CSV loading and validation

import sys; sys.path.insert(0, '..')
import pytest
import pandas as pd
import tempfile
import os
from loader import load_csv
from exceptions import FileNotFoundError, InvalidCSVEror


@pytest.fixture
def valid_csv(tmp_path):
    """Create a temporary valid CSV file."""
    f = tmp_path / "test.csv"
    f.write_text("name,age,city\nAlice,30,Jakarta\nBob,25,Bandung\n")
    return str(f)

@pytest.fixture
def empty_csv(tmp_path):
    f = tmp_path / "empty.csv"
    f.write_text("")
    return str(f)

@pytest.fixture
def headers_only_csv(tmp_path):
    f = tmp_path / "headers.csv"
    f.write_text("name,age,city\n")
    return str(f)


def test_load_valid_csv(valid_csv):
    df = load_csv(valid_csv)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert list(df.columns) == ["name", "age", "city"]

def test_load_returns_correct_values(valid_csv):
    df = load_csv(valid_csv)
    assert df.iloc[0]["name"] == "Alice"
    assert df.iloc[1]["age"] == 25

def test_file_not_found_raises():
    with pytest.raises(FileNotFoundError) as exc_info:
        load_csv("ghost_file.csv")
    assert "ghost_file.csv" in str(exc_info.value)

def test_empty_file_raises(empty_csv):
    with pytest.raises(InvalidCSVEror):
        load_csv(empty_csv)

def test_headers_only_raises(headers_only_csv):
    with pytest.raises(InvalidCSVEror):
        load_csv(headers_only_csv)

