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
    {"endpoint": "site.parts", "label": "Repuestos / Productos"},
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
        "title_template": "Repuestos / Productos | {site_name}",
        "description_template": "Consulta de repuestos y productos para frenos, mantención y suspensión con atención por WhatsApp.",
    },
    "products": {
        "title_template": "Productos | {site_name}",
        "description_template": "Catálogo de productos: aceites, lubricantes y más para tu vehículo.",
    },
    "product_detail": {
        "title_template": "{product_name} | {site_name}",
        "description_template": "{product_description}",
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
        "image": "/static/img/services/maintenance.webp",
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
        "image": "/static/img/services/brakes-suspension.webp",
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
        "image": "/static/img/services/diagnostic.webp",
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
        "image": "/static/img/services/clutch-transmission.webp",
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
        "image": "/static/img/services/air-conditioning.webp",
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
        "image": "/static/img/services/fleet-service.webp",
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

DEFAULT_PRODUCT_CATALOG = [
    {
        "slug": "aceite-totalenergies-quartz-ineo-mc3-5w30-5l",
        "title": "Aceite de Motor TotalEnergies QUARTZ INEO MC3 5W-30 5 Litros",
        "short_description": "Aceite sintético 5W-30 para motores diésel y gasolina con filtro de partículas. Envase de 5 litros.",
        "image": "/static/img/products/aceite-ineo-mc3-5w30-5l.webp",
        "category": "Aceite de Motor",
        "brand": "TotalEnergies",
        "description": "QUARTZ INEO MC3 asegura el óptimo funcionamiento de los convertidores catalíticos de tres vías y los filtros de partículas. Además, contribuye a reducir las emisiones de NOx, CO2, CO y partículas, lo que garantiza el cumplimiento de los niveles de rendimiento exigidos por los fabricantes y las normas medioambientales EURO V. Gracias a su formulación avanzada, prolonga la vida útil de los sistemas de post-tratamiento, previniendo tanto la obstrucción como el llenado prematuro de los filtros de partículas y del convertidor catalítico de tres vías. Por otro lado, su excelente resistencia a las variaciones de temperatura asegura la longevidad de las partes del motor, manteniendo un nivel óptimo de rendimiento en todo tipo de condiciones. Asimismo, satisface los planes de servicio más exigentes de los fabricantes, permitiendo intervalos de cambio de aceite extra-largos sin comprometer la protección del motor.",
        "recommendations": [
            "Antes de utilizar el producto, consulta siempre la guía de mantenimiento del vehículo.",
            "Realiza los cambios de aceite según las recomendaciones del fabricante.",
            "No almacenar a temperaturas superiores a 60 °C.",
            "Mantener alejado de la luz solar directa, el frío extremo y las fluctuaciones bruscas de temperatura.",
            "Evitar la exposición del embalaje a la intemperie. En caso de ser inevitable, colocar los tambores en posición horizontal para prevenir la contaminación por agua y proteger la etiqueta del producto.",
        ],
        "features": [
            "Grado de viscosidad: SAE J300 5W-30",
            "Viscosidad cinemática a 40 °C: 69 mm²/s (ASTM D445)",
            "Viscosidad cinemática a 100 °C: 12 mm²/s (ASTM D445)",
            "Densidad a 15 °C: 852 kg/m³ (ASTM D4052)",
            "Índice de viscosidad: 171 (ASTM D2270)",
            "Punto de congelación: -36 °C (ASTM D97)",
            "Punto de inflamación: 233 °C (ASTM D92)",
        ],
        "whatsapp_message": "Hola, quiero consultar por el Aceite TotalEnergies QUARTZ INEO MC3 5W-30 5 Litros.",
    },
    {
        "slug": "aceite-totalenergies-quartz-ineo-mc3-5w30-1l",
        "title": "Aceite de Motor TotalEnergies QUARTZ INEO MC3 5W-30 1 Litro",
        "short_description": "Aceite sintético 5W-30 para motores diésel y gasolina. Envase de 1 litro ideal para reposición.",
        "image": "/static/img/products/aceite-ineo-mc3-5w30-1l.webp",
        "category": "Aceite de Motor",
        "brand": "TotalEnergies",
        "description": "QUARTZ INEO MC3 asegura el óptimo funcionamiento de los convertidores catalíticos de tres vías y los filtros de partículas. Contribuye a reducir las emisiones de NOx, CO2, CO y partículas, cumpliendo con los niveles de rendimiento exigidos por los fabricantes y las normas medioambientales EURO V. Prolonga la vida útil de los sistemas de post-tratamiento, previniendo la obstrucción y el llenado prematuro de los filtros de partículas. Su excelente resistencia a las variaciones de temperatura asegura la longevidad de las partes del motor en todo tipo de condiciones.",
        "recommendations": [
            "Antes de utilizar el producto, consulta siempre la guía de mantenimiento del vehículo.",
            "Realiza los cambios de aceite según las recomendaciones del fabricante.",
            "No almacenar a temperaturas superiores a 60 °C.",
            "Mantener alejado de la luz solar directa, el frío extremo y las fluctuaciones bruscas de temperatura.",
        ],
        "features": [
            "Grado de viscosidad: SAE J300 5W-30",
            "Viscosidad cinemática a 40 °C: 69 mm²/s (ASTM D445)",
            "Viscosidad cinemática a 100 °C: 12 mm²/s (ASTM D445)",
            "Densidad a 15 °C: 852 kg/m³ (ASTM D4052)",
            "Índice de viscosidad: 171 (ASTM D2270)",
            "Punto de congelación: -36 °C (ASTM D97)",
            "Punto de inflamación: 233 °C (ASTM D92)",
        ],
        "whatsapp_message": "Hola, quiero consultar por el Aceite TotalEnergies QUARTZ INEO MC3 5W-30 1 Litro.",
    },
    {
        "slug": "aceite-totalenergies-quartz-ineo-first-0w30-5l",
        "title": "Aceite de Motor TotalEnergies QUARTZ INEO FIRST 0W-30 5 Litros",
        "short_description": "Aceite sintético 0W-30 de última generación para máxima eficiencia y protección. Envase de 5 litros.",
        "image": "/static/img/products/aceite-ineo-first-0w30-5l.webp",
        "category": "Aceite de Motor",
        "brand": "TotalEnergies",
        "description": "Ahorro de combustible: Ofrece una mejora del 2,61% en eficiencia energética, según la prueba oficial M111 FE. Arranques en frío más fáciles: Gracias a su grado 0W-30 y aditivos especiales, facilita el encendido del motor incluso en temperaturas extremas, con validaciones realizadas hasta -40 °C. Protección para sistemas de control de emisiones: Optimiza el funcionamiento de catalizadores de tres vías y filtros de partículas, evitando obstrucciones por hollín o lodos. Además, reduce emisiones de NOx, HC y CO. Protección y limpieza del motor: Brinda una defensa superior contra el desgaste y la obstrucción desde el primer arranque, manteniendo el motor limpio y eficiente.",
        "recommendations": [
            "Consultar el manual de mantenimiento del vehículo antes de utilizar el producto.",
            "Realizar los cambios de aceite según las recomendaciones del fabricante.",
            "No almacenar a temperaturas superiores a 60 °C.",
            "Proteger el producto de la luz solar directa, el frío extremo y las fluctuaciones térmicas.",
            "Evitar que los envases se expongan a la intemperie. En caso necesario, colocarlos en posición horizontal para prevenir contaminación y proteger la etiqueta.",
        ],
        "features": [
            "Grado de viscosidad: SAE J300 0W-30",
            "Viscosidad cinemática a 40 °C: 50.34 mm²/s (ASTM D445)",
            "Viscosidad cinemática a 100 °C: 9.9 mm²/s (ASTM D445)",
            "Densidad a 15 °C: 844 kg/m³ (ASTM D1298)",
            "Índice de viscosidad: 187 (ASTM D2270)",
            "Punto de escurrimiento: -42 °C (ASTM D97)",
            "Punto de inflamación: 230 °C (ASTM D92)",
        ],
        "whatsapp_message": "Hola, quiero consultar por el Aceite TotalEnergies QUARTZ INEO FIRST 0W-30 5 Litros.",
    },
    {
        "slug": "aceite-totalenergies-quartz-ineo-first-0w30-1l",
        "title": "Aceite de Motor TotalEnergies QUARTZ INEO FIRST 0W-30 1 Litro",
        "short_description": "Aceite sintético 0W-30 de última generación. Envase de 1 litro para reposición.",
        "image": "/static/img/products/aceite-ineo-first-0w30-1l.webp",
        "category": "Aceite de Motor",
        "brand": "TotalEnergies",
        "description": "Ahorro de combustible: Ofrece una mejora del 2,61% en eficiencia energética, según la prueba oficial M111 FE. Arranques en frío más fáciles: Gracias a su grado 0W-30 y aditivos especiales, facilita el encendido del motor incluso en temperaturas extremas, con validaciones realizadas hasta -40 °C. Protección para sistemas de control de emisiones: Optimiza el funcionamiento de catalizadores de tres vías y filtros de partículas, evitando obstrucciones por hollín o lodos. Además, reduce emisiones de NOx, HC y CO. Protección y limpieza del motor: Brinda una defensa superior contra el desgaste y la obstrucción desde el primer arranque, manteniendo el motor limpio y eficiente.",
        "recommendations": [
            "Consultar el manual de mantenimiento del vehículo antes de utilizar el producto.",
            "Realizar los cambios de aceite según las recomendaciones del fabricante.",
            "No almacenar a temperaturas superiores a 60 °C.",
            "Proteger el producto de la luz solar directa, el frío extremo y las fluctuaciones térmicas.",
            "Evitar que los envases se expongan a la intemperie. En caso necesario, colocarlos en posición horizontal para prevenir contaminación y proteger la etiqueta.",
        ],
        "features": [
            "Grado de viscosidad: SAE J300 0W-30",
            "Viscosidad cinemática a 40 °C: 50.34 mm²/s (ASTM D445)",
            "Viscosidad cinemática a 100 °C: 9.9 mm²/s (ASTM D445)",
            "Densidad a 15 °C: 844 kg/m³ (ASTM D1298)",
            "Índice de viscosidad: 187 (ASTM D2270)",
            "Punto de escurrimiento: -42 °C (ASTM D97)",
            "Punto de inflamación: 230 °C (ASTM D92)",
        ],
        "whatsapp_message": "Hola, quiero consultar por el Aceite TotalEnergies QUARTZ INEO FIRST 0W-30 1 Litro.",
    },
    {
        "slug": "aceite-totalenergies-quartz-5000-15w40-1l",
        "title": "Aceite de Motor TotalEnergies QUARTZ 5000 SN 15W-40 1 Litro",
        "short_description": "Aceite mineral 15W-40 multiuso para motores gasolina. Alto rendimiento y protección confiable.",
        "image": "/static/img/products/aceite-quartz-5000-15w40-1l.webp",
        "category": "Aceite de Motor",
        "brand": "TotalEnergies",
        "description": "Norma API SM: Cumple con los estándares de calidad exigidos, garantizando una lubricación óptima y protección efectiva del motor. Multigrado de alto rendimiento: Forma una película lubricante resistente que asegura una excelente lubricación desde el arranque, gracias a su fluidez en frío y estabilidad frente a altas temperaturas. Capacidad detergente y dispersante: Evita la formación de depósitos, manteniendo los residuos de combustión suspendidos y asegurando la estanqueidad de la cámara de combustión. Esto permite conservar la potencia máxima del motor durante toda su vida útil. Protección antidesgaste: Prolonga la vida útil de las piezas móviles del motor, reduciendo el desgaste por fricción. Aditivos de alto desempeño: Ofrece propiedades antioxidantes, antiespumantes, anticorrosivas y antiherrumbre, que mejoran la durabilidad del lubricante. Compatibilidad total: Es perfectamente compatible con juntas y retenes, cumpliendo con las exigencias más estrictas de los fabricantes de automóviles.",
        "recommendations": [
            "Consultar el manual de mantenimiento del vehículo antes de utilizar el producto.",
            "Realizar los cambios de aceite según las recomendaciones del fabricante.",
            "No almacenar a temperaturas superiores a 60 °C.",
            "Proteger el producto de la luz solar directa, el frío extremo y las fluctuaciones térmicas.",
            "Evitar que los envases se expongan a la intemperie para prevenir contaminación y daños en el etiquetado.",
        ],
        "features": [
            "Grado de viscosidad: SAE J300 15W-40",
            "Viscosidad cinemática a 40 °C: 110 mm²/s (ASTM D445)",
            "Viscosidad cinemática a 100 °C: 14.3 mm²/s (ASTM D445)",
            "Densidad a 15 °C: 888 kg/m³ (ASTM D1298)",
            "Índice de viscosidad: 140 (ASTM D2270)",
            "Punto de goteo: -36 °C (ASTM D97)",
            "Punto de inflamación: 234 °C (ASTM D92)",
        ],
        "whatsapp_message": "Hola, quiero consultar por el Aceite TotalEnergies QUARTZ 5000 SN 15W-40 1 Litro.",
    },
    {
        "slug": "aceite-totalenergies-quartz-5000-20w50-4l",
        "title": "Aceite de Motor TotalEnergies QUARTZ 5000 SN 20W-50 4 Litros",
        "short_description": "Aceite mineral 20W-50 para motores con alto kilometraje. Protección robusta en envase de 4 litros.",
        "image": "/static/img/products/aceite-quartz-5000-20w50-4l.webp",
        "category": "Aceite de Motor",
        "brand": "TotalEnergies",
        "description": "Norma API SN: Cumple con los estándares más exigentes, garantizando una lubricación perfecta y una protección confiable del motor. Multigrado de alto rendimiento: Forma una película lubricante resistente que asegura una excelente lubricación desde el arranque, gracias a su fluidez en frío y estabilidad frente a altas temperaturas. Capacidad detergente y dispersante: Evita la formación de depósitos, manteniendo los residuos de combustión suspendidos y asegurando la estanqueidad de la cámara. Protección antidesgaste: Prolonga la vida útil de las piezas móviles del motor. Compatibilidad total: Es perfectamente compatible con juntas y retenes.",
        "recommendations": [
            "Consultar la guía de mantenimiento del vehículo antes de utilizar el producto.",
            "Realizar los cambios de aceite según las recomendaciones del fabricante.",
            "No almacenar a temperaturas superiores a 60 °C.",
            "Proteger el producto de la luz solar directa, el frío extremo y las fluctuaciones térmicas.",
            "Evitar que los envases se expongan a la intemperie.",
        ],
        "features": [
            "Grado de viscosidad: SAE J300 20W-50",
            "Viscosidad cinemática a 40 °C: 156.8 mm²/s (ASTM D445)",
            "Viscosidad cinemática a 100 °C: 17.85 mm²/s (ASTM D445)",
            "Densidad a 15 °C: 883.3 kg/m³ (ASTM D1298)",
            "Índice de viscosidad: 126 (ASTM D2270)",
            "Punto de fluidez: -30 °C (ASTM D97)",
            "Punto de inflamación: 248 °C (ASTM D92)",
        ],
        "whatsapp_message": "Hola, quiero consultar por el Aceite TotalEnergies QUARTZ 5000 SN 20W-50 4 Litros.",
    },
    {
        "slug": "aceite-super-leichtlauf-10w40-4l",
        "title": "Aceite de Motor Super Leichtlauf 10W-40 4 Litros",
        "short_description": "Aceite semi-sintético 10W-40 de alto rendimiento para motores gasolina y diésel.",
        "image": "/static/img/products/aceite-super-leichtlauf-10w40-4l.webp",
        "category": "Aceite de Motor",
        "brand": "Liqui Moly",
        "description": "Aceite de motor antifrición con tecnología de síntesis (hidrocraqueado), diseñado para satisfacer las elevadas exigencias de los potentes motores modernos de gasolina y diésel. Este aceite ahorra combustible, ofrece una protección óptima contra el desgaste y tiene un efecto positivo en los materiales de sellado, mejorando la estanqueidad del motor. Por esta razón, es una opción excelente para el uso durante todo el año en vehículos con kilometrajes superiores a 100.000 km. Regenera y conserva las juntas del motor. Proporciona una limpieza sobresaliente del motor. Ahorra combustible y reduce emisiones. Funcionamiento suave y silencioso. Rápida lubricación en arranques en frío. Probado y seguro para motores con turbocompresor y catalizador. Miscible con todos los aceites de motor convencionales.",
        "recommendations": [
            "Consultar el manual del vehículo antes de utilizar el producto.",
            "Realizar los cambios de aceite según las recomendaciones del fabricante.",
            "No almacenar a temperaturas superiores a 60 °C.",
            "Proteger de la luz solar directa y fluctuaciones térmicas.",
        ],
        "features": [
            "Clase SAE: 10W-40 (SAE J300)",
            "Densidad a 15 °C: 0,870 g/cm³ (DIN 51757)",
            "Viscosidad a 40 °C: 97,0 mm²/s (ASTM D7042)",
            "Viscosidad a 100 °C: 14,5 mm²/s (ASTM D7042)",
            "Índice de viscosidad: 155 (DIN ISO 2909)",
            "Punto de combustión: 230 °C (DIN ISO 2592)",
            "Punto de fluidez: -36 °C (DIN ISO 3016)",
            "Índice de base total: 11,0 mg KOH/g (DIN ISO 3771)",
            "Cenizas de sulfato: 1,0 – 1,6 g/100g (DIN 51575)",
            "Homologaciones: ACEA A3/B4, API SP, MB-Approval 229.3, VW 501 01 / 505 00",
        ],
        "whatsapp_message": "Hola, quiero consultar por el Aceite Super Leichtlauf 10W-40 4 Litros.",
    },
    {
        "slug": "aceite-totalenergies-quartz-7000-diesel-10w40-4l",
        "title": "Aceite de Motor Diesel TotalEnergies QUARTZ 7000 10W-40 4 Litros",
        "short_description": "Aceite semi-sintético 10W-40 especialmente formulado para motores diésel de alto desempeño.",
        "image": "/static/img/products/aceite-quartz-7000-diesel-10w40-4l.webp",
        "category": "Aceite de Motor",
        "brand": "TotalEnergies",
        "description": "Resistencia a la oxidación: Su fórmula con bases y aditivos seleccionados ofrece una excepcional protección contra la oxidación, lo que prolonga la vida útil del aceite y del motor. Limpieza eficiente: Asegura una correcta limpieza del motor al reducir la acumulación de partículas, gracias a su alto poder dispersante. Protección prolongada: Protege a largo plazo los componentes sensibles del motor —como la distribución, los aros, los pistones y las camisas— minimizando el desgaste y aumentando la durabilidad del sistema.",
        "recommendations": [
            "Consultar siempre la guía de mantenimiento del vehículo antes de utilizar el producto.",
            "Realizar los cambios de aceite según las recomendaciones del fabricante.",
            "No almacenar a temperaturas superiores a 60 °C.",
            "Mantener alejado de la luz solar directa, el frío extremo y las fluctuaciones térmicas.",
            "Evitar que el embalaje se exponga a la intemperie. Si no es posible, colocar los tambores en posición horizontal para prevenir la contaminación por agua y proteger la etiqueta del producto.",
        ],
        "features": [
            "Grado de viscosidad: SAE J300 10W-40",
            "Viscosidad cinemática a 40 °C: 96.8 mm²/s (ASTM D445)",
            "Viscosidad cinemática a 100 °C: 14.81 mm²/s (ASTM D445)",
            "Densidad a 15 °C: 873.6 kg/m³ (ASTM D1298)",
            "Índice de viscosidad: 160 (ASTM D2270)",
            "Punto de fluidez: -24 °C (ASTM D97)",
            "Punto de inflamación: 232 °C (ASTM D92)",
        ],
        "whatsapp_message": "Hola, quiero consultar por el Aceite TotalEnergies QUARTZ 7000 DIESEL 10W-40 4 Litros.",
    },
]


DEFAULT_SITE_CONTENT = {
    "hero": {
        "eyebrow": "Diagnóstico, mantención y repuestos",
        "title": "Tu vehículo en manos técnicas, rápidas y confiables.",
        "description": "Atención profesional para autos particulares y flotas. Revisamos, cotizamos y coordinamos tu servicio con una experiencia simple y actual.",
        "intro_logo": "/static/img/branding/intro-logo.png",
        "intro_logo_alt": "Logo provisional del taller",
        "intro_description": "Confianza técnica para seguir en ruta.",
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
            "eyebrow": "Repuestos / Productos",
            "title": "Repuestos y productos esenciales para tu vehículo.",
            "description": "Frenos, mantención y suspensión con atención orientada a stock, compatibilidad y soporte técnico.",
            "cta_label": "Ver todos los repuestos y productos",
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
            "title": "Visítanos en San Bernardo y conoce las opiniones de nuestros clientes.",
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
            "image": "/static/img/parts/frenos.webp",
            "whatsapp_message": "Hola, quiero consultar por repuestos de frenos.",
        },
        {
            "title": "Mantención",
            "description": "Filtros, lubricantes, bujías y kits de servicio.",
            "image": "/static/img/parts/mantencion.webp",
            "whatsapp_message": "Hola, quiero consultar por repuestos de mantención.",
        },
        {
            "title": "Suspensión",
            "description": "Amortiguadores, cazoletas, terminales y bandejas.",
            "image": "/static/img/parts/suspencion.webp",
            "whatsapp_message": "Hola, quiero consultar por repuestos de suspensión.",
        },
    ],
    "gallery": [
        {"title": "Diagnóstico electrónico", "image": "/static/img/gallery/diagnostic.webp"},
        {"title": "Mantención general", "image": "/static/img/hero.webp"},
        {"title": "Revisión de frenos", "image": "/static/img/gallery/brakes.webp"},
        {"title": "Recepción y entrega", "image": "/static/img/gallery/reception.webp"},
        {"title": "Asesoría técnica", "image": "/static/img/services/services-hero.webp"},
        {"title": "Atención de flotas", "image": "/static/img/services/fleet-service.webp"},
    ],
    "brands": [
        {"name": "Hyundai", "image": "/static/img/brands/hyundai.svg"},
        {"name": "Chevrolet", "image": "/static/img/brands/chevrolet.svg"},
        {"name": "Nissan", "image": "/static/img/brands/nissan.svg"},
        {"name": "Peugeot", "image": "/static/img/brands/peugeot.svg"},
        {"name": "Kia", "image": "/static/img/brands/kia.svg"},
        {"name": "Toyota", "image": "/static/img/brands/toyota.svg"},
        {"name": "Opel", "image": "/static/img/brands/opel.svg"},
        {"name": "Volkswagen", "image": "/static/img/brands/volkswagen.svg"},
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
        "poster": "/static/img/hero.webp",
        "label": "Espacio listo para video del taller",
    },
    "services_page": {
        "eyebrow": "Servicios",
        "title": "Atención mecánica especializada para diagnóstico, mantención y reparación.",
        "description": "Soluciones técnicas para vehículos particulares, SUV y flotas, con enfoque en seguridad, rendimiento y continuidad operativa.",
        "catalog_eyebrow": "Cobertura técnica",
        "catalog_title": "Servicios organizados para cotizar rápido y entender el alcance de cada trabajo.",
        "catalog_description": "Presentamos mantención, diagnóstico, reparación y soporte operativo con una lectura más clara, visual y comercial.",
    },
    "parts_page": {
        "eyebrow": "Repuestos / Productos",
        "title": "Venta asistida de repuestos y productos con respuesta rápida por WhatsApp.",
        "description": "La sección está preparada para evolucionar más adelante hacia un inventario o ecommerce sin rehacer la vista.",
        "catalog_eyebrow": "Catálogo asistido",
        "catalog_title": "Lubricantes y productos seleccionados para mantención, protección y rendimiento del vehículo.",
        "catalog_description": "Una vitrina más clara para consultar compatibilidad, disponibilidad y orientación técnica antes de comprar.",
        "product_cta_label": "Ver producto",
    },
    "products_detail_page": {
        "primary_cta_label": "Consultar disponibilidad",
        "back_label": "Volver a productos",
        "description_title": "Descripción",
        "recommendations_title": "Recomendaciones de uso",
        "features_title": "Características técnicas",
        "related_eyebrow": "También te puede servir",
        "related_title": "Productos relacionados para completar la mantención o reposición.",
        "related_card_cta_label": "Ver producto",
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
        "team_image": "/static/img/about/team-pablete.webp",
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
    PRODUCT_CATALOG = _get_structured_env("PRODUCT_CATALOG_JSON", "PRODUCT_CATALOG_FILE", DEFAULT_PRODUCT_CATALOG)
    SITE_CONTENT = _get_structured_env("SITE_CONTENT_JSON", "SITE_CONTENT_FILE", DEFAULT_SITE_CONTENT)


class ProductionConfig(BaseConfig):
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


def get_config():
    if _get_env("APP_ENV", "development").lower() == "production":
        return ProductionConfig
    return DevelopmentConfig
