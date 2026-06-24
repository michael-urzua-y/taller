import os
import secrets
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


def _get_env(name: str, default: str = "") -> str:
    return os.getenv(name, default).strip()


def _get_allowed_origins() -> tuple[str, ...]:
    raw_value = _get_env("ALLOWED_ORIGINS", "http://127.0.0.1:5000,http://localhost:5000")
    origins = [origin.strip().rstrip("/") for origin in raw_value.split(",") if origin.strip()]
    return tuple(dict.fromkeys(origins))


@dataclass(frozen=True)
class BaseConfig:
    SECRET_KEY: str = _get_env("SECRET_KEY", secrets.token_urlsafe(32))
    ENV_NAME: str = _get_env("APP_ENV", "development")
    DEBUG: bool = ENV_NAME == "development"
    TESTING: bool = False
    MAX_CONTENT_LENGTH: int = 16 * 1024
    SESSION_COOKIE_HTTPONLY: bool = True
    SESSION_COOKIE_SAMESITE: str = "Lax"
    SESSION_COOKIE_SECURE: bool = ENV_NAME == "production"
    PREFERRED_URL_SCHEME: str = "https"
    SITE_NAME: str = _get_env("SITE_NAME", "MotorLab")
    CONTACT_EMAIL: str = _get_env("CONTACT_EMAIL", "contacto@motorlab.cl")
    CONTACT_PHONE: str = _get_env("CONTACT_PHONE", "+56 9 4979 0992")
    WHATSAPP_NUMBER: str = _get_env("WHATSAPP_NUMBER", "56949790992")
    ADDRESS: str = _get_env("ADDRESS", "Av. Principal 1234, Santiago")
    BUSINESS_HOURS: str = _get_env(
        "BUSINESS_HOURS",
        "Lun-Vie 08:30-18:30 | Sáb 09:00-14:00",
    )
    GOOGLE_PLACES_API_KEY: str = _get_env("GOOGLE_PLACES_API_KEY")
    GOOGLE_PLACE_QUERY: str = _get_env("GOOGLE_PLACE_QUERY", "Garage MASB Aguamarina 1821 San Bernardo")
    GOOGLE_PLACE_ID: str = _get_env("GOOGLE_PLACE_ID")
    GOOGLE_PLACE_URL: str = _get_env(
        "GOOGLE_PLACE_URL",
        "https://www.google.com/maps/place/Garage+MASB/@-33.6122605,-70.7407522,14z/data=!4m10!1m2!2m1!1staller+mecanico+san+bernardo!3m6!1s0x9662d9dfbe8b299f:0xd608f74cd28538f9!8m2!3d-33.6122657!4d-70.7026397!15sChx0YWxsZXIgbWVjYW5pY28gc2FuIGJlcm5hcmRvWh4iHHRhbGxlciBtZWNhbmljbyBzYW4gYmVybmFyZG-SAQhtZWNoYW5pY5oBRENpOURRVWxSUVVOdlpFTm9kSGxqUmpsdlQycENNMXB0YkVOVE1EQTBaV3BDUlZGdWNIRmxSVVpzWW0xYWVrMUZSUkFC4AEA-gEECAAQIA!16s%2Fg%2F11h6crqlg6?entry=ttu&g_ep=EgoyMDI2MDYyMS4wIKXMDSoASAFQAw%3D%3D",
    )
    ALLOWED_ORIGINS: tuple[str, ...] = _get_allowed_origins()


class ProductionConfig(BaseConfig):
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


def get_config():
    if _get_env("APP_ENV", "development").lower() == "production":
        return ProductionConfig
    return DevelopmentConfig
