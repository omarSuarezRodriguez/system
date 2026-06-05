"""Global prompt/text defaults — seed from legacy restaurant_flow.json."""

from __future__ import annotations

# Claves alineadas con nodos del flujo; el dueño sobrescribe por negocio en BD.
DEFAULT_PROMPTS: dict[str, str] = {
    "welcome_secondary": (
        "¿Qué te gustaría hacer hoy?\n\n"
        "1. *menu* — Ver el menú\n"
        "2. *pedido* — Hacer tu pedido\n"
        "3. *reservar* — Reservar mesa"
    ),
    "cancel_message": (
        "Entendido, cancelé el proceso actual. "
        "Estoy aquí cuando quieras continuar."
    ),
    "order_start": (
        "Perfecto, vamos con tu pedido.\n\n"
        "Cuéntame qué te gustaría en lenguaje natural."
    ),
    "order_saved_pending": (
        "Gracias por tu confianza. Tu pedido fue registrado y está "
        "*pendiente* de confirmación del restaurante."
    ),
    "admin_unrecognized": (
        "Comando admin no reconocido.\n"
        "Pedidos: *CONFIRMAR ORD-XXXXXXXX* o *pedido ORD-XXXXXXXX listo*"
    ),
    "error_generic": (
        "Disculpa, tuve un inconveniente momentáneo. "
        "Por favor intenta de nuevo en unos segundos.\n\n"
        "Escribe *inicio* para reiniciar."
    ),
    "empty_body_hint": (
        "Estoy aquí para ayudarte. Escribe *menu*, *pedido* o *reservar*."
    ),
}


def get_prompt(key: str, fallback: str = "") -> str:
    return DEFAULT_PROMPTS.get(key, fallback)


# -----------------------------------------------------------------------------
# GUÍA RÁPIDA
# - Entrada: textos por defecto para negocios nuevos (copiados de flows/*.json).
# - Salida: business_prompts en BD; gateway lee BD primero, luego este fallback.
# - Fase 9: pantalla Mensajes en Flutter → PUT /whatsbot/business/prompts.
# - No duplicar lógica de plantillas {{restaurant_name}} aquí; eso queda en flow engine.
# -----------------------------------------------------------------------------
