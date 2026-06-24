from typing import Optional

from flask import current_app


def get_services_data() -> list[dict]:
    return [
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


def get_service_by_slug(slug: str) -> Optional[dict]:
    return next((service for service in get_services_data() if service["slug"] == slug), None)


def build_site_content() -> dict:
    whatsapp_number = current_app.config["WHATSAPP_NUMBER"]
    phone = current_app.config["CONTACT_PHONE"]
    email = current_app.config["CONTACT_EMAIL"]
    address = current_app.config["ADDRESS"]
    business_hours = current_app.config["BUSINESS_HOURS"]
    site_name = current_app.config["SITE_NAME"]

    return {
        "site_name": site_name,
        "contact": {
            "whatsapp_number": whatsapp_number,
            "phone": phone,
            "email": email,
            "address": address,
            "business_hours": business_hours,
        },
        "hero": {
            "eyebrow": "Diagnóstico, mantención y repuestos",
            "title": "Tu vehículo en manos técnicas, rápidas y confiables.",
            "description": (
                "Atención profesional para autos particulares y flotas. "
                "Revisamos, cotizamos y coordinamos tu servicio con una experiencia simple y actual."
            ),
            "highlights": [
                "Diagnóstico con escáner",
                "Garantía en trabajos seleccionados",
                "Seguimiento por WhatsApp",
            ],
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
        "services": get_services_data(),
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
            {
                "title": "Diagnóstico electrónico",
                "image": "/static/img/gallery/diagnostic.jpg",
            },
            {
                "title": "Mantención general",
                "image": "/static/img/hero.jpg",
            },
            {
                "title": "Revisión de frenos",
                "image": "/static/img/gallery/brakes.jpg",
            },
            {
                "title": "Recepción y entrega",
                "image": "/static/img/gallery/reception.jpg",
            },
            {
                "title": "Asesoría técnica",
                "image": "/static/img/services/services-hero.jpg",
            },
            {
                "title": "Atención de flotas",
                "image": "/static/img/services/fleet-service.jpg",
            },
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
            "description": (
                "Una sección de video ayuda mucho a transmitir orden, limpieza, "
                "equipamiento y confianza antes de que el cliente escriba."
            ),
            "poster": "/static/img/hero.jpg",
            "label": "Espacio listo para video del taller",
        },
        "features": [
            "Diseño responsive para celular y escritorio",
            "Secciones claras para servicios, repuestos y confianza comercial",
            "Botones directos de cotización por WhatsApp",
            "Base ordenada para crecer sin rehacer todo",
        ],
        "business_details": [
            ("Lunes a viernes", "08:30 a 18:30"),
            ("Sábado", "09:00 a 14:00"),
            ("Ubicación", address),
            ("Atención", "Particulares, empresas y flotas"),
        ],
        "testimonials": [
            "Me explicaron el diagnóstico, enviaron la cotización rápido y el auto quedó listo en el tiempo prometido.",
            "Se nota orden en la atención. Ideal para flotas y mantenciones programadas.",
            "La web deja claro qué hacen y el botón de WhatsApp resuelve todo en segundos.",
        ],
    }
