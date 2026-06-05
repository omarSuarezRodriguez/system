"""Create database tables (Fase 4)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from infrastructure.database import init_db  # noqa: E402


def main() -> int:
    init_db()
    print("Tables created/verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
