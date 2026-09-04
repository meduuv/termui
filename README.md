# TermUI

TermUI is a tiny collection of terminal interface primitives for Python. It keeps the API deliberately small and uses ANSI escape sequences directly, making it useful for CLIs that want polished output without pulling in a full UI framework.

## Included

* 256-color text
* Character gradients
* Unicode boxes
* Aligned tables
* Progress bars
* ANSI-aware visible-length calculation
* Zero runtime dependencies

## Install

```bash
git clone https://github.com/meduuv/termui.git
cd termui
pip install -e .
```

## Preview

```bash
termui
termui banner
termui table
termui progress
```

The built-in banner includes a red-to-orange `APEIRON` ASCII signature.

## Python API

```python
from termui import box, progress

print(box("status", ["service: online", "latency: 18 ms"]))
print(progress(73, 100))
```

## Development

```bash
python -m unittest discover -s tests -v
```

## Credits

Built by [meduuv](https://guns.lol/meduu).

## License

MIT
