#!/usr/bin/env python3
"""Post-process Platane/snk SVGs so the snake head grows as it eats contributions."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def grow_snake(svg_path: Path) -> None:
    content = svg_path.read_text(encoding="utf-8")

    duration_match = re.search(r"(\d+)ms linear infinite", content)
    duration = duration_match.group(1) if duration_match else "15900"

    grow_block = f"""
@keyframes snake-size {{
  0% {{ width: 10px; height: 10px; x: 2.6px; y: 2.6px; }}
  35% {{ width: 12px; height: 12px; x: 1.8px; y: 1.8px; }}
  65% {{ width: 15px; height: 15px; x: 0.9px; y: 0.9px; }}
  100% {{ width: 18px; height: 18px; x: 0px; y: 0px; }}
}}
.s.s0 {{
  animation: snake-size {duration}ms linear infinite, s0 {duration}ms linear infinite;
}}
"""

    if "snake-size" not in content:
        content = content.replace("</style>", grow_block + "</style>")

    svg_path.write_text(content, encoding="utf-8")
    print(f"grew  {svg_path}")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: grow_snake.py <svg> [svg...]", file=sys.stderr)
        return 1

    for arg in sys.argv[1:]:
        grow_snake(Path(arg))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
