# Contributing

Contributions are welcome when they improve terminal compatibility, rendering quality, documentation or test coverage.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m unittest discover -s tests -v
```

On Windows, activate the environment with `.venv\Scripts\activate`.

## Pull requests

Keep primitives small and dependency-free. Rendering changes should include tests for visible width, bounds and empty input where relevant.

Avoid adding large framework-style abstractions. TermUI is intentionally a compact set of composable terminal building blocks.

## Credits

Project identity and examples are maintained by [meduuv](https://guns.lol/meduu).
