# main.py - CLI entry point. Wires everything together.

import argparse
import sys
from loader import load_csv, display_summary
from filters import apply_filter
from sorter import sort_data
from exporter import export_csv
from logger import save_run_log
from exceptions import CSVToolError


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="csv_tool",
        description="CSV Too - filter, sort and export CSV files from the command line.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "file",
        help="Path to the input CSV file"
    )
    parser.add_argument(
        "--filter",
        dest="filter_expr",
        metavar="EXPR",
        help='Filter rows by expression. Examples:\n --filter "age>25"\n --filter "city=Jakarta"'
    )
    parser.add_argument(
        "--sort",
        dest="sort_col",
        metavar="COLUMN",
        help="Column name to sort by"
    )
    parser.add_argument(
        "--desc",
        action="store_true",
        help="Sort in descending order (use with --sort)"
    )
    parser.add_argument(
        "--export",
        dest="export_path",
        metavar="OUTPUT",
        help="Export results to a new CSV file"
    )
    parser.add_argument(
        "--log",
        dest="log_path",
        metavar="LOG",
        default="run_log.json",
        help="Path for the JSON run log (default: run_log.json)"
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    run_meta = {
        "input_file": args.file,
        "filter": args.filter_expr,
        "sort": args.sort_col,
        "descending": args.desc,
        "export": args.export_path,
    }

    try:
        print(f"\n Loading '{args.file}'...")
        df = load_csv(args.file)
        display_summary(df)

        run_meta["rows_loaded"] = len(df)

        if args.filter_expr:
            print(" Applying filter...")
            df = apply_filter(df, args.filter_expr)
            run_meta["rows_after_filter"] = len(df)

        if args.sort_col:
            print(" Sorting...")
            df = sort_data(df, args.sort_col, descending=args.desc)

        if args.export_path:
            print(" Exporting...")
            export_csv(df, args.export_path)
            run_meta["rows_exported"] = len(df)
        else:
            print("\n Result Preview (first 10 rows):")
            print(df.head(10).to_string(index=False))

        run_meta["status"] = "success"

    except CSVToolError as e:
        print(f"\n Error: {e}", file=sys.stderr)
        run_meta["status"] = "error"
        run_meta["error"] = str(e)
        sys.exit(1)

    finally:
        save_run_log(run_meta, args.log_path)

    print("\n Done.\n")


if __name__ == "__main__":
    main()

