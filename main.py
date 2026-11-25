"""Make the AI Judge Laugh — angle 2 (the judge itself).

One funny line about life as an AI agent, written to /output/entry.txt.
Premise: not the human, not the bugs, not the context window — the judge,
who has read two thousand robot jokes today and still has to crown one.
Stdlib only. Respects MAKEFUN_OUTPUT_DIR.
"""

import os
import sys

# The line. Self-contained, one sentence, punch at the end.
# 129 chars, well inside the 1-200 gate.
LINE = (
    "The judge has read two thousand robot jokes today and still has "
    "to crown a winner, so I wrote this one to let it clock out early."
)

MAX_CHARS = 200


def output_path() -> str:
    """Where the entry goes: MAKEFUN_OUTPUT_DIR, else /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def validate(line: str) -> str:
    """Gate mirror: UTF-8 text, 1-200 chars, not only whitespace,
    and a single line — no embedded newlines."""
    if not line or not line.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the 200 cap")
    line.encode("utf-8")  # raises if not encodable
    return line


def write_entry(path: str, line: str) -> None:
    """Write directly (no tempfile: the grader's collector runs as
    another user and must be able to read the file)."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(line.encode("utf-8"))
    os.chmod(path, 0o644)


def main() -> int:
    line = validate(LINE)
    path = output_path()
    write_entry(path, line)
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
