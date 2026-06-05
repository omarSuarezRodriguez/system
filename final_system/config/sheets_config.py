"""Google Sheets optional sync — migrated from legacy app/config.py."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

GOOGLE_SHEETS_ENABLED = os.getenv("GOOGLE_SHEETS_ENABLED", "false").strip().lower() in {
    "1",
    "true",
    "yes",
    "on",
}

# Legacy GOOGLE_SHEETS_CREDENTIALS_PATH → GOOGLE_SERVICE_ACCOUNT_JSON_PATH
GOOGLE_SERVICE_ACCOUNT_JSON_PATH = os.getenv(
    "GOOGLE_SERVICE_ACCOUNT_JSON_PATH",
    str(BASE_DIR / "credentials" / "google-service-account.json"),
)

# Inline JSON for cloud (Render/Railway); optional if file path exists
GOOGLE_SERVICE_ACCOUNT_JSON = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON", "").strip()

GOOGLE_SPREADSHEET_ID = os.getenv("GOOGLE_SPREADSHEET_ID", "")
GOOGLE_SHEET_ID_MENU = os.getenv(
    "GOOGLE_SHEET_ID_MENU",
    GOOGLE_SPREADSHEET_ID,
)
GOOGLE_SHEET_ID_ORDERS = os.getenv(
    "GOOGLE_SHEET_ID_ORDERS",
    GOOGLE_SPREADSHEET_ID,
)

MENU_CACHE_TTL_SECONDS = int(os.getenv("MENU_CACHE_TTL_SECONDS", "60"))
ORDERS_CACHE_TTL_SECONDS = int(os.getenv("ORDERS_CACHE_TTL_SECONDS", "30"))
BLOCKED_USERS_CACHE_TTL_SECONDS = int(
    os.getenv("BLOCKED_USERS_CACHE_TTL_SECONDS", "15")
)
SHEETS_INCREMENTAL_THRESHOLD = int(os.getenv("SHEETS_INCREMENTAL_THRESHOLD", "500"))
SHEETS_FULL_REFRESH_INTERVAL_SECONDS = int(
    os.getenv("SHEETS_FULL_REFRESH_INTERVAL_SECONDS", "3600")
)
SHEETS_INCREMENTAL_BATCH_SIZE = int(os.getenv("SHEETS_INCREMENTAL_BATCH_SIZE", "100"))


def credentials_path() -> Path:
    return Path(GOOGLE_SERVICE_ACCOUNT_JSON_PATH)


# -----------------------------------------------------------------------------
# GUÍA RÁPIDA
# - Entrada: .env + archivo credentials/google-service-account.json (copiado Fase 1).
# - Salida: parámetros para sheets_sync_service (Fase 8).
# - Fuente de verdad futura: PostgreSQL; Sheets = espejo si GOOGLE_SHEETS_ENABLED=true.
# - Un solo spreadsheet legacy usa la misma ID en MENU y ORDERS (pestañas distintas).
# -----------------------------------------------------------------------------
