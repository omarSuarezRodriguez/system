"""Bot session defaults — global fallbacks until business config lives in DB."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# Flow JSON (legacy path until chatbot is copied in Fase 2)
FLOWS_PATH = Path(
    os.getenv(
        "FLOWS_PATH",
        str(BASE_DIR.parent / "flows" / "restaurant_flow.json"),
    )
)

GLOBAL_COMMANDS = frozenset({"menu", "pedido", "reservar", "inicio", "cancelar"})

NAV_HINT = (
    "\n\n---\n"
    "Escribe *inicio* para volver al inicio\n"
)

# Navigation / UX flags (mirrors restaurant_flow.json meta)
NAVIGATION_HINT_ENABLED = True
CANCEL_MESSAGE_DEFAULT = (
    "Entendido, cancelé el proceso actual. Estoy aquí cuando quieras continuar."
)

# -----------------------------------------------------------------------------
# GUÍA RÁPIDA
# - Entrada: FLOWS_PATH apunta al JSON conversacional (hoy en raíz: flows/).
# - Salida: defaults para nuevos negocios al hacer onboard_business (Fase 5+).
# - El dueño edita flujo/textos desde Flutter → BD; este archivo NO es su panel.
# - Fase 2: copiar chatbot; Fase 3: mover hardcoded de app/config.py aquí.
# -----------------------------------------------------------------------------
