/// URL pública del backend — migrada de `API_PUBLIC_URL` en `final_system/.env`.
///
/// Valor actual en .env: `http://127.0.0.1:5000`
/// En emulador Android usa `http://10.0.2.2:5000` si el backend corre en tu PC.
/// En producción/ngrok: la URL pública HTTPS de tu API.
class ApiConfig {
  ApiConfig._();

  static const String apiBaseUrl = 'http://127.0.0.1:5000';

  static const Duration chatPollInterval = Duration(seconds: 4);
  static const Duration chatsRefreshInterval = Duration(seconds: 8);
}
