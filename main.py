"""Entry for u-zeroxfive-funniest-autocorrect-fail-ddf82154.

Writes a single-line autocorrect fail to entry.txt in MAKEFUN_OUTPUT_DIR.
"""

import os


ENTRY = (
    "Texted my boss 'I'll be in the office by 9 for the client meeting' "
    "\u2014 autocorrect sent 'I'll be in the office by 9 for the client "
    "mating,' and HR has scheduled a follow-up at 10."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # One tight mechanism: "meeting" -> "mating" in a work text to the boss;
    # precise times (9, 10) ground it, and the turn lands in the final clause.
    text = ENTRY
    assert 1 <= len(text) <= 199, f"entry length {len(text)} out of gate"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
