#!/usr/bin/env python3
"""Serve this repository to local browser and Typora embeds."""

from __future__ import annotations

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PORT = 8765


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Serve Interview Learning Lab on this computer only."
    )
    parser.add_argument(
        "--port",
        type=int,
        default=DEFAULT_PORT,
        help=f"HTTP port (default: {DEFAULT_PORT})",
    )
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error("--port must be between 1 and 65535")
    return args


def main() -> None:
    args = parse_args()
    handler = partial(
        SimpleHTTPRequestHandler,
        directory=str(PROJECT_ROOT),
    )

    try:
        server = ThreadingHTTPServer(("127.0.0.1", args.port), handler)
    except OSError as error:
        raise SystemExit(
            f"Cannot start local server at 127.0.0.1:{args.port}: {error}"
        ) from None

    print(f"Serving repository: {PROJECT_ROOT}")
    print(
        "Quiz: "
        f"http://127.0.0.1:{args.port}/apps/hot100-binary-tree-quiz/index.html"
    )
    print("Keep this terminal open while using the pages; press Ctrl-C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nLocal server stopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
