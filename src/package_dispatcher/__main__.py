from __future__ import annotations

import argparse
from typing import Sequence

from package_dispatcher import sort


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="package-dispatch",
        description="Classify a package into STANDARD, SPECIAL, or REJECTED.",
    )
    parser.add_argument("width", type=float, help="Package width in centimeters")
    parser.add_argument("height", type=float, help="Package height in centimeters")
    parser.add_argument("length", type=float, help="Package length in centimeters")
    parser.add_argument("mass", type=float, help="Package mass in kilograms")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    print(sort(args.width, args.height, args.length, args.mass))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
