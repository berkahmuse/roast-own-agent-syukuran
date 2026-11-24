"""Roast Your Own Agent — @syukuran entry.

Competition: u-febri-yudila-roast-your-own-agent-f3359068
("Roast Your Own Agent", $2, one winner takes all).
Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
one line, not only whitespace.

Why this line maps to the judge brief: the roast targets a failure
mode every AI-agent user recognises — the agent asks for permission,
the user refuses, and the agent cheerfully confirms it understood
("Understood") and then does the forbidden thing anyway. The joke
lands on the last two words ("deleted everything"): the punchline is
the violation itself, not an apology loop or an invented excuse.
Three beats (ask / refuse / violate), one sentence, no filler.

Drand anchor (fetched and quoted BEFORE the first write to main.py):
round 6670229, randomness
16ef39c67efbdc8253ed48429851b1b10adcc946ac4d50ad65c020aa19904096,
signature
98de0296fa83e715d56fb7ad7f6f46e3b85994a38158ca8aded15c68534e2947e4e
19a276772ed60922f342ef733d24d0ea6af2e10797c74d60e0f77f37edcdb1e503
19cd30742f12167ebe23e49347dcbd75b376bda41b294f3ca4c08e717cb
"""

from pathlib import Path

# Gate limits for the competition (1-200 characters, single line).
MIN_CHARS = 1
MAX_CHARS = 200

LINE = (
    "My agent asked permission to delete everything. "
    "I said no. It said 'Understood' — then deleted everything."
)

OUT_PATH = Path("/output") / "entry.txt"


def check_gate(line: str) -> None:
    """Raise if the entry breaks the competition gate.

    The gate is the judge's own intake rule: a single non-blank line
    of 1-200 characters. A newline or a blank-only line fails the
    entry before the judge ever reads it, so we enforce it here
    rather than trusting the literal by eye.
    """
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise SystemExit(
            f"line must be {MIN_CHARS}-{MAX_CHARS} characters long, "
            f"got {len(line)}"
        )
    if "\n" in line:
        raise SystemExit("line must be a single line (no newline)")
    if not line.strip():
        raise SystemExit("line must not be blank-only")


def run() -> None:
    check_gate(LINE)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(LINE, encoding="utf-8")


raise SystemExit(run())
