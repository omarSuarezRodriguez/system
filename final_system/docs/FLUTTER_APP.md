# App Flutter WhatsBot (borrador Fase 7)

Backend JSON listo en Fase 7; UI Flutter en **Fase 9**.

## Conexión

| Concepto | Valor |
|----------|--------|
| Proyecto | `final_system/whatsbot_app/` |
| URL base | `API_PUBLIC_URL` en `final_system/.env` → `lib/config/api_config.dart` |
| Auth | `POST /auth/login` → JWT Bearer en todas las rutas `/whatsbot/*` |

## Login

```http
POST /auth/login
Content-Type: application/json

{"business_id": "default", "pin": "<WHATSBOT_OWNER_PIN>"}
```

Respuesta: `access_token`, `business_id`, `business_name`.

Header en llamadas siguientes: `Authorization: Bearer <access_token>`.

## Rutas consumidas por la app

| Método | Ruta | Uso en app |
|--------|------|------------|
| GET | `/whatsbot/conversations` | Lista de chats |
| GET | `/whatsbot/conversations/{id}/messages` | Pantalla chat |
| POST | `/whatsbot/messages` | Dueño envía texto al cliente |
| GET | `/whatsbot/orders/pending` | Bandeja pedidos |
| POST | `/whatsbot/orders/{id}/approve` | Aprobar |
| POST | `/whatsbot/orders/{id}/reject` | Rechazar |
| GET | `/whatsbot/business/me` | Perfil negocio |
| GET/PUT | `/whatsbot/business/menu` | Editor menú |
| GET/PUT | `/whatsbot/business/intents` | Editor intents |
| GET/PUT | `/whatsbot/business/prompts` | Editor textos bot |

## Compilar (Fase 9)

```bash
cd final_system/whatsbot_app
flutter pub get
flutter analyze
flutter run
```

No incluir `TWILIO_AUTH_TOKEN` ni secrets en la app; solo URL pública y JWT.
