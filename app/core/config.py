import json
import os
import secrets
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DEFAULT_NAVIGATION = [
    {"endpoint": "site.home", "label": "Inicio"},
    {"endpoint": "site.services", "label": "Servicios"},
    {"endpoint": "site.parts", "label": "Repuestos"},
    {"endpoint": "site.about", "label": "Nosotros"},
]

DEFAULT_PAGE_META = {
    "home": {
        "title_template": "{site_name} | Taller mecánico moderno",
        "description_template": "Taller mecánico moderno con navegación rápida, servicios, repuestos y contacto por WhatsApp.",
    },
    "services": {
        "title_template": "Servicios | {site_name}",
        "description_template": "Servicios de mantención, frenos, suspensión, diagnóstico y atención a flotas.",
    },
    "service_detail": {
        "title_template": "{service_title} | {site_name}",
        "description_template": "{service_description}",
    },
    "parts": {
        "title_template": "Repuestos | {site_name}",
        "description_template": "Consulta de repuestos para frenos, mantención y suspensión con atención por WhatsApp.",
    },
    "about": {
        "title_template": "Nosotros | {site_name}",
        "description_template": "Conoce el taller, su propuesta de valor y la infraestructura digital preparada para crecer.",
    },
}

DEFAULT_SITE_COPY = {
    "brand_mark": "ML",
    "brand_subtitle": "Taller mecánico",
    "nav_cta_label": "Agenda tu cita",
    "nav_cta_message": "Hola, quiero agendar una revisión.",
    "whatsapp_float_label": "WhatsApp",
    "whatsapp_float_aria_label": "Contactar por WhatsApp",
    "whatsapp_float_message": "Hola, quiero cotizar un servicio para mi vehículo.",
    "footer_tagline": "Taller mecánico moderno, rápido y confiable.",
    "footer_credit": "Desarrollado por MonaySolutions. Todos los derechos reservados.",
    "service_link_label": "Ver más",
    "parts_cta_label": "Consultar stock",
    "gallery_modal_close_label": "Cerrar",
    "gallery_modal_close_aria_label": "Cerrar imagen",
}

