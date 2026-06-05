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

## Backend (cuando esté listo — Fase 4+)

```bash
cd final_system
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
# Configurar PostgreSQL y DATABASE_URL en .env
python -m api.main
```

Webhook Twilio: `{API_PUBLIC_URL}/webhook` (ruta final en Fase 4; legacy sigue en `/bot` en raíz).

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
