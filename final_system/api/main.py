"""
FastAPI application entry (Fase 4).

Arranque:
  cd final_system
  python -m api.main

Webhook Twilio:
  POST {API_PUBLIC_URL}/webhook  (alias: /bot)
"""

from __future__ import annotations

import logging
import sys
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# final_system on path
_FS = Path(__file__).resolve().parent.parent
if str(_FS) not in sys.path:
    sys.path.insert(0, str(_FS))

from api.routes import whatsapp  # noqa: E402
from config.settings import (  # noqa: E402
    API_PUBLIC_URL,
    CORS_ORIGINS,
    DEBUG,
    HOST,
    PORT,
    RESTAURANT_NAME,
)
from infrastructure.database import init_db  # noqa: E402

logging.basicConfig(
    level=logging.DEBUG if DEBUG else logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    logger.info("WhatsBot API started — %s", API_PUBLIC_URL)
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title="WhatsBot API",
        description="Backend JSON + webhook Twilio (sin UI web)",
        version="0.4.0",
        lifespan=lifespan,
    )

    origins = [o.strip() for o in CORS_ORIGINS.split(",") if o.strip()]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins if origins != ["*"] else ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(whatsapp.router)

    @app.get("/health")
    async def health():
        return {
            "status": "ok",
            "service": "whatsbot-api",
            "restaurant": RESTAURANT_NAME,
            "api_public_url": API_PUBLIC_URL,
        }

    return app


app = create_app()


def main() -> None:
    import uvicorn

    uvicorn.run(
        "api.main:app",
        host=HOST,
        port=PORT,
        reload=DEBUG,
    )


if __name__ == "__main__":
    main()
