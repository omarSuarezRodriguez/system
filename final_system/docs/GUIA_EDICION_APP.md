# Guía edición desde la app (borrador Fase 7)

El dueño configura su negocio **solo desde WhatsBot (Flutter)**. No debe editar `config/*.py` ni archivos del servidor.

## Qué puede editar el dueño

| Pantalla (Fase 9) | API | Efecto |
|-------------------|-----|--------|
| Menú | `PUT /whatsbot/business/menu` | Productos en BD; el bot los usa al atender clientes |
| Intents | `PUT /whatsbot/business/intents` | Frases/comandos globales (menu, pedido, …) por negocio |
| Mensajes del bot | `PUT /whatsbot/business/prompts` | Textos de bienvenida, errores, flujos de pedido/reserva |

Tras guardar, el próximo mensaje WhatsApp del cliente usa la configuración de **su** `business_id`.

## Flujo recomendado

1. Iniciar sesión con `business_id` y PIN (`WHATSBOT_OWNER_PIN` en servidor).
2. Revisar **Ajustes → Mi negocio** (`GET /whatsbot/business/me`).
3. Editar menú: agregar productos, precios y categorías.
4. Ajustar mensajes del bot si el tono o instrucciones deben cambiar.
5. (Opcional) Afinar intents si los clientes usan frases distintas a las por defecto.

## Chats y pedidos

- **Chats:** historial en BD desde el webhook; el dueño responde con `POST /whatsbot/messages`.
- **Pedidos:** lista `GET /whatsbot/orders/pending`; aprobar/rechazar notifica al cliente por Twilio.

## Lo que no hace la app

- No hay panel web (HTML/React).
- No se sustituye la confirmación legacy por `ADMIN_WHATSAPP_NUMBER` (sigue disponible).

Pantallas visuales y tutorial paso a paso: **Fase 9** (`whatsbot_app/`).
