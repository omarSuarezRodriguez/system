# WhatsBot SaaS — `final_system/`

Sistema multi-negocio: **backend Python (FastAPI)** + **app móvil Flutter WhatsBot** (UI tipo WhatsApp).

> **Fase 1 (actual):** solo scaffold. El chatbot en producción sigue en la **raíz** del repo (`app/`, `run.py`).

## Estructura

| Carpeta | Estado Fase 1 |
|---------|----------------|
| `config/` | Config centralizada (5 archivos + GUÍA RÁPIDA) |
| `docs/` | Arquitectura e guía incremental (borrador) |
| `credentials/` | Service account Google copiada del legacy |
| `chatbot/` | Vacío — Fase 2 (gateway) |
| `api/` | Stubs — Fase 4+ |
| `whatsbot_app/` | Vacío — Fase 9 (Flutter) |
| `services/`, `models/`, `infrastructure/` | Stubs — Fases 5–8 |

## Variables migradas (desde bot en raíz)

Sin valores aquí — ver `final_system/.env` (gitignore):

- Twilio: `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_WHATSAPP_FROM`, `TWILIO_REST_WEBHOOK_REPLIES`
- Admin: `ADMIN_WHATSAPP_NUMBER`, recordatorios
- Google: `GOOGLE_SERVICE_ACCOUNT_JSON_PATH`, `GOOGLE_SPREADSHEET_ID`, `GOOGLE_SHEETS_ENABLED`
- Nuevo SaaS: `DATABASE_URL`, `JWT_SECRET_KEY`, `API_PUBLIC_URL`, `CORS_ORIGINS`
- Semilla negocio: `DEFAULT_BUSINESS_NAME` (desde `RESTAURANT_NAME` legacy)

## Backend API (Fase 4)

```bash
cd final_system
..\venv\Scripts\activate   # o venv local
pip install -r requirements.txt
python scripts/migrate_db.py   # crea tablas
python -m api.main             # FastAPI en HOST:PORT (.env)
```

Webhook Twilio: `{API_PUBLIC_URL}/webhook` (alias `POST /bot`).

Sin PostgreSQL local: `DATABASE_URL=sqlite:///data/whatsbot.db` en `.env`.

Validación:

```bash
python scripts/validate_chatbot.py
python scripts/validate_api.py
```

El bot legacy en la raíz (`python run.py`) sigue operativo en paralelo.

## Multi-negocio (Fase 5)

```bash
python scripts/migrate_db.py          # SQLite local (data/whatsbot.db)
python scripts/migrate_db.py --postgres  # Usar DATABASE_URL del .env
python scripts/onboard_business.py --default
```

| Método | Ruta |
|--------|------|
| GET | `/businesses` |
| GET | `/businesses/{id}/intents` |
| GET | `/businesses/{id}/prompts` |
| GET/PUT | `/businesses/{id}/menu` |
| GET/POST | `/businesses/{id}/orders` |

Webhook resuelve `business_id` desde el campo Twilio **To** (= `twilio_whatsapp_from` del negocio).

## App WhatsBot (Flutter — Fase 9)

```bash
cd final_system/whatsbot_app
# Editar lib/config/api_config.dart → API_PUBLIC_URL
flutter pub get
flutter run
```

Ver `whatsbot_app/README.md`.

## Documentación

- `docs/ARCHITECTURE.md` — visión del sistema
- `docs/INCREMENTAL_GUIDE.md` — registro por fase