DEFAULT_SERVICE_CATALOG = [
    {
        "slug": "mantencion-preventiva",
        "title": "Mantención preventiva",
        "description": "Cambio de aceite, filtros, revisión de niveles y chequeo general para mantener el vehículo en condiciones óptimas.",
        "image": "/static/img/services/maintenance.jpg",
        "hero_title": "Mantención preventiva para cuidar rendimiento, seguridad y vida útil del vehículo.",
        "detail_intro": "La mantención preventiva permite anticiparse al desgaste natural del vehículo y evitar fallas mayores. Es una de las intervenciones más importantes para conservar rendimiento, consumo y seguridad.",
        "includes": [
            "Cambio de aceite y filtro según especificación del fabricante",
            "Revisión de filtro de aire, filtro de cabina y niveles generales",
            "Inspección visual de correas, fugas, batería y sistema de carga",
            "Chequeo de frenos, neumáticos y elementos de desgaste rápido",
        ],
        "applies_to": [
            "Vehículos con kilometraje de servicio próximo",
            "Autos que han estado detenidos por largos periodos",
            "Clientes que buscan prevenir fallas costosas",
        ],
        "common_signs": [
            "Aceite vencido o de color muy oscuro",
            "Pérdida de rendimiento o aumento de consumo",
            "Ruido mecánico mayor al habitual",
        ],
        "whatsapp_message": "Hola, les hablo desde el sitio web y quiero solicitar una cotización correspondiente al servicio de mantención preventiva para mi vehículo. Quedo atento a su información.",
    },
    {
        "slug": "frenos-suspension",
        "title": "Frenos y suspensión",
        "description": "Revisión y reparación de pastillas, discos, amortiguadores, bandejas, terminales y otros componentes críticos.",
        "image": "/static/img/services/brakes-suspension.jpg",
        "hero_title": "Frenos y suspensión con enfoque en seguridad, control y confort de manejo.",
        "detail_intro": "Trabajamos el sistema de frenado y suspensión como un conjunto clave para la seguridad. Una inspección correcta permite detectar desgaste, holguras y componentes comprometidos antes de que afecten la conducción.",
        "includes": [
            "Diagnóstico de pastillas, discos, cálipers y líquido de frenos",
            "Revisión de amortiguadores, cazoletas, bandejas y terminales",
            "Detección de vibraciones, ruidos y desgaste irregular",
            "Recomendación de reemplazos según estado real del sistema",
        ],
        "applies_to": [
            "Vehículos con ruidos al frenar o al pasar irregularidades",
            "Autos con vibraciones en volante o pérdida de estabilidad",
            "Clientes que buscan revisión preventiva antes de viaje",
        ],
        "common_signs": [
            "Chirridos o golpeteos en frenado o suspensión",
            "Vehículo cargado hacia un lado",
            "Mayor distancia de frenado",
        ],
        "whatsapp_message": "Hola, les hablo desde el sitio web y quiero solicitar una cotización correspondiente al servicio de frenos y suspensión para mi vehículo. Quedo atento a su información.",
    },
    {
        "slug": "escaner-diagnostico",
        "title": "Escáner y diagnóstico",
        "description": "Lectura de fallas, análisis técnico y orientación clara para detectar el origen del problema antes de reparar.",
        "image": "/static/img/services/diagnostic.jpg",
        "hero_title": "Diagnóstico electrónico y evaluación técnica para decisiones más precisas.",
        "detail_intro": "No se trata solo de leer códigos. Un buen diagnóstico combina escáner, inspección visual y criterio técnico para identificar la causa de la falla y no solo su síntoma.",
        "includes": [
            "Lectura de códigos y parámetros del sistema",
            "Interpretación técnica de fallas activas o históricas",
            "Revisión de comportamiento del vehículo y componentes asociados",
            "Orientación sobre reparación, prioridad y próximos pasos",
        ],
        "applies_to": [
            "Vehículos con luces de advertencia encendidas",
            "Fallos intermitentes de motor, encendido o sensores",
            "Clientes que necesitan diagnóstico antes de autorizar reparaciones",
        ],
        "common_signs": [
            "Check engine encendido",
            "Fallas de potencia o tirones",
            "Consumo anormal o ralentí inestable",
        ],
        "whatsapp_message": "Hola, les hablo desde el sitio web y quiero solicitar una cotización correspondiente al servicio de escáner y diagnóstico para mi vehículo. Quedo atento a su información.",
    },
    {
        "slug": "embrague-transmision",
        "title": "Embrague y transmisión",
        "description": "Inspección, ajuste y reemplazo de componentes de embrague y transmisión para una conducción segura y estable.",
        "image": "/static/img/services/clutch-transmission.jpg",
        "hero_title": "Servicio de embrague y transmisión orientado a respuesta, tracción y continuidad operativa.",
        "detail_intro": "Los problemas de embrague o transmisión suelen escalar rápido si no se revisan a tiempo. Evaluamos el sistema completo para definir si corresponde ajuste, reparación o reemplazo.",
        "includes": [
            "Inspección de kit de embrague, prensa, disco y collarín",
            "Revisión de pérdidas, soportes y comportamiento de caja",
            "Evaluación de vibraciones, patinamiento y dificultad de paso",
            "Definición técnica del alcance real de la intervención",
        ],
        "applies_to": [
            "Vehículos con dificultad al pasar cambios",
            "Autos con patinamiento o vibración al salir",
            "Transmisiones con ruidos anormales o pérdida de respuesta",
        ],
        "common_signs": [
            "Pedal de embrague duro o irregular",
            "Cambios que no entran con normalidad",
            "Olor a embrague o pérdida de fuerza",
        ],
        "whatsapp_message": "Hola, les hablo desde el sitio web y quiero solicitar una cotización correspondiente al servicio de embrague y transmisión para mi vehículo. Quedo atento a su información.",
    },
    {
        "slug": "aire-acondicionado",
        "title": "Aire acondicionado",
        "description": "Diagnóstico, carga de gas, revisión de fugas y mantención del sistema de climatización del vehículo.",
        "image": "/static/img/services/air-conditioning.jpg",
        "hero_title": "Aire acondicionado automotriz con revisión completa del sistema y control de fugas.",
        "detail_intro": "El sistema de climatización necesita más que una simple recarga. Revisamos presión, funcionamiento y posibles fugas para asegurar un servicio duradero y no una solución temporal.",
        "includes": [
            "Verificación de presión y rendimiento del sistema",
            "Revisión de fugas y estado de conexiones",
            "Carga de gas según condición del equipo",
            "Chequeo general de funcionamiento y respuesta del climatizador",
        ],
        "applies_to": [
            "Vehículos que enfrían poco o dejaron de enfriar",
            "Sistemas con olor extraño o funcionamiento irregular",
            "Clientes que buscan mantención preventiva antes de temporada alta",
        ],
        "common_signs": [
            "Bajo rendimiento de enfriamiento",
            "Ruidos al activar el aire",
            "Diferencia térmica insuficiente en cabina",
        ],
        "whatsapp_message": "Hola, les hablo desde el sitio web y quiero solicitar una cotización correspondiente al servicio de aire acondicionado automotriz para mi vehículo. Quedo atento a su información.",
    },
    {
        "slug": "atencion-flotas",
        "title": "Atención a flotas",
        "description": "Gestión de mantenciones periódicas y soporte técnico para vehículos de trabajo, empresas y operaciones comerciales.",
        "image": "/static/img/services/fleet-service.jpg",
        "hero_title": "Atención técnica para flotas con foco en continuidad operativa y planificación.",
        "detail_intro": "Cuando una flota se detiene, el negocio lo siente. Ordenamos mantenciones, diagnósticos y prioridades para reducir tiempos muertos y mantener los vehículos operativos.",
        "includes": [
            "Planificación de mantenciones por kilometraje o uso",
            "Revisión de unidades con prioridad operativa",
            "Seguimiento de observaciones técnicas y trabajos recomendados",
            "Atención pensada para empresas y vehículos de trabajo",
        ],
        "applies_to": [
            "Empresas con vehículos utilitarios o comerciales",
            "Flotas que requieren orden y continuidad operativa",
            "Clientes que necesitan soporte técnico recurrente",
        ],
        "common_signs": [
            "Atraso en mantenciones periódicas",
            "Unidades fuera de servicio por falta de control preventivo",
            "Desorden en prioridades de reparación",
        ],
        "whatsapp_message": "Hola, les hablo desde el sitio web y quiero solicitar una cotización correspondiente al servicio de atención y mantención de flotas. Quedo atento a su información.",
    },
]

