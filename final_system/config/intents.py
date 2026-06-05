"""Global intent defaults — seed for new businesses (dueño edita en app Flutter)."""

from __future__ import annotations

# Comandos exactos (legacy GLOBAL_COMMANDS + restaurant_flow.json meta.global_commands)
GLOBAL_COMMANDS: dict[str, str] = {
    "menu": "menu_node",
    "pedido": "order_start",
    "reservar": "reservation_start",
    "inicio": "start",
    "cancelar": "start",
}

# Subconjunto mínimo de frases NL (completo vive en chatbot/parser.py hasta Fase 2)
GLOBAL_COMMAND_INTENTS_SEED: dict[str, dict] = {
    "menu": {
        "tokens": ["menu", "menú", "carta", "catalogo", "catálogo"],
        "phrases": [
            "quiero ver el menu",
            "muestrame el menu",
            "opciones del menu",
        ],
    },
    "pedido": {
        "tokens": ["pedido", "ordenar", "orden"],
        "phrases": [
            "hacer pedido",
            "ordenar comida",
            "quiero ordenar",
        ],
    },
    "reservar": {
        "tokens": ["reservar", "reserva", "mesa"],
        "phrases": [
            "quiero reservar",
            "reservar mesa",
            "hacer una reserva",
        ],
    },
    "inicio": {
        "tokens": ["inicio", "empezar", "volver"],
        "phrases": ["volver al inicio", "empezar de nuevo"],
    },
    "cancelar": {
        "tokens": ["cancelar", "cancela"],
        "phrases": ["cancelar pedido", "cancelar todo"],
    },
}


def global_commands_frozenset() -> frozenset[str]:
    return frozenset(GLOBAL_COMMANDS.keys())


# -----------------------------------------------------------------------------
# GUÍA RÁPIDA
# - Entrada: semilla al crear negocio (onboard_business); copia a business_intents en BD.
# - Salida: fallback si el negocio no tiene intents personalizados en BD.
# - Fuente completa hoy: app/core/parser.py GLOBAL_COMMAND_INTENTS (Fase 2 copia).
# - Prohibido pedir al dueño editar este .py; usar pantalla Intents en Flutter.
# -----------------------------------------------------------------------------
