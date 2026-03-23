class CSVToolError(Exception):
    """Base exception for all csv_tool errors."""
    pass

class FileNotFoundError(CSVToolError):
    """Raised when the specified CSV file does not exist."""
    def __init__(self, filepath: str) -> None:
        super().__init__(f"File not found: '{filepath}'")
        self.filepath = filepath

class InvalidCSVEror(CSVToolError):
    """Raised when the file cannot be parsed as valid CSV."""
    def __init__(self, filepath: str, reason: str = "") -> None:
        msg = f"Invalid CSV file: '{filepath}'"
        if reason:
            msg += f" - {reason}"
        super().__init__(msg)

class InvalidFilterExpressionError(CSVToolError):
    """Raised when a --filter expression cannot be parsed."""
    def __init__(self, expression: str) -> None:
        super().__init__(
            f"Invalid filter expression: '{expression}'."
            f"Expected format: 'column>value', 'column<value', or 'column=value'"
        )
        self.expression = expression

class ColumnNotFoundError(CSVToolError):
    """Raised when a referenced column does not exist in the CSV."""
    def __init__(self, column: str, available: list) -> None:
        super().__init__(
            f"Column '{column}' not found. Available: {', '.join(available)}"
        )
        self.column = column
        self.available = available

class ExportError(CSVToolError):
    """Raised when exporting results to a file fails."""
    def __init__(self, path: str, reason: str = "") -> None:
        msg = f"Failed to export to '{path}'"
        if reason:
            msg += f": {reason}"
        super().__init__(msg)

class LogWriteError(CSVToolError):
    """Raised when writing the JSON run log fails."""
    def __init__(self, path: str, reason: str = "") -> None:
        msg = f"Failed to write log to '{path}'"
        if reason:
            msg += f": {reason}"
        super().__init__(msg)