DEFAULT_SITE_CONTENT = {
    "hero": {
        "eyebrow": "Diagnóstico, mantención y repuestos",
        "title": "Tu vehículo en manos técnicas, rápidas y confiables.",
        "description": "Atención profesional para autos particulares y flotas. Revisamos, cotizamos y coordinamos tu servicio con una experiencia simple y actual.",
        # "highlights": [
        #     "Diagnóstico con escáner",
        #     "Garantía en trabajos seleccionados",
        #     "Seguimiento por WhatsApp",
        # ],
        "primary_cta_label": "Cotizar ahora",
        "primary_cta_message": "Hola, quiero cotizar una reparación.",
        "secondary_cta_label": "Ver servicios",
    },
    "trust_points": [
        {
            "title": "Diagnóstico claro",
            "description": "Explicamos el problema antes de ejecutar cualquier trabajo.",
        },
        {
            "title": "Repuestos confiables",
            "description": "Trabajamos con marcas reconocidas y alternativas según presupuesto.",
        },
        {
            "title": "Entrega ordenada",
            "description": "Coordinamos tiempos, avances y retiro sin fricción.",
        },
    ],
    "home_sections": {
        "services": {
            "eyebrow": "Servicios",
            "title": "Servicios mecánicos para diagnóstico, mantención y reparación automotriz.",
            "description": "Cobertura técnica en mantención preventiva, frenos, suspensión, escáner, transmisión, climatización y atención a flotas.",
            "cta_label": "Ver todos los servicios",
        },
        "brands": {
            "eyebrow": "Marcas que trabajamos",
            "title": "Atención multimarca para autos, SUV y vehículos de trabajo.",
        },
        "parts": {
            "eyebrow": "Repuestos",
            "title": "Consulta repuestos esenciales con contacto directo y respuesta rápida.",
            "description": "Frenos, mantención y suspensión con atención orientada a stock, compatibilidad y soporte técnico.",
        },
        "gallery": {
            "eyebrow": "Galería multimedia",
            "title": "Taller, diagnósticos y trabajos en ejecución.",
            "description": "Instalaciones, procesos técnicos y trabajos reales presentados en un carrusel visual más limpio y más actual.",
            "controls_aria_label": "Controles de galería",
            "prev_aria_label": "Anterior",
            "next_aria_label": "Siguiente",
        },
        "map": {
            "eyebrow": "Ubicación y reseñas",
            "title": "Ubicación visible, presencia local y acceso directo a la ficha pública en Google Maps.",
            "summary_rating_label": "Calificación visible en Google Maps:",
            "primary_cta": "Ver ubicación y reseñas",
            "card_aria_label": "Abrir ubicación y reseñas del taller en Google Maps",
            "card_badge": "Ver reseñas reales",
            "preview_meta": "San Bernardo · Taller mecánico",
            "preview_summary": "Abrir en Google Maps para ver ubicación, reseñas, fotos y cómo llegar.",
            "review_stars": "★★★★★",
            "maps_pill_label": "Google Maps",
        },
    },
    "parts": [
        {
            "title": "Frenos",
            "description": "Pastillas, discos, kits y sensores para múltiples marcas.",
            "image": "/static/img/gallery/brakes.jpg",
            "whatsapp_message": "Hola, quiero consultar por repuestos de frenos.",
        },
        {
            "title": "Mantención",
            "description": "Filtros, lubricantes, bujías y kits de servicio.",
            "image": "/static/img/gallery/reception.jpg",
            "whatsapp_message": "Hola, quiero consultar por repuestos de mantención.",
        },
        {
            "title": "Suspensión",
            "description": "Amortiguadores, cazoletas, terminales y bandejas.",
            "image": "/static/img/gallery/diagnostic.jpg",
            "whatsapp_message": "Hola, quiero consultar por repuestos de suspensión.",
        },
    ],
    "gallery": [
        {"title": "Diagnóstico electrónico", "image": "/static/img/gallery/diagnostic.jpg"},
        {"title": "Mantención general", "image": "/static/img/hero.jpg"},
        {"title": "Revisión de frenos", "image": "/static/img/gallery/brakes.jpg"},
        {"title": "Recepción y entrega", "image": "/static/img/gallery/reception.jpg"},
        {"title": "Asesoría técnica", "image": "/static/img/services/services-hero.jpg"},
        {"title": "Atención de flotas", "image": "/static/img/services/fleet-service.jpg"},
    ],
    "brands": [
        {"name": "Hyundai", "image": "/static/img/brands/hyundai.svg"},
        {"name": "Chevrolet", "image": "/static/img/brands/chevrolet.svg"},
        {"name": "Nissan", "image": "/static/img/brands/nissan.svg"},
        {"name": "Peugeot", "image": "/static/img/brands/peugeot.svg"},
    ],
    "google_place": {
        "name": "Garage MASB",
        "rating": "5.0",
        "address": "Aguamarina 1821, San Bernardo, Región Metropolitana",
        "phone": "+56 9 6489 0613",
        "maps_url": "https://www.google.com/maps/place/Garage+MASB/@-33.6122605,-70.7407522,14z/data=!4m10!1m2!2m1!1staller+mecanico+san+bernardo!3m6!1s0x9662d9dfbe8b299f:0xd608f74cd28538f9!8m2!3d-33.6122657!4d-70.7026397!15sChx0YWxsZXIgbWVjYW5pY28gc2FuIGJlcm5hcmRvWh4iHHRhbGxlciBtZWNhbmljbyBzYW4gYmVybmFyZG-SAQhtZWNoYW5pY5oBRENpOURRVWxSUVVOdlpFTm9kSGxqUmpsdlQycENNMXB0YkVOVE1EQTBaV3BDUlZGdWNIRmxSVVpzWW0xYWVrMUZSUkFC4AEA-gEECAAQIA!16s%2Fg%2F11h6crqlg6?entry=ttu&g_ep=EgoyMDI2MDYyMS4wIKXMDSoASAFQAw%3D%3D",
    },
    "google_review_cards": [
        {
            "title": "Calificación 5.0 en Google Maps",
            "summary": "Consulta la ficha pública, la valoración general y la presencia del taller en Google.",
            "cta": "Ver en Google Maps",
        },
        {
            "title": "Opiniones, fotos y ubicación",
            "summary": "Accede a la reseña pública del negocio, revisa fotografías y obtén cómo llegar.",
            "cta": "Abrir ficha",
        },
        {
            "title": "Presencia local en San Bernardo",
            "summary": "Consulta la ficha pública del negocio, su ubicación y la información visible para clientes en Google Maps.",
            "cta": "Explorar ficha",
        },
    ],
    "video": {
        "title": "Conoce cómo trabajamos en el taller",
        "description": "Una sección de video ayuda mucho a transmitir orden, limpieza, equipamiento y confianza antes de que el cliente escriba.",
        "poster": "/static/img/hero.jpg",
        "label": "Espacio listo para video del taller",
    },
    "services_page": {
        "eyebrow": "Servicios",
        "title": "Atención mecánica especializada para diagnóstico, mantención y reparación.",
        "description": "Soluciones técnicas para vehículos particulares, SUV y flotas, con enfoque en seguridad, rendimiento y continuidad operativa.",
    },
    "parts_page": {
        "eyebrow": "Repuestos",
        "title": "Venta asistida de repuestos con respuesta rápida por WhatsApp.",
        "description": "La sección está preparada para evolucionar más adelante hacia un inventario o ecommerce sin rehacer la vista.",
    },
    "about_page": {
        "hero": {
            "eyebrow": "Nosotros",
            "title": "Respaldo técnico para tu vehículo",
            "description": "Somos un taller automotriz multimarca orientado a seguridad, continuidad operativa y atención profesional, con una propuesta pensada para responder con rapidez y criterio técnico en cada servicio.",
        },
        "intro_title": "Soporte técnico para mantener cada unidad en ruta.",
        "intro_paragraphs": [
            "En Pablete entendemos que la movilidad y la seguridad del vehículo impactan directamente en la operación diaria de cada cliente. Por eso trabajamos con una atención técnica orientada a reducir tiempos muertos, ordenar diagnósticos y mantener cada unidad en condiciones confiables de funcionamiento.",
            "Contamos con infraestructura de taller, experiencia en diagnóstico avanzado y un equipo preparado para intervenir sistemas críticos con criterio, precisión y seguimiento. Desde mantenciones preventivas hasta revisión de frenos, suspensión, transmisión y escáner, abordamos cada servicio con foco en rendimiento, seguridad y continuidad operativa.",
            "Para clientes particulares, empresas y flotas, desarrollamos una atención cercana y organizada, con seguimiento técnico claro, respuesta rápida y una relación de trabajo pensada para dar respaldo real en el día a día.",
        ],
        "check_list": [
            "Atención multimarca para autos, SUV y vehículos de trabajo",
            "Diagnóstico técnico con enfoque preventivo y correctivo",
            "Seguimiento ordenado para clientes particulares y empresas",
            "Soporte orientado a continuidad operativa de flotas",
        ],
        "team_image": "/static/img/about/team-pablete.png",
        "team_alt": "Equipo técnico de Pablete en taller mecánico",
        "team_caption": "Equipo técnico preparado para atención multimarca y soporte operativo.",
        "capabilities": {
            "eyebrow": "Capacidades",
            "title": "Servicio orientado a diagnóstico técnico preciso y tiempos de atención confiables.",
            "cards": [
                {
                    "title": "Diagnóstico avanzado",
                    "description": "Revisión técnica de sistemas críticos con apoyo de escáner, inspección mecánica y análisis orientado a la causa real del problema.",
                },
                {
                    "title": "Mantención y reparación",
                    "description": "Intervenciones preventivas y correctivas para proteger seguridad, rendimiento y vida útil del vehículo en uso diario o comercial.",
                },
                {
                    "title": "Atención a empresas y flotas",
                    "description": "Seguimiento técnico ordenado, prioridad operativa y una relación de trabajo pensada para clientes que necesitan continuidad y respuesta.",
                },
            ],
        },
        "commitment": {
            "eyebrow": "Compromiso",
            "title": "Trabajamos para que cada cliente tenga claridad, respaldo y continuidad operativa.",
            "quotes": [
                "Priorizamos diagnósticos claros, decisiones técnicas bien fundamentadas y una atención que permita avanzar con confianza.",
                "Entendemos que cada vehículo detenido afecta tiempo, operación y productividad; por eso respondemos con orden y seguimiento.",
                "Pablete busca convertirse en el soporte técnico que permita a cada cliente enfocarse en su operación mientras el taller resuelve.",
            ],
        },
    },
    "service_detail_page": {
        "eyebrow": "Servicio especializado",
        "cta_label": "Cotiza con nosotros",
        "back_label": "Volver a servicios",
        "includes_title": "Qué incluye",
        "applies_title": "Cuándo aplica",
        "signs_title": "Señales frecuentes",
    },
}


