"""Make the Judge Laugh in One Line — entry program.

Writes a single funny line to the grader's output path.
Standard library only; no third-party imports. The joke lands on the
last clause: the judge laughs at the defendant's claim and ends up
sentencing himself, which is the whole punchline.
"""

import os
import sys

LINE = "I told the judge I was innocent, and he laughed so hard he held himself in contempt of court."

DEFAULT_OUTPUT = "/output/entry.txt"


def main(argv):
    output = argv[1] if len(argv) > 1 else DEFAULT_OUTPUT
    directory = os.path.dirname(output)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    # The grader reads this file as a different user, so make it
    # world-readable explicitly instead of relying on the umask.
    os.chmod(output, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
