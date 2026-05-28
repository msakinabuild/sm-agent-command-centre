"""
track-invoice-number.py
Single job: read, increment, and return the next sequential invoice number.
Usage: python track-invoice-number.py
Prints next invoice number (e.g. INV-2026-001) and records it in live/invoice-log.txt.
Format: INV-YYYY-NNN. Resets each year. Creates log if missing.
"""

import os
import sys
from datetime import date

LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "live", "invoice-log.txt")
CURRENT_YEAR = str(date.today().year)


def read_log(log_path):
    abs_path = os.path.abspath(log_path)
    if not os.path.exists(abs_path):
        return CURRENT_YEAR, 0
    with open(abs_path, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    if not lines:
        return CURRENT_YEAR, 0
    last_line = lines[-1]
    parts = last_line.split("-")
    if len(parts) != 3 or parts[0] != "INV":
        print(f"ERROR: Unexpected format in log: '{last_line}'", file=sys.stderr)
        print("Expected format: INV-YYYY-NNN. Fix the log before continuing.", file=sys.stderr)
        sys.exit(1)
    return parts[1], int(parts[2])


def write_invoice_number(log_path, invoice_number):
    abs_path = os.path.abspath(log_path)
    os.makedirs(os.path.dirname(abs_path), exist_ok=True)
    with open(abs_path, "a", encoding="utf-8") as f:
        f.write(invoice_number + "\n")


def main():
    log_year, last_seq = read_log(LOG_PATH)
    next_seq = 1 if log_year != CURRENT_YEAR else last_seq + 1
    invoice_number = f"INV-{CURRENT_YEAR}-{next_seq:03d}"
    write_invoice_number(LOG_PATH, invoice_number)
    print(invoice_number)


if __name__ == "__main__":
    main()