def _get_env(name: str, default: str = "") -> str:
    return os.getenv(name, default).strip()


def _get_bool_env(name: str, default: bool) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


def _get_int_env(name: str, default: int) -> int:
    raw = os.getenv(name)
    if raw is None or not raw.strip():
        return default
    return int(raw.strip())


def _clone(value):
    return json.loads(json.dumps(value))


def _load_json_payload(raw_value: str, source_name: str):
    try:
        return json.loads(raw_value)
    except json.JSONDecodeError as exc:
        raise ValueError(f"No se pudo interpretar JSON desde {source_name}: {exc}") from exc


def _get_json_env(name: str, default):
    raw_value = os.getenv(name)
    if raw_value is None or not raw_value.strip():
        return _clone(default)
    return _load_json_payload(raw_value, name)


def _get_json_file_env(name: str, default):
    raw_path = _get_env(name)
    if not raw_path:
        return _clone(default)
    path = Path(raw_path)
    if not path.is_absolute():
        path = PROJECT_ROOT / raw_path
    return _load_json_payload(path.read_text(encoding="utf-8"), name)


def _get_structured_env(json_env_name: str, file_env_name: str, default):
    raw_json = os.getenv(json_env_name)
    if raw_json is not None and raw_json.strip():
        return _get_json_env(json_env_name, default)
    raw_file = _get_env(file_env_name)
    if raw_file:
        return _get_json_file_env(file_env_name, default)
    return _clone(default)


