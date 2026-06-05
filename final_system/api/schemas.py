"""Pydantic schemas for REST API (Fase 5)."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class BusinessOut(BaseModel):
    id: str
    name: str
    twilio_whatsapp_from: str
    admin_whatsapp_number: str
    google_spreadsheet_id: str | None
    sheets_enabled: bool
    is_default: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class BusinessCreate(BaseModel):
    id: str = Field(..., min_length=1, max_length=64)
    name: str
    twilio_whatsapp_from: str
    admin_whatsapp_number: str = ""
    google_spreadsheet_id: str | None = None
    sheets_enabled: bool = False
    is_default: bool = False


class MenuItemOut(BaseModel):
    id: int
    business_id: str
    external_id: str
    nombre: str
    precio: float
    categoria: str
    disponible: bool

    model_config = {"from_attributes": True}


class MenuItemCreate(BaseModel):
    nombre: str
    precio: float
    categoria: str = ""
    external_id: str = ""
    disponible: bool = True


class MenuItemUpdate(BaseModel):
    nombre: str | None = None
    precio: float | None = None
    categoria: str | None = None
    external_id: str | None = None
    disponible: bool | None = None


class MenuReplace(BaseModel):
    items: list[dict[str, Any]]


class OrderOut(BaseModel):
    id: int
    business_id: str
    order_id: str
    wa_id: str
    items: list[dict[str, Any]]
    total: float
    status: str
    customer_name: str
    address: str
    delivery_type: str
    created_at: datetime

    model_config = {"from_attributes": True}


class OrderCreate(BaseModel):
    order_id: str
    wa_id: str
    items: list[dict[str, Any]] = Field(default_factory=list)
    total: float = 0
    status: str = "pending"
    customer_name: str = ""
    address: str = ""
    delivery_type: str = ""
