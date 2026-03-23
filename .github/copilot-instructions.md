# GitHub Copilot Instructions

## Repository Context

This repository is a compact Python project centered on one core behavior: classifying a package into `STANDARD`, `SPECIAL`, or `REJECTED`.

Primary code locations:

- `src/package_dispatcher/sorter.py`
- `src/package_dispatcher/__main__.py`
- `tests/test_sorter.py`

## Coding Guidelines

- Keep the solution minimal, explicit, and easy to review.
- Preserve the required public API: `sort(width, height, length, mass)`.
- Prefer straightforward conditionals over unnecessary abstractions.
- Avoid adding dependencies unless they provide clear value.
- Use Python 3.11+ features only when they improve clarity.

## Domain Rules

Apply these rules exactly:

- A package is bulky when:
  - `width * height * length >= 1_000_000`, or
  - any single dimension is `>= 150`
- A package is heavy when:
  - `mass >= 20`

Dispatch outcomes:

- both bulky and heavy -> `REJECTED`
- either bulky or heavy -> `SPECIAL`
- neither -> `STANDARD`

## Testing Expectations

- Add or update tests for any logic change.
- Keep boundary coverage for threshold values.
- Validate negative inputs if touching input handling.

Run validation with:

```bash
pytest
```

## Editing Preferences

- Keep files ASCII unless a file already requires otherwise.
- Maintain concise docstrings and comments.
- Do not reformat unrelated code.
- Keep README examples synchronized with actual CLI behavior.