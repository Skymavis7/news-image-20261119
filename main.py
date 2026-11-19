"""Place the finished news image where the grader reads it.

The repository holds the finished image as entry.png: a newspaper front
page summing up Thursday 19 November 2026 world news. This program
copies that file, byte for byte, into the output directory the grader
reads. It uses only the Python standard library, touches no network,
and writes identical bytes on every run.
"""

from os import environ, makedirs
from pathlib import Path
from shutil import copyfile


def place_entry() -> None:
    # The image sits beside this file; the destination comes from
    # MAKEFUN_OUTPUT_DIR and falls back to /output. Create the target
    # directory first: the grader's /output may not exist yet on a
    # fresh sandbox, and the copy must not fail for that reason.
    image = Path(__file__).resolve().parent / "entry.png"
    target_dir = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    makedirs(target_dir, exist_ok=True)
    copyfile(image, target_dir / "entry.png")


if __name__ == "__main__":
    place_entry()