def _get_allowed_origins() -> tuple[str, ...]:
    raw_value = _get_env("ALLOWED_ORIGINS", "http://127.0.0.1:5000,http://localhost:5000")
    origins = [origin.strip().rstrip("/") for origin in raw_value.split(",") if origin.strip()]
    return tuple(dict.fromkeys(origins))


class BaseConfig:
    ENV_NAME = _get_env("APP_ENV", "development").lower()
    SECRET_KEY = _get_env("SECRET_KEY", secrets.token_urlsafe(32))
    DEBUG = ENV_NAME == "development"
    TESTING = False
    MAX_CONTENT_LENGTH = _get_int_env("MAX_CONTENT_LENGTH", 16 * 1024)
    SESSION_COOKIE_HTTPONLY = _get_bool_env("SESSION_COOKIE_HTTPONLY", True)
    SESSION_COOKIE_SAMESITE = _get_env("SESSION_COOKIE_SAMESITE", "Lax")
    SESSION_COOKIE_SECURE = _get_bool_env("SESSION_COOKIE_SECURE", ENV_NAME == "production")
    PREFERRED_URL_SCHEME = _get_env("PREFERRED_URL_SCHEME", "https")
    SITE_NAME = _get_env("SITE_NAME", "MotorLab")
    CONTACT_EMAIL = _get_env("CONTACT_EMAIL", "contacto@motorlab.cl")
    CONTACT_PHONE = _get_env("CONTACT_PHONE", "+56 9 4979 0992")
    WHATSAPP_NUMBER = _get_env("WHATSAPP_NUMBER", "56949790992")
    ADDRESS = _get_env("ADDRESS", "Av. Principal 1234, Santiago")
    BUSINESS_HOURS = _get_env("BUSINESS_HOURS", "Lun-Vie 08:30-18:30 | Sáb 09:00-14:00")
    HOST = _get_env("HOST", "127.0.0.1")
    PORT = _get_int_env("PORT", 5000)
    GOOGLE_PLACES_API_KEY = _get_env("GOOGLE_PLACES_API_KEY")
    GOOGLE_PLACE_QUERY = _get_env("GOOGLE_PLACE_QUERY", "Garage MASB Aguamarina 1821 San Bernardo")
    GOOGLE_PLACE_ID = _get_env("GOOGLE_PLACE_ID")
    GOOGLE_PLACE_URL = _get_env(
        "GOOGLE_PLACE_URL",
        "https://www.google.com/maps/place/Garage+MASB/@-33.6122605,-70.7407522,14z/data=!4m10!1m2!2m1!1staller+mecanico+san+bernardo!3m6!1s0x9662d9dfbe8b299f:0xd608f74cd28538f9!8m2!3d-33.6122657!4d-70.7026397!15sChx0YWxsZXIgbWVjYW5pY28gc2FuIGJlcm5hcmRvWh4iHHRhbGxlciBtZWNhbmljbyBzYW4gYmVybmFyZG-SAQhtZWNoYW5pY5oBRENpOURRVWxSUVVOdlpFTm9kSGxqUmpsdlQycENNMXB0YkVOVE1EQTBaV3BDUlZGdWNIRmxSVVpzWW0xYWVrMUZSUkFC4AEA-gEECAAQIA!16s%2Fg%2F11h6crqlg6?entry=ttu&g_ep=EgoyMDI2MDYyMS4wIKXMDSoASAFQAw%3D%3D",
    )
    GOOGLE_API_USER_AGENT = _get_env("GOOGLE_API_USER_AGENT", "MotorLab/1.0")
    ALLOWED_ORIGINS = _get_allowed_origins()
    NAVIGATION = _get_structured_env("NAVIGATION_JSON", "NAVIGATION_FILE", DEFAULT_NAVIGATION)
    PAGE_META = _get_structured_env("PAGE_META_JSON", "PAGE_META_FILE", DEFAULT_PAGE_META)
    SITE_COPY = _get_structured_env("SITE_COPY_JSON", "SITE_COPY_FILE", DEFAULT_SITE_COPY)
    SERVICE_CATALOG = _get_structured_env("SERVICE_CATALOG_JSON", "SERVICE_CATALOG_FILE", DEFAULT_SERVICE_CATALOG)
    SITE_CONTENT = _get_structured_env("SITE_CONTENT_JSON", "SITE_CONTENT_FILE", DEFAULT_SITE_CONTENT)


class ProductionConfig(BaseConfig):
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


def get_config():
    if _get_env("APP_ENV", "development").lower() == "production":
        return ProductionConfig
    return DevelopmentConfig
