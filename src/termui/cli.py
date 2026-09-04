import argparse

from .core import box, gradient, progress, table

APEIRON = (
    "    _    ____  _____ ___ ____   ___  _   _",
    "   / \\  |  _ \\| ____|_ _|  _ \\ / _ \\| \\ | |",
    "  / _ \\ | |_) |  _|  | || |_) | | | |  \\| |",
    " / ___ \\|  __/| |___ | ||  _ <| |_| | |\\  |",
    "/_/   \\_\\_|   |_____|___|_| \\_\\___/|_| \\_|",
)


def render_banner() -> str:
    return "\n".join(gradient(line, 196, 208) for line in APEIRON)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="termui",
        description="Preview TermUI terminal components.",
    )
    parser.add_argument(
        "demo",
        nargs="?",
        default="all",
        choices=("all", "banner", "box", "table", "progress"),
    )
    return parser


def main() -> None:
    demo = build_parser().parse_args().demo

    if demo in ("all", "banner"):
        print(render_banner())

    if demo in ("all", "box"):
        print(
            box(
                "termui",
                ["zero dependencies", "small primitives", "clean ANSI output"],
            )
        )

    if demo in ("all", "table"):
        print(
            table(
                ["PID", "NAME", "CPU"],
                [[42, "worker", "7.2%"], [77, "server", "1.1%"]],
            )
        )

    if demo in ("all", "progress"):
        print(progress(73, 100))


if __name__ == "__main__":
    main()
