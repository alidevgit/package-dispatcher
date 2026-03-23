# Package Dispatcher

A compact, production-leaning Python implementation of a package dispatch classifier.

It solves a simple rules problem, but the repo is intentionally structured like something worth shipping:

- small public API
- CLI entrypoint
- boundary-focused test suite
- CI-ready layout

## Problem

Given `width`, `height`, `length` in centimeters and `mass` in kilograms, classify a package into one of three stacks:

- `STANDARD`: not bulky and not heavy
- `SPECIAL`: bulky or heavy, but not both
- `REJECTED`: both bulky and heavy

Rules:

- Bulky if volume is greater than or equal to `1_000_000 cm^3`
- Bulky if any dimension is greater than or equal to `150 cm`
- Heavy if mass is greater than or equal to `20 kg`

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
python -m package_dispatcher 100 100 100 10
```

Example output:

```text
REJECTED
```

## CLI Usage

```bash
python -m package_dispatcher <width> <height> <length> <mass>
```

Example:

```bash
python -m package_dispatcher 50 40 30 10
python -m package_dispatcher 150 40 30 10
python -m package_dispatcher 100 100 100 20
```

## API Usage

```python
from package_dispatcher import sort

stack = sort(50, 40, 30, 10)
print(stack)  # STANDARD
```

## Design Notes

- The challenge asks for a `sort(width, height, length, mass)` function, so that API is exposed directly.
- Input validation is explicit: negative values are rejected with `ValueError`.
- The logic is separated into a small domain model to keep the classification easy to test and extend.

## Repository Layout

```text
.
├── .github/workflows/ci.yml
├── pyproject.toml
├── README.md
├── src/package_dispatcher
│   ├── __init__.py
│   ├── __main__.py
│   └── sorter.py
└── tests/test_sorter.py
```

## Running Tests

```bash
pytest
```

Or, if you prefer a single-command workflow:

```bash
make install
make test
make run
```
