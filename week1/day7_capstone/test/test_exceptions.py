# test_exceptions.py - verify al exceptions carry the right attributes and messages

import sys; sys.path.insert(0, '..')
import pytest
from exceptions import *


def test_base_is_exception():
    assert issubclass(CSVToolError, Exception)

def test_file_not_found_message():
    e = FileNotFoundError("data.csv")
    assert "data.csv" in str(e)
    assert e.filepath == "data.csv"

def test_invalid_csv_no_reason():
    e = InvalidCSVEror("bad.csv")
    assert "bad.csv" in str(e)

def test_invalid_csv_with_reason():
    e = InvalidCSVEror("bad.csv", "file is empty")
    assert "file is empty" in str(e)

def test_invalid_filter_expression():
    e = InvalidFilterExpressionError("age??25")
    assert "age??25" in str(e)
    assert e.expression == "age??25"

def test_column_not_found():
    e = ColumnNotFoundError("missing_col", ["name", "age", "city"])
    assert "missing_col" in str(e)
    assert "name" in str(e)
    assert e.column == "missing_col"
    assert e.available == ["name", "age", "city"]

def test_export_with_reason():
    e = ExportError("out.csv", "permission denied")
    assert "out.csv" in str(e)
    assert "permission denied" in str(e)

def test_log_write_error():
    e = LogWriteError("run_log.json", "disk full")
    assert "run_log.json" in str(e)
    assert "disk full" in str(e)

def test_all_inherit_from_base():
    for cls in [FileNotFoundError, InvalidCSVEror, InvalidFilterExpressionError,
                ColumnNotFoundError, ExportError, LogWriteError]:
        assert issubclass(cls, CSVToolError)

