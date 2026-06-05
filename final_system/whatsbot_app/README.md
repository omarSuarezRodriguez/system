# App Flutter — se implementa en Fase 9

WhatsBot: UI móvil tipo WhatsApp para el dueño (Android/iOS). **No Flutter Web** como producto principal.

- Conectará a `API_PUBLIC_URL` del backend (`final_system/.env`).
- Sin `TWILIO_AUTH_TOKEN` en el cliente.
- Pantallas: login, chats, chat, pedidos, menú/intents/mensajes editables.

```bash
# Cuando exista pubspec.yaml (Fase 9):
cd final_system/whatsbot_app
flutter pub get
flutter run
```
