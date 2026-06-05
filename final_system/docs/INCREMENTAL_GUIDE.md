# Guía incremental — registro por fase

> Una nota breve al cerrar cada fase. El bot en **raíz** no debe regresar hasta validar.

## Fase 0 — Análisis ✅

- Inventario completo del bot en raíz.
- Mapa de credenciales legacy → `final_system/.env`.
- Diagramas flujo cliente + admin.
- **Sin código** en `final_system/`.

## Fase 1 — Scaffold ✅

**Hecho:**

- Árbol `final_system/` según prompt maestro.
- `config/settings.py`, `bot_config.py`, `intents.py`, `prompts.py`, `sheets_config.py` (con GUÍA RÁPIDA).
- `.env.example` con todas las variables del mapa Fase 0.
- `.env` con valores **copiados** del bot en raíz (Twilio, Admin, Sheets, cachés, JWT desde `SECRET_KEY`).
- `credentials/google-service-account.json` copiado desde raíz.
- `docs/ARCHITECTURE.md`, `INCREMENTAL_GUIDE.md` (este archivo).
- `requirements.txt`, `.gitignore`, `README.md`.
- `whatsbot_app/README.md` — placeholder Fase 9.
- Stubs en `api/`, `services/`, `models/`, `infrastructure/`, `scripts/`, `tests/`, `chatbot/`.

**No hecho (intencional):**

- Copiar chatbot / `gateway.py` → Fase 2.
- FastAPI webhook operativo → Fase 4.
- PostgreSQL migraciones → Fase 5.
- Flutter UI → Fase 9.

**Validación:** el bot en raíz (`python run.py`) sigue sin cambios.

**Variables migradas (nombres):** ver lista en `README.md` sección “Variables migradas”.

---

## Fase 2 — Gateway ✅

- [x] Copiar `app/` → `final_system/chatbot/app/` (raíz intacta)
- [x] `chatbot/gateway.py` → `handle_incoming_message()` (misma lógica que `POST /bot`)
- [x] `business_id` opcional en payload (passthrough)
- [x] `chatbot/runtime.py` — singleton servicios
- [x] `scripts/validate_chatbot.py`
- [x] Rutas `DATA_DIR` / `FLOWS_PATH` apuntan a `final_system/` y repo raíz

**Validar:** `python scripts/validate_chatbot.py` desde `final_system/`.

---

## Fase 3 — Config ✅

- [x] Secrets y URLs solo en `final_system/.env` (sin sobrescribir valores Fase 1)
- [x] `config/settings.py` — Twilio, admin, JWT, paths, API
- [x] `config/sheets_config.py` — Sheets TTL, credenciales (alias legacy)
- [x] `config/bot_config.py` — FLOWS_PATH, NAV_HINT, branding
- [x] `config/intents.py` — GLOBAL_COMMAND_INTENTS + GREETING_PHRASES (parser legacy)
- [x] `config/prompts.py` — 21 textos desde `flows/restaurant_flow.json` + gateway
- [x] `chatbot/app/config.py` — shim hacia `config/*`
- [x] `validate_chatbot.py` → 0 fallos

---

## Fase 4 — API webhook (pendiente)

- [ ] FastAPI + `whatsapp.py` → gateway

---

## Fases 5–10

Ver `PROMPT_EVOLUCION_SAAS_WHATSBOT.md` sección 9.
