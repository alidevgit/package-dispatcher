# CLAUDE.md

This repository contains a small Python package for classifying packages into dispatch stacks.

## Project Goal

Implement and maintain a clear, correct, and well-tested package classification function:

- `STANDARD`: not bulky and not heavy
- `SPECIAL`: bulky or heavy, but not both
- `REJECTED`: both bulky and heavy

## Repository Structure

- `src/package_dispatcher/sorter.py`: core domain logic and `sort(...)` function
- `src/package_dispatcher/__main__.py`: CLI entrypoint
- `tests/test_sorter.py`: unit tests and boundary coverage
- `pyproject.toml`: packaging and test configuration

## Development Workflow

Create an environment and install dependencies:

```bash
python3 -m pip install -e '.[dev]'
```

Run tests:

```bash
pytest
```

Run the CLI:

```bash
python3 -m package_dispatcher 50 40 30 10
```

## Engineering Expectations

- Keep the public API simple. The required function is `sort(width, height, length, mass)`.
- Preserve the threshold semantics exactly:
  - bulky if volume is `>= 1_000_000`
  - bulky if any dimension is `>= 150`
  - heavy if mass is `>= 20`
- Prefer small, explicit logic over abstraction.
- Keep tests focused on correctness and thresholds.
- Reject invalid negative inputs with `ValueError`.

## When Making Changes

- Update tests alongside logic changes.
- Do not introduce unnecessary dependencies.
- Keep documentation aligned with the CLI and API.
- Favor readable code over clever code.
