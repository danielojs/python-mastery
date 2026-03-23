# exporter.py - Export filtered/sorted DataFrame to a new CSV file

import pandas as pd
from exceptions import ExportError


def export_csv(df: pd.DataFrame, output_path: str) -> None:
    """
    Write the DataFrame to a CSV file at output_path.
    Raises ExportError if writing fails.
    """
    try:
        df.to_csv(output_path, index=False)
        print(f"  Exported {len(df)} rows -> '{output_path}'")
    except PermissionError:
        raise ExportError(output_path, "permission denied")
    except OSError as e:
        raise ExportError(output_path, str(e))

