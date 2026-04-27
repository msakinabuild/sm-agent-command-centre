"""
log-exchange.py
Single job: append a formatted exchange record to the client comms log.
Usage:
  python log-exchange.py --direction inbound --sender "HR Consultancy" --date 2026-04-15 --body "Message text here"
  python log-exchange.py --direction sent --sender "Sakina" --date 2026-04-15 --body "Reply text here"
"""

import argparse
import os
import sys
from datetime import date

LOG_PATH = os.path.join(
    os.path.dirname(__file__),
    "..", "live", "hr-consultant-automation", "comms-log.md"
)


def build_entry(direction: str, sender: str, entry_date: str, body: str) -> str:
    label = "INBOUND" if direction == "inbound" else "SENT"
    return f"\n---\n\n**[{label}] — {entry_date}**\n**From:** {sender}\n\n{body.strip()}\n"


def append_entry(log_path: str, entry: str) -> None:
    abs_path = os.path.abspath(log_path)
    if not os.path.exists(abs_path):
        print(f"ERROR: Comms log not found at {abs_path}", file=sys.stderr)
        print("Do not proceed without a log — create it first.", file=sys.stderr)
        sys.exit(1)
    with open(abs_path, "a", encoding="utf-8") as f:
        f.write(entry)


def main():
    parser = argparse.ArgumentParser(description="Append an exchange to the client comms log.")
    parser.add_argument("--direction", required=True, choices=["inbound", "sent"],
                        help="Direction of the message: inbound (from client) or sent (by Sakina)")
    parser.add_argument("--sender", required=True,
                        help='Who sent the message, e.g. "HR Consultancy" or "Sakina"')
    parser.add_argument("--date", default=str(date.today()),
                        help="ISO date of the message (YYYY-MM-DD). Defaults to today.")
    parser.add_argument("--body", required=True,
                        help="The full message text to log")
    args = parser.parse_args()

    entry = build_entry(args.direction, args.sender, args.date, args.body)
    append_entry(LOG_PATH, entry)
    print(f"Logged [{args.direction.upper()}] from {args.sender} on {args.date}.")


if __name__ == "__main__":
    main()
