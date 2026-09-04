from __future__ import annotations

import re
import shutil
from collections.abc import Iterable, Sequence

RESET = "\x1b[0m"
ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")


def visible_len(text: str) -> int:
    """Return the printable width of text after stripping ANSI color codes."""
    return len(ANSI_RE.sub("", text))


def color(text: str, code: int) -> str:
    """Wrap text in a 256-color foreground escape sequence."""
    if not 0 <= code <= 255:
        raise ValueError("color code must be between 0 and 255")
    return f"\x1b[38;5;{code}m{text}{RESET}"


def gradient(text: str, start: int = 196, end: int = 208) -> str:
    """Apply a character-by-character ANSI color gradient."""
    if not text:
        return ""
    if not 0 <= start <= 255 or not 0 <= end <= 255:
        raise ValueError("gradient colors must be between 0 and 255")

    last = max(1, len(text) - 1)
    pieces = []
    for index, char in enumerate(text):
        code = round(start + (end - start) * index / last)
        pieces.append(color(char, code))
    return "".join(pieces)


def box(title: str, lines: Sequence[str], width: int | None = None) -> str:
    """Render a compact Unicode box with a title and body lines."""
    content_width = max(
        [visible_len(title), *(visible_len(line) for line in lines)],
        default=0,
    )
    terminal_width = shutil.get_terminal_size((100, 20)).columns
    requested = width if width is not None else content_width + 4
    actual_width = max(6, min(requested, terminal_width))
    inner = actual_width - 2

    output = ["┌" + "─" * inner + "┐"]
    heading = f" {title} "
    output.append("│" + heading[:inner].ljust(inner) + "│")
    output.append("├" + "─" * inner + "┤")

    body_width = max(0, inner - 2)
    for line in lines:
        plain = ANSI_RE.sub("", line)
        output.append("│ " + plain[:body_width].ljust(body_width) + " │")

    output.append("└" + "─" * inner + "┘")
    return "\n".join(output)


def table(headers: Sequence[str], rows: Iterable[Sequence[object]]) -> str:
    """Render a simple left-aligned table."""
    headers = [str(value) for value in headers]
    rows = [[str(value) for value in row] for row in rows]
    if not headers:
        return ""

    widths = []
    for index, header in enumerate(headers):
        cells = [row[index] for row in rows if index < len(row)]
        widths.append(max([len(header), *(len(cell) for cell in cells)]))

    def render_row(row: Sequence[str]) -> str:
        return "  ".join(
            (row[index] if index < len(row) else "").ljust(widths[index])
            for index in range(len(headers))
        )

    separator = "  ".join("─" * width for width in widths)
    return "\n".join(
        [render_row(headers), separator, *(render_row(row) for row in rows)]
    )


def progress(value: float, total: float, width: int = 30) -> str:
    """Render a bounded progress bar and percentage."""
    if width < 1:
        raise ValueError("width must be at least 1")
    ratio = 0.0 if total <= 0 else max(0.0, min(1.0, value / total))
    filled = round(width * ratio)
    return "[" + "█" * filled + "░" * (width - filled) + f"] {ratio * 100:5.1f}%"
