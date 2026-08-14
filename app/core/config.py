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
        "title_template": "{site_name} | Servicio integral automotriz",
        "description_template": "Servicio integral automotriz con navegación rápida, servicios, repuestos y contacto por WhatsApp.",
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
        "description_template": "Catálogo de repuestos originales, filtros, frenos, encendido, lubricantes y productos automotrices con consulta directa por WhatsApp.",
    },
    "products": {
        "title_template": "Productos | {site_name}",
        "description_template": "Catálogo de productos y repuestos automotrices con lubricantes, filtros, encendido, frenos y componentes Hyundai/Kia.",
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
    "brand_mark": "HyH",
    "brand_subtitle": "Servicio integral automotriz",
    "nav_cta_label": "Agenda tu cita",
    "nav_cta_message": "Hola, quiero agendar una revisión.",
    "whatsapp_float_label": "WhatsApp",
    "whatsapp_float_aria_label": "Contactar por WhatsApp",
    "whatsapp_float_message": "Hola, quiero cotizar un servicio para mi vehículo.",
    "footer_tagline": "Servicio integral automotriz, rápido y confiable.",
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
    {
        "slug": "simunizado-pintura",
        "title": "Simunizado de pintura",
        "description": "Protección y realce de pintura con limpieza técnica, aplicación de productos especializados y terminación orientada a brillo y conservación.",
        "image": "/static/img/services/paint-sealant.webp",
        "hero_title": "Simunizado de pintura para mejorar terminación, protección y presentación exterior del vehículo.",
        "detail_intro": "El simunizado de pintura ayuda a mantener la carrocería en mejor estado visual y a prolongar el cuidado de la superficie. Trabajamos la terminación con enfoque en presentación, protección y brillo uniforme.",
        "includes": [
            "Evaluación general del estado de pintura y terminación exterior",
            "Limpieza previa y preparación de la superficie",
            "Aplicación de productos de protección y realce de brillo",
            "Terminación orientada a mejor presentación y conservación",
        ],
        "applies_to": [
            "Vehículos con pintura opaca o terminación desgastada",
            "Clientes que buscan mejorar brillo y presencia general",
            "Autos que requieren protección básica de superficie",
        ],
        "common_signs": [
            "Pérdida de brillo en la pintura",
            "Superficie con apariencia opaca",
            "Necesidad de mejorar presentación exterior",
        ],
        "whatsapp_message": "Hola, les hablo desde el sitio web y quiero solicitar una cotización correspondiente al servicio de simunizado de pintura para mi vehículo. Quedo atento a su información.",
    },
    {
        "slug": "lavado-tapiz",
        "title": "Lavado de tapiz",
        "description": "Limpieza profunda de tapices, asientos y superficies interiores para mejorar higiene, apariencia y sensación de cuidado en cabina.",
        "image": "/static/img/services/upholstery-cleaning.webp",
        "hero_title": "Lavado de tapiz orientado a limpieza profunda, higiene y mejor presentación interior.",
        "detail_intro": "El lavado de tapiz permite recuperar limpieza, olor y presencia del interior del vehículo. Realizamos un trabajo pensado para mejorar la experiencia en cabina y mantener el interior en mejores condiciones.",
        "includes": [
            "Inspección inicial de tapices, asientos y superficies interiores",
            "Limpieza profunda de zonas textiles y puntos de mayor uso",
            "Tratamiento enfocado en higiene y mejor presentación",
            "Terminación general con enfoque en orden y cuidado interior",
        ],
        "applies_to": [
            "Vehículos con manchas o suciedad acumulada en cabina",
            "Clientes que buscan mejorar higiene interior",
            "Autos de uso diario o comercial que requieren renovación visual",
        ],
        "common_signs": [
            "Tapices con suciedad visible",
            "Olores persistentes en el interior",
            "Desgaste visual de la cabina por uso continuo",
        ],
        "whatsapp_message": "Hola, les hablo desde el sitio web y quiero solicitar una cotización correspondiente al servicio de lavado de tapiz para mi vehículo. Quedo atento a su información.",
    },
    {
        "slug": "desabolladura-pintura",
        "title": "Desabolladura y pintura",
        "description": "Corrección de daños en carrocería, reparación estética y trabajos de pintura para recuperar presentación y terminación exterior.",
        "image": "/static/img/services/dent-paint-repair.webp",
        "hero_title": "Desabolladura y pintura para recuperar presentación, alineación visual y terminación de carrocería.",
        "detail_intro": "Los trabajos de desabolladura y pintura permiten corregir daños visibles en la carrocería y devolver una mejor terminación exterior al vehículo. Evaluamos el alcance del daño para definir la intervención adecuada.",
        "includes": [
            "Inspección visual de golpes, abolladuras y daños de superficie",
            "Evaluación del alcance de reparación en carrocería",
            "Preparación y terminación de zonas intervenidas",
            "Trabajo de pintura orientado a una presentación uniforme",
        ],
        "applies_to": [
            "Vehículos con golpes menores o daños estéticos visibles",
            "Clientes que buscan recuperar presentación exterior",
            "Autos que requieren reparación localizada de carrocería",
        ],
        "common_signs": [
            "Abolladuras visibles en la carrocería",
            "Rayas o zonas con pintura dañada",
            "Necesidad de reparación estética exterior",
        ],
        "whatsapp_message": "Hola, les hablo desde el sitio web y quiero solicitar una cotización correspondiente al servicio de desabolladura y pintura para mi vehículo. Quedo atento a su información.",
    },
]

DEFAULT_PRODUCT_CATALOG = [{'slug': 'aceite-mobil-super-3000-xe-5w30-4l',
  'title': 'Aceite Mobil Super 3000 XE 5W-30 4 Litros',
  'short_description': 'Aceite 100% sintético 5W-30 para motores gasolina y diésel, con foco en protección del sistema '
                       'de emisiones.',
  'image': '/static/img/products/aceite-mobil-super-3000-xe-5w30-4l.webp',
  'category': 'Aceites',
  'brand': 'Mobil',
  'description': 'Lubricante sintético de alto desempeño orientado a motores gasolina y diésel que requieren una '
                 'viscosidad 5W-30 y cuidado del sistema de emisiones. La línea Mobil Super 3000 XE está pensada para '
                 'entregar limpieza interna, protección frente al desgaste y buen comportamiento térmico en uso diario '
                 'y exigente.',
  'recommendations': ['Verificar la viscosidad y especificación exigida por el fabricante antes de instalar.',
                      'Usar filtro de aceite en buen estado y respetar los intervalos de servicio del vehículo.',
                      'Mantener el envase cerrado, protegido del sol y de temperaturas extremas.'],
  'features': ['Viscosidad SAE 5W-30.',
               'Aceite 100% sintético para motores gasolina y diésel.',
               'Ayuda a proteger sistemas de emisiones y postratamiento.',
               'Presentación: bidón de 4 litros.',
               'Orientado a limpieza, protección térmica y reducción de desgaste.'],
  'whatsapp_message': 'Hola, quiero consultar por el Aceite Mobil Super 3000 XE 5W-30 4 Litros.'},
 {'slug': 'bobina-original-accent-rb-elantra-cerato-2011-2019',
  'title': 'Bobina Original Accent RB / Elantra / Cerato 2011-2019',
  'short_description': 'Bobina de encendido original Hyundai / Kia para reposición en modelos compatibles del grupo '
                       'Accent, Elantra y Cerato.',
  'image': '/static/img/products/bobina-original-accent-rb-elantra-cerato-2011-2019.webp',
  'category': 'Encendido',
  'brand': 'Hyundai / Kia Genuine Parts',
  'description': 'Bobina de encendido original orientada a mantener una chispa estable, un ralentí parejo y una '
                 'respuesta correcta del motor en aceleración. Es una alternativa adecuada cuando existen fallas de '
                 'encendido, tironeos, pérdida de potencia o códigos asociados al sistema de ignición.',
  'recommendations': ['Verificar compatibilidad por VIN, motorización y año antes de comprar.',
                      'Revisar bujías y conectores del sistema al momento de la instalación.',
                      'Reemplazar con mano de obra calificada para evitar daños en conectores o arnés.'],
  'features': ['Tipo de pieza: bobina de encendido.',
               'Condición: repuesto original Hyundai / Kia.',
               'Part number visible: 27301-2B010.',
               'Compatibilidad comercial visible: Accent RB, Elantra, Kia Cerato 2011-2019.',
               'Pensada para reposición directa del sistema de encendido.'],
  'whatsapp_message': 'Hola, quiero consultar por la Bobina Original Accent RB / Elantra / Cerato 2011-2019.'},
 {'slug': 'aceite-mobil-super-2000-10w40-4l',
  'title': 'Aceite Mobil Super 2000 10W-40 4 Litros',
  'short_description': 'Aceite con tecnología sintética 10W-40 para motores gasolina y diésel, con muy buena '
                       'protección contra desgaste.',
  'image': '/static/img/products/aceite-mobil-super-2000-10w40-4l.webp',
  'category': 'Aceites',
  'brand': 'Mobil',
  'description': 'Lubricante con tecnología sintética diseñado para entregar protección confiable en motores de uso '
                 'diario, ayudando a controlar desgaste, oxidación y depósitos. Es una alternativa habitual para '
                 'vehículos que trabajan con viscosidad 10W-40 y necesitan una solución equilibrada entre protección y '
                 'costo de mantención.',
  'recommendations': ['Confirmar viscosidad y norma exigida por el fabricante del vehículo.',
                      'Realizar el cambio junto con filtro de aceite cuando corresponda.',
                      'Guardar el producto sellado y protegido de sol directo y contaminación.'],
  'features': ['Viscosidad SAE 10W-40.',
               'Aceite con tecnología sintética para motor gasolina y diésel.',
               'Ayuda a controlar desgaste y formación de depósitos.',
               'Presentación: bidón de 4 litros.',
               'Pensado para uso cotidiano y protección prolongada del motor.'],
  'whatsapp_message': 'Hola, quiero consultar por el Aceite Mobil Super 2000 10W-40 4 Litros.'},
 {'slug': 'plumillas-bosch-eco-grand-i10-2015-2021',
  'title': 'Plumillas Bosch Eco Hyundai Grand i10 2015-2021',
  'short_description': 'Juego de plumillas Bosch para Hyundai Grand i10, orientado a barrido parejo y buena '
                       'visibilidad en lluvia.',
  'image': '/static/img/products/plumillas-bosch-eco-grand-i10-2015-2021.webp',
  'category': 'Plumillas',
  'brand': 'Bosch',
  'description': 'Plumillas orientadas a mantener un barrido uniforme, reducir vibraciones y mejorar la visibilidad en '
                 'condiciones de lluvia o suciedad en parabrisas. La línea Bosch Eco es una opción práctica para '
                 'reposición de uso diario con montaje correcto y desempeño consistente.',
  'recommendations': ['Confirmar medida y compatibilidad exacta antes de la compra.',
                      'Instalar ambas plumillas cuando el desgaste es parejo.',
                      'Limpiar el parabrisas y el filo de goma para prolongar su vida útil.'],
  'features': ['Tipo de pieza: plumillas limpiaparabrisas.',
               'Marca: Bosch.',
               'Línea comercial visible: Eco / Classic Wiper.',
               'Compatibilidad comercial visible: Hyundai Grand i10 2015-2021.',
               'Enfocadas en visibilidad, barrido uniforme y reposición rápida.'],
  'whatsapp_message': 'Hola, quiero consultar por las Plumillas Bosch Eco para Hyundai Grand i10 2015-2021.'},
 {'slug': 'pastillas-freno-trasera-santa-fe-2005-2010',
  'title': 'Pastillas Freno Trasera Hyundai Santa Fe 2005-2010 Original',
  'short_description': 'Pastillas de freno traseras originales para Hyundai Santa Fe, pensadas para una frenada '
                       'estable y segura.',
  'image': '/static/img/products/pastillas-freno-trasera-santa-fe-2005-2010.webp',
  'category': 'Frenos',
  'brand': 'Hyundai Genuine Parts',
  'description': 'Juego de pastillas traseras originales orientado a mantener el comportamiento de frenado definido '
                 'por el fabricante, con ajuste correcto sobre el conjunto compatible. Son una opción apropiada para '
                 'reposición cuando aparece ruido, desgaste avanzado o disminución de eficiencia de frenado en el eje '
                 'trasero.',
  'recommendations': ['Verificar compatibilidad por VIN, año y versión de la Santa Fe.',
                      'Revisar discos, guías y estado general del sistema al reemplazar pastillas.',
                      'Realizar asentamiento inicial posterior a la instalación.'],
  'features': ['Tipo de pieza: pastillas de freno traseras.',
               'Condición: repuesto original Hyundai.',
               'Compatibilidad comercial visible: Hyundai Santa Fe 2005-2010.',
               'Pensadas para frenado estable, ajuste correcto y reposición segura.'],
  'whatsapp_message': 'Hola, quiero consultar por las Pastillas de Freno Traseras Hyundai Santa Fe 2005-2010 '
                      'Original.'},
 {'slug': 'sensor-map-santa-fe-24-2010-2019',
  'title': 'Sensor MAP Original Hyundai Santa Fe 2.4 2010-2019',
  'short_description': 'Sensor MAP original para Hyundai Santa Fe 2.4, clave para la lectura de presión del múltiple y '
                       'la gestión del motor.',
  'image': '/static/img/products/sensor-map-santa-fe-24-2010-2019.webp',
  'category': 'Sensores',
  'brand': 'Hyundai Genuine Parts',
  'description': 'Sensor MAP original orientado a entregar una lectura estable de la presión en admisión para que la '
                 'ECU gestione mezcla, carga y respuesta del motor con mayor precisión. Su reemplazo suele ser '
                 'relevante cuando existen tironeos, ralentí inestable, consumo anormal o códigos asociados a presión '
                 '/ carga.',
  'recommendations': ['Verificar compatibilidad exacta por VIN y código de motor.',
                      'Revisar conectores, mangueras y estado del sistema de admisión antes de reemplazar.',
                      'Borrar códigos y validar lectura con escáner después de la instalación.'],
  'features': ['Tipo de pieza: sensor MAP.',
               'Condición: repuesto original Hyundai.',
               'Part number visible en la imagen: 39300-2B000.',
               'Compatibilidad comercial visible: Hyundai Santa Fe 2.4 2010-2019.',
               'Participa en la lectura de carga y presión del múltiple de admisión.'],
  'whatsapp_message': 'Hola, quiero consultar por el Sensor MAP Original Hyundai Santa Fe 2.4 2010-2019.'},
 {'slug': 'aceite-total-quartz-ineo-mc3-5w30-5l',
  'title': 'Aceite Total Quartz INEO MC3 5W-30 5 Litros',
  'short_description': 'Aceite sintético 5W-30 de baja ceniza para motores gasolina y diésel, con foco en emisiones y '
                       'protección extendida.',
  'image': '/static/img/products/aceite-total-quartz-ineo-mc3-5w30-5l.webp',
  'category': 'Aceites',
  'brand': 'TotalEnergies',
  'description': 'Lubricante sintético de tecnología Low SAPS orientado a motores modernos gasolina y diésel, '
                 'especialmente útil en vehículos con sistemas de postratamiento y filtros de partículas. La línea '
                 'QUARTZ INEO MC3 es reconocida por combinar limpieza, resistencia térmica y protección de componentes '
                 'de emisiones en intervalos de servicio exigentes.',
  'recommendations': ['Confirmar viscosidad, homologación y nivel de cenizas requerido por el fabricante.',
                      'Usar filtro de aceite en buen estado y mantener intervalos de mantención definidos para el '
                      'vehículo.',
                      'Conservar el envase cerrado y protegido de temperatura extrema o contaminación.'],
  'features': ['Viscosidad SAE 5W-30.',
               'Aceite sintético de tecnología Low SAPS.',
               'Compatible con motores gasolina y diésel según aplicación del fabricante.',
               'Ayuda a proteger catalizador y filtro de partículas.',
               'Presentación: bidón de 5 litros.'],
  'whatsapp_message': 'Hola, quiero consultar por el Aceite Total Quartz INEO MC3 5W-30 5 Litros.'},
 {'slug': 'filtro-aceite-hyundai-i10-2007-2024',
  'title': 'Filtro de Aceite Hyundai i10 2007-2024 Original',
  'short_description': 'Filtro de aceite original para Hyundai i10, pensado para retener partículas y mantener flujo '
                       'adecuado de lubricación.',
  'image': '/static/img/products/filtro-aceite-hyundai-i10-2007-2024.webp',
  'category': 'Filtro de Aceite',
  'brand': 'Hyundai Genuine Parts',
  'description': 'Filtro de aceite original orientado a mantener la limpieza del lubricante en circulación y proteger '
                 'componentes internos del motor frente a partículas y residuos de combustión. Es una pieza crítica en '
                 'cada servicio de aceite y su compatibilidad exacta debe confirmarse por versión y motorización.',
  'recommendations': ['Verificar compatibilidad por VIN y código de motor antes de instalar.',
                      'Reemplazarlo junto con el cambio de aceite correspondiente.',
                      'Lubricar la empaquetadura y respetar el torque / ajuste de instalación recomendado.'],
  'features': ['Tipo de pieza: filtro de aceite.',
               'Condición: repuesto original Hyundai / Kia.',
               'Part number visible: 26300-02752.',
               'Compatibilidad comercial visible: Hyundai i10 2007-2024.',
               'Orientado a filtrado de partículas y protección del circuito de lubricación.'],
  'whatsapp_message': 'Hola, quiero consultar por el Filtro de Aceite Hyundai i10 2007-2024 Original.'},
 {'slug': 'aceite-total-quartz-7000-10w40-4l',
  'title': 'Aceite Total Quartz 7000 10W-40 4 Litros',
  'short_description': 'Aceite semi sintético 10W-40 para motores gasolina y diésel, orientado a limpieza y protección '
                       'prolongada.',
  'image': '/static/img/products/aceite-total-quartz-7000-10w40-4l.webp',
  'category': 'Aceites',
  'brand': 'TotalEnergies',
  'description': 'Lubricante de tecnología sintética diseñado para entregar protección frente a oxidación, desgaste y '
                 'formación de depósitos en motores gasolina y diésel compatibles. La línea QUARTZ 7000 es una '
                 'alternativa frecuente cuando se busca un aceite 10W-40 con buen equilibrio entre limpieza interna, '
                 'protección y uso diario exigente.',
  'recommendations': ['Confirmar que la viscosidad 10W-40 y la especificación sean compatibles con el motor.',
                      'Respetar el kilometraje o periodo de cambio recomendado por el fabricante.',
                      'Mantener el envase cerrado y alejado de calor excesivo o contaminación.'],
  'features': ['Viscosidad SAE 10W-40.',
               'Aceite de tecnología sintética / semi sintética según línea comercial.',
               'Aplicación para motores gasolina y diésel compatibles.',
               'Ayuda a controlar oxidación, depósitos y desgaste.',
               'Presentación: bidón de 4 litros.'],
  'whatsapp_message': 'Hola, quiero consultar por el Aceite Total Quartz 7000 10W-40 4 Litros.'},
 {'slug': 'optico-izquierdo-grand-i10-hatchback-2021',
  'title': 'Óptico Izquierdo Original Hyundai Grand i10 Hatchback 2021',
  'short_description': 'Óptico izquierdo original para Hyundai Grand i10 Hatchback, orientado a reposición con ajuste '
                       'correcto y terminación de fábrica.',
  'image': '/static/img/products/optico-izquierdo-grand-i10-hatchback-2021.webp',
  'category': 'Iluminación',
  'brand': 'Hyundai Genuine Parts',
  'description': 'Óptico delantero izquierdo original pensado para mantener alineación, terminación y compatibilidad '
                 'visual con el vehículo. Es una solución adecuada para reposición por quiebre, opacidad, filtración o '
                 'daño estructural del conjunto óptico.',
  'recommendations': ['Confirmar lado, versión de carrocería y compatibilidad exacta por VIN.',
                      'Revisar soportes, anclajes y regulación de altura al instalar.',
                      'Verificar funcionamiento de ampolletas y estanqueidad luego del montaje.'],
  'features': ['Tipo de pieza: óptico delantero izquierdo.',
               'Condición: repuesto original Hyundai.',
               'Compatibilidad comercial visible: Hyundai Grand i10 Hatchback 2021.',
               'Pensado para ajuste correcto, terminación OEM y reposición segura.'],
  'whatsapp_message': 'Hola, quiero consultar por el Óptico Izquierdo Original Hyundai Grand i10 Hatchback 2021.'},
 {'slug': 'plumillas-bosch-eco-accent-2011-2019',
  'title': 'Plumillas Bosch Eco Hyundai Accent 2011-2019',
  'short_description': 'Plumillas Bosch para Hyundai Accent con enfoque en barrido parejo, bajo ruido y visibilidad '
                       'estable.',
  'image': '/static/img/products/plumillas-bosch-eco-accent-2011-2019.webp',
  'category': 'Plumillas',
  'brand': 'Bosch',
  'description': 'Juego de plumillas orientado a mantener limpieza visual del parabrisas con un barrido más uniforme '
                 'en lluvia y uso diario. La línea Bosch Eco / Classic Wiper es una opción práctica de reposición para '
                 'quienes necesitan compatibilidad comercial clara y un funcionamiento confiable.',
  'recommendations': ['Confirmar medidas y sistema de anclaje antes de comprar.',
                      'Cambiar ambas plumillas cuando presentan desgaste similar.',
                      'Mantener parabrisas limpio para evitar daño prematuro del filo de goma.'],
  'features': ['Tipo de pieza: plumillas limpiaparabrisas.',
               'Marca: Bosch.',
               'Compatibilidad comercial visible: Hyundai Accent 2011-2019.',
               'Pensadas para barrido uniforme, mejor visibilidad y reposición simple.'],
  'whatsapp_message': 'Hola, quiero consultar por las Plumillas Bosch Eco para Hyundai Accent 2011-2019.'},
 {'slug': 'bobina-hyundai-accent-14-2015-2021',
  'title': 'Bobina Original Hyundai Accent 1.4 2015-2021',
  'short_description': 'Bobina de encendido original para Hyundai Accent 1.4, diseñada para una chispa estable y '
                       'respuesta correcta del motor.',
  'image': '/static/img/products/bobina-hyundai-accent-14-2015-2021.webp',
  'category': 'Encendido',
  'brand': 'Hyundai Genuine Parts',
  'description': 'Bobina de encendido original pensada para restablecer una entrega de chispa consistente, mejorar '
                 'ralentí y reducir fallas de combustión en motores compatibles. Es una pieza habitual de reemplazo '
                 'cuando aparecen tironeos, códigos de misfire, pérdida de potencia o encendido irregular.',
  'recommendations': ['Confirmar compatibilidad exacta por VIN y código de motor.',
                      'Revisar estado de bujías y conectores durante la instalación.',
                      'Realizar montaje con procedimiento correcto para evitar daño en arnés y aislación.'],
  'features': ['Tipo de pieza: bobina de encendido.',
               'Condición: repuesto original Hyundai.',
               'Part number visible: 27301-03200.',
               'Compatibilidad comercial visible: Hyundai Accent 1.4 2015-2021.',
               'Orientada a restablecer encendido estable y combustión eficiente.'],
  'whatsapp_message': 'Hola, quiero consultar por la Bobina Original Hyundai Accent 1.4 2015-2021.'},
 {'slug': 'filtro-aire-santa-fe-g4ke-24-2013-2019',
  'title': 'Filtro de Aire Hyundai Santa Fe G4KE 2.4 2013-2019 Original',
  'short_description': 'Filtro de aire original para Hyundai Santa Fe 2.4 G4KE, orientado a proteger admisión y '
                       'mantener flujo limpio al motor.',
  'image': '/static/img/products/filtro-aire-santa-fe-g4ke-24-2013-2019.webp',
  'category': 'Filtro de Aire',
  'brand': 'Hyundai Genuine Parts',
  'description': 'Filtro de aire original diseñado para retener polvo y partículas antes del ingreso al motor, '
                 'ayudando a mantener una combustión más limpia y un flujo de aire adecuado. Es una pieza clave en '
                 'mantenciones preventivas y suele reemplazarse cuando hay saturación, polvo acumulado o pérdida de '
                 'eficiencia.',
  'recommendations': ['Verificar compatibilidad por VIN, motor y caja filtrante.',
                      'Inspeccionar estado del ducto y del alojamiento al reemplazar el filtro.',
                      'Revisar periódicamente en zonas de alto polvo o uso severo.'],
  'features': ['Tipo de pieza: filtro de aire motor.',
               'Condición: repuesto original Hyundai.',
               'Compatibilidad comercial visible: Santa Fe G4KE 2.4 2013-2019.',
               'Ayuda a proteger admisión, mezcla y vida útil del motor.'],
  'whatsapp_message': 'Hola, quiero consultar por el Filtro de Aire Hyundai Santa Fe G4KE 2.4 2013-2019 Original.'},
 {'slug': 'kit-embrague-hyundai-verna-2018-2022',
  'title': 'Kit Embrague Hyundai Verna 2018-2022 Original',
  'short_description': 'Kit de embrague original para Hyundai Verna, pensado para reposición con acople parejo y '
                       'funcionamiento confiable.',
  'image': '/static/img/products/kit-embrague-hyundai-verna-2018-2022.webp',
  'category': 'Embrague',
  'brand': 'Hyundai Genuine Parts',
  'description': 'Conjunto de embrague orientado a recuperar suavidad de acople, control del deslizamiento y respuesta '
                 'correcta en salida y cambios de marcha. Es una opción adecuada cuando el vehículo presenta '
                 'patinamiento, vibración, dureza de pedal o desgaste del conjunto de transmisión manual.',
  'recommendations': ['Confirmar compatibilidad por VIN, motorización y transmisión.',
                      'Revisar estado de volante, rodamiento y retenes al instalar el kit.',
                      'Realizar montaje con centrado y torque adecuados.'],
  'features': ['Tipo de pieza: kit de embrague.',
               'Condición: repuesto original Hyundai.',
               'Compatibilidad comercial visible: Hyundai Verna 2018-2022.',
               'Orientado a restablecer acople, tracción y funcionamiento parejo del sistema.'],
  'whatsapp_message': 'Hola, quiero consultar por el Kit Embrague Hyundai Verna 2018-2022 Original.'},
 {'slug': 'anticongelante-mobil-permazone-verde-4l',
  'title': 'Anticongelante / Refrigerante Mobil Permazone Verde 4 Litros',
  'short_description': 'Refrigerante premezclado 50/50 listo para uso, con protección contra corrosión y control '
                       'térmico del motor.',
  'image': '/static/img/products/anticongelante-mobil-permazone-verde-4l.webp',
  'category': 'Refrigerante',
  'brand': 'Mobil',
  'description': 'Refrigerante / anticongelante premezclado listo para uso, orientado a proteger el sistema de '
                 'enfriamiento frente a corrosión, cavitación y variaciones térmicas. Es una solución práctica para '
                 'reposición o servicio, ayudando a mantener un rango de trabajo estable en climas fríos y de alta '
                 'temperatura.',
  'recommendations': ['No mezclar sin verificar compatibilidad con el refrigerante existente en el sistema.',
                      'Usar en sistema limpio y con nivel de estanque correcto.',
                      'Revisar mangueras, tapa, bomba de agua y radiador cuando se detectan pérdidas o '
                      'sobretemperatura.'],
  'features': ['Tipo de producto: anticongelante / refrigerante.',
               'Presentación: 4 litros.',
               'Fórmula lista para uso, premezclada 50/50.',
               'Rango visible en envase: protección aprox. -37 °C a 129 °C.',
               'Ayuda a proteger frente a corrosión, oxidación y control térmico.'],
  'whatsapp_message': 'Hola, quiero consultar por el Anticongelante / Refrigerante Mobil Permazone Verde 4 Litros.'},
 {'slug': 'inmovilizador-antirobo-hyundai-elantra',
  'title': 'Inmovilizador Antirobo Hyundai Elantra',
  'short_description': 'Componente asociado al sistema inmovilizador / seguridad para Hyundai Elantra, orientado a '
                       'reposición técnica.',
  'image': '/static/img/products/inmovilizador-antirobo-hyundai-elantra.webp',
  'category': 'Seguridad',
  'brand': 'Hyundai Genuine Parts',
  'description': 'Pieza asociada al sistema inmovilizador del vehículo, orientada a mantener reconocimiento correcto y '
                 'funcionamiento del sistema de seguridad / arranque en modelos compatibles. Este tipo de componente '
                 'requiere validación técnica precisa, ya que puede involucrar codificación, sincronización o '
                 'diagnóstico electrónico complementario.',
  'recommendations': ['Confirmar compatibilidad exacta por VIN antes de comprar.',
                      'Verificar si el reemplazo requiere programación o adaptación electrónica.',
                      'Instalar y diagnosticar con apoyo técnico cuando exista falla de arranque o reconocimiento.'],
  'features': ['Tipo de pieza: componente de inmovilizador / antirobo.',
               'Condición: repuesto original Hyundai.',
               'Compatibilidad comercial visible: Hyundai Elantra.',
               'Puede requerir diagnóstico o codificación según versión del vehículo.'],
  'whatsapp_message': 'Hola, quiero consultar por el Inmovilizador Antirobo Hyundai Elantra.'},
 {'slug': 'liquido-frenos-mobil-dot4-1l',
  'title': 'Líquido de Frenos Mobil DOT 4 1 Litro',
  'short_description': 'Líquido de frenos DOT 4 para sistemas hidráulicos que requieren respuesta estable y punto de '
                       'ebullición adecuado.',
  'image': '/static/img/products/liquido-frenos-mobil-dot4-1l.webp',
  'category': 'Líquido de Frenos',
  'brand': 'Mobil',
  'description': 'Fluido de frenos DOT 4 orientado a sistemas hidráulicos de frenado y embrague compatibles, diseñado '
                 'para mantener desempeño estable frente a temperatura y humedad dentro de los parámetros de servicio. '
                 'Es un insumo crítico para seguridad y debe manipularse con procedimiento limpio y envase '
                 'correctamente sellado.',
  'recommendations': ['Confirmar especificación DOT requerida por el fabricante del vehículo.',
                      'No reutilizar producto contaminado ni mezclar con fluidos incompatibles.',
                      'Realizar purga y reemplazo según plan de mantención del sistema de frenos.'],
  'features': ['Especificación visible: DOT 4.',
               'Aplicación en sistemas hidráulicos de frenos compatibles.',
               'Presentación: 1 litro.',
               'Orientado a estabilidad térmica y respuesta de frenado confiable.'],
  'whatsapp_message': 'Hola, quiero consultar por el Líquido de Frenos Mobil DOT 4 1 Litro.'},
 {'slug': 'filtro-aceite-hyundai-creta-15',
  'title': 'Filtro de Aceite Original Hyundai Creta 1.5',
  'short_description': 'Filtro de aceite original para Hyundai Creta 1.5, diseñado para servicio de lubricación con '
                       'ajuste correcto.',
  'image': '/static/img/products/filtro-aceite-hyundai-creta-15.webp',
  'category': 'Filtro de Aceite',
  'brand': 'Hyundai Genuine Parts',
  'description': 'Filtro de aceite original orientado a retener partículas y mantener flujo de lubricación estable en '
                 'motores compatibles. Es una pieza de mantención directa que ayuda a proteger componentes internos '
                 'del motor durante los intervalos normales de servicio.',
  'recommendations': ['Comprobar compatibilidad exacta por VIN y motorización.',
                      'Instalar junto con aceite y sello en condiciones correctas.',
                      'Evitar reutilización y respetar el intervalo de cambio recomendado.'],
  'features': ['Tipo de pieza: filtro de aceite.',
               'Condición: repuesto original Hyundai.',
               'Part number visible: 26350-2M000.',
               'Compatibilidad comercial visible: Hyundai Creta 1.5.',
               'Pensado para servicio de lubricación y protección del motor.'],
  'whatsapp_message': 'Hola, quiero consultar por el Filtro de Aceite Original Hyundai Creta 1.5.'},
 {'slug': 'aceite-mobil-1-esp-5w30-4l',
  'title': 'Aceite Mobil 1 ESP 5W-30 4 Litros',
  'short_description': 'Aceite sintético avanzado 5W-30 de baja ceniza, orientado a motores modernos y protección de '
                       'sistemas de emisiones.',
  'image': '/static/img/products/aceite-mobil-1-esp-5w30-4l.webp',
  'category': 'Aceites',
  'brand': 'Mobil',
  'description': 'Lubricante sintético de alto desempeño formulado para ayudar a prolongar la vida útil del motor y '
                 'proteger sistemas de emisiones como filtros de partículas y catalizadores. La línea Mobil 1 ESP es '
                 'una referencia frecuente en aplicaciones que requieren baja ceniza, limpieza interna y estabilidad '
                 'en intervalos de servicio exigentes.',
  'recommendations': ['Verificar viscosidad y homologaciones exigidas por el fabricante del vehículo.',
                      'Instalar con filtro de aceite en buen estado y respetar intervalo de cambio.',
                      'Mantener el producto almacenado de forma sellada y protegido de temperaturas extremas.'],
  'features': ['Viscosidad SAE 5W-30.',
               'Aceite sintético avanzado con enfoque en protección de emisiones.',
               'Aplicación para motores gasolina y diésel compatibles.',
               'Ayuda a controlar depósitos, desgaste y estabilidad térmica.',
               'Presentación: bidón de 4 litros.'],
  'whatsapp_message': 'Hola, quiero consultar por el Aceite Mobil 1 ESP 5W-30 4 Litros.'},
 {'slug': 'bujia-hyundai-santa-fe-2009-2021-unidad',
  'title': 'Bujía Hyundai Santa Fe 2009-2021 Original (Unidad)',
  'short_description': 'Bujía original para Hyundai Santa Fe, orientada a encendido estable y combustión eficiente en '
                       'motores compatibles.',
  'image': '/static/img/products/bujia-hyundai-santa-fe-2009-2021-unidad.webp',
  'category': 'Bujías',
  'brand': 'Hyundai Genuine Parts',
  'description': 'Bujía original pensada para sostener una chispa correcta, combustión pareja y mejor respuesta del '
                 'motor en las condiciones definidas por fábrica. Su reemplazo es habitual en mantenciones programadas '
                 'o cuando aparecen fallas de arranque, ralentí inestable o pérdida de eficiencia.',
  'recommendations': ['Confirmar referencia y holgura especificada por el fabricante antes de instalar.',
                      'Reemplazar con el torque correcto y sobre motor en condición adecuada.',
                      'Revisar bobinas y sistema de encendido si existen fallas repetitivas.'],
  'features': ['Tipo de pieza: bujía de encendido.',
               'Condición: repuesto original Hyundai.',
               'Part number visible: 18841-11051.',
               'Compatibilidad comercial visible: Hyundai Santa Fe 2009-2021.',
               'Venta por unidad según imagen de referencia.'],
  'whatsapp_message': 'Hola, quiero consultar por la Bujía Hyundai Santa Fe 2009-2021 Original (Unidad).'},
 {'slug': 'sensor-ciguenal-hyundai-accent-2011-2023',
  'title': 'Sensor Cigüeñal Hyundai Accent 1.4-1.6 2011-2023',
  'short_description': 'Sensor de posición de cigüeñal para Hyundai Accent, esencial para sincronización de encendido '
                       'e inyección.',
  'image': '/static/img/products/sensor-ciguenal-hyundai-accent-2011-2023.webp',
  'category': 'Sensores',
  'brand': 'Hyundai Genuine Parts',
  'description': 'Sensor de posición de cigüeñal orientado a informar la velocidad y posición del cigüeñal para que la '
                 'ECU controle encendido e inyección de manera precisa. Su falla puede provocar dificultad de '
                 'arranque, apagones, tironeos o códigos de sincronización del motor.',
  'recommendations': ['Confirmar compatibilidad exacta por VIN y motorización.',
                      'Revisar cableado, señal y limpieza del entorno del sensor antes de reemplazar.',
                      'Validar lectura con escáner y borrar códigos después de la instalación.'],
  'features': ['Tipo de pieza: sensor de cigüeñal.',
               'Condición: repuesto original Hyundai.',
               'Part number visible: 39180-2B000.',
               'Compatibilidad comercial visible: Hyundai Accent 1.4-1.6 2011-2023.',
               'Componente crítico para sincronización y arranque del motor.'],
  'whatsapp_message': 'Hola, quiero consultar por el Sensor Cigüeñal Hyundai Accent 1.4-1.6 2011-2023.'},
 {'slug': 'filtro-aire-hyundai-elantra-2021-2024',
  'title': 'Filtro de Aire Hyundai Elantra 1.6 / 2.0 2021-2024 Original',
  'short_description': 'Filtro de aire original para Hyundai Elantra, orientado a mantener admisión limpia y '
                       'protección del motor.',
  'image': '/static/img/products/filtro-aire-hyundai-elantra-2021-2024.webp',
  'category': 'Filtro de Aire',
  'brand': 'Hyundai Genuine Parts',
  'description': 'Filtro de aire motor diseñado para retener polvo y suciedad antes del ingreso al sistema de '
                 'admisión, ayudando a proteger el motor y sostener una mezcla aire / combustible estable. Su '
                 'reemplazo preventivo es relevante en ciclos de uso urbano, polvo o tráfico intenso.',
  'recommendations': ['Verificar compatibilidad exacta con versión 1.6 o 2.0 antes de comprar.',
                      'Revisar estado del alojamiento y sellos al momento del cambio.',
                      'Acortar intervalo de inspección en zonas con polvo o uso severo.'],
  'features': ['Tipo de pieza: filtro de aire motor.',
               'Condición: repuesto original Hyundai.',
               'Part number visible: 28113-AA100.',
               'Compatibilidad comercial visible: Hyundai Elantra 1.6 / 2.0 2021-2024.',
               'Ayuda a mantener admisión limpia y proteger componentes internos.'],
  'whatsapp_message': 'Hola, quiero consultar por el Filtro de Aire Hyundai Elantra 1.6 / 2.0 2021-2024 Original.'},
 {'slug': 'filtro-aceite-hyundai-accent-2010-2024',
  'title': 'Filtro de Aceite Hyundai Original Accent 2010-2024',
  'short_description': 'Filtro de aceite original Hyundai para Accent, pensado para mantención periódica y protección '
                       'del circuito de lubricación.',
  'image': '/static/img/products/filtro-aceite-hyundai-accent-2010-2024.webp',
  'category': 'Filtro de Aceite',
  'brand': 'Hyundai Genuine Parts',
  'description': 'Filtro de aceite original orientado a filtrar partículas suspendidas en el lubricante y sostener una '
                 'circulación limpia dentro del motor. Es una pieza base en cada cambio de aceite y su correcta '
                 'elección ayuda a proteger desgaste prematuro y suciedad acumulada en el sistema.',
  'recommendations': ['Confirmar compatibilidad por VIN, año y motorización del Accent.',
                      'Instalar siempre junto con aceite nuevo y sello en buen estado.',
                      'Respetar la frecuencia de cambio recomendada por el fabricante.'],
  'features': ['Tipo de pieza: filtro de aceite.',
               'Condición: repuesto original Hyundai.',
               'Part number visible: 26300-35505.',
               'Compatibilidad comercial visible: Hyundai Accent 2010-2024.',
               'Orientado a filtrado del lubricante y mantención preventiva.'],
  'whatsapp_message': 'Hola, quiero consultar por el Filtro de Aceite Hyundai Original Accent 2010-2024.'},
 {'slug': 'kit-bujias-hyundai-accent-2020-2023',
  'title': 'Kit de Bujías Hyundai Accent 1.4 2020-2023 Originales',
  'short_description': 'Juego de bujías originales para Hyundai Accent 1.4, orientado a mantención programada y '
                       'encendido estable.',
  'image': '/static/img/products/kit-bujias-hyundai-accent-2020-2023.webp',
  'category': 'Bujías',
  'brand': 'Hyundai Genuine Parts',
  'description': 'Kit de bujías pensado para reposición programada del sistema de encendido en motores compatibles, '
                 'ayudando a mantener una chispa más uniforme, combustión limpia y mejor respuesta de marcha. Es una '
                 'pieza habitual en mantenciones por kilometraje o cuando hay tironeos y arranque irregular.',
  'recommendations': ['Confirmar referencia exacta y compatibilidad por VIN antes de comprar.',
                      'Instalar con torque y procedimiento adecuados para evitar daño en culata o aislante.',
                      'Revisar bobinas y conectores si hay fallas repetidas de encendido.'],
  'features': ['Tipo de pieza: kit de bujías.',
               'Condición: repuesto original Hyundai.',
               'Part number visible: 18854-10080.',
               'Compatibilidad comercial visible: Hyundai Accent 1.4 2020-2023.',
               'Formato comercial visible: juego / kit.'],
  'whatsapp_message': 'Hola, quiero consultar por el Kit de Bujías Hyundai Accent 1.4 2020-2023 Originales.'},
 {'slug': 'correa-alternador-hyundai-creta-2018-2021',
  'title': 'Correa Alternador Hyundai Creta 2018-2021 Original',
  'short_description': 'Correa de accesorios original para Hyundai Creta, pensada para transmisión confiable en '
                       'sistema auxiliar.',
  'image': '/static/img/products/correa-alternador-hyundai-creta-2018-2021.webp',
  'category': 'Correas',
  'brand': 'Hyundai Genuine Parts',
  'description': 'Correa de accesorios orientada a transmitir movimiento al sistema auxiliar del motor en condiciones '
                 'estables de tensión y funcionamiento. Es una pieza importante para mantención preventiva cuando '
                 'aparecen ruidos, grietas, resequedad o desgaste del material.',
  'recommendations': ['Verificar compatibilidad exacta por VIN y configuración de accesorios.',
                      'Inspeccionar tensor, poleas y alineación antes de reemplazar la correa.',
                      'No reutilizar correas con grietas, cristalización o desgaste evidente.'],
  'features': ['Tipo de pieza: correa de accesorios / alternador.',
               'Condición: repuesto original Hyundai.',
               'Part number visible en imagen: 25212-28140.',
               'Compatibilidad comercial visible: Hyundai Creta 2018-2021.',
               'Material visible de línea EPDM para trabajo auxiliar del motor.'],
  'whatsapp_message': 'Hola, quiero consultar por la Correa Alternador Hyundai Creta 2018-2021 Original.'},
 {'slug': 'pastilla-freno-delantera-santa-fe-2019-2020',
  'title': 'Pastilla Freno Delantera Santa Fe 2.4 2019-2020 Original',
  'short_description': 'Pastillas delanteras originales para Hyundai Santa Fe 2.4, orientadas a frenado seguro y '
                       'comportamiento estable.',
  'image': '/static/img/products/pastilla-freno-delantera-santa-fe-2019-2020.webp',
  'category': 'Frenos',
  'brand': 'Hyundai Genuine Parts',
  'description': 'Juego de pastillas delanteras originales diseñado para mantener el rendimiento de frenado y el '
                 'ajuste esperado por fábrica en el eje delantero. Es una solución apropiada para reposición cuando '
                 'existe desgaste, ruido, vibración o disminución de capacidad de frenado en el tren delantero.',
  'recommendations': ['Confirmar compatibilidad exacta por VIN, motorización y año.',
                      'Revisar discos, guías y nivel del sistema antes de instalar nuevas pastillas.',
                      'Realizar asentamiento posterior a la instalación para lograr apoyo uniforme.'],
  'features': ['Tipo de pieza: pastillas de freno delanteras.',
               'Condición: repuesto original Hyundai.',
               'Compatibilidad comercial visible: Santa Fe 2.4 2019-2020.',
               'Orientadas a seguridad, estabilidad y respuesta de frenado delantera.'],
  'whatsapp_message': 'Hola, quiero consultar por la Pastilla Freno Delantera Santa Fe 2.4 2019-2020 Original.'}]


DEFAULT_SITE_CONTENT = {
    "asset_version": "20260814-1",
    "hero": {
        "eyebrow": "Diagnóstico, mantención y repuestos",
        "title": "Somos un servicio especialista en Hyundai y Kia.",
        "description": "Atención profesional con técnicos certificados por la marca. Revisamos, cotizamos y coordinamos tu servicio con una experiencia simple y actual.",
        "intro_logo": "/static/img/branding/intro-logo.webp?v=20260724-1",
        "intro_logo_fallback": "/static/img/branding/intro-logo.png?v=20260724-1",
        "intro_logo_alt": "Servicio Integral Automotriz HyH Spa",
        "intro_description": "Servicio Integral Automotriz HyH Spa",
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
            "description": "Utilizamos repuestos originales y alternativos de excelente calidad para garantizar un servicio confiable.",
        },
        {
            "title": "Entrega ordenada",
            "description": "Trabajamos con reserva de horas para optimizar nuestros tiempos de atención. Coordinamos los tiempos e informamos avances para una entrega segura.",
        },
    ],
    "home_sections": {
        "services": {
            "eyebrow": "Servicios",
            "title": "Servicios mecánicos para diagnóstico, mantención y reparación automotriz.",
            "description": "Cobertura técnica en mantención preventiva, frenos, suspensión, diagnóstico con escáner, transmisión, climatización, atención de flotas, simunizado de pintura, lavado de tapiz, desabolladura y pintura para Hyundai, Kia y otras marcas.",
            "cta_label": "Ver todos los servicios",
        },
        "brands": {
            "eyebrow": "Marcas que trabajamos",
            "title": "Especialistas Hyundai y Kia. ",
            "subtitle": "Consulta por otras marcas.",
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
        "reviews": {
            "eyebrow": "Reseñas de clientes",
            "title": "Lo que dicen quienes ya confiaron su vehículo en nosotros.",
            "description": "Opiniones reales de clientes publicadas en Google Maps.",
            "rating_headline": "Calificación 5.0 en Google Maps",
            "rating_subtext": "Respaldada por nuestros clientes",
            "controls_aria_label": "Controles de reseñas",
            "prev_aria_label": "Reseña anterior",
            "next_aria_label": "Siguiente reseña",
        },
        "map": {
            "eyebrow": "Ubicación y reseñas",
            "title": "Visítanos en Independencia y conoce las opiniones de nuestros clientes.",
            "summary_rating_label": "Calificación visible en Google Maps:",
            "primary_cta": "Ver ubicación y reseñas",
            "card_aria_label": "Abrir ubicación y reseñas del taller en Google Maps",
            "card_badge": "Ver reseñas reales",
            "preview_meta": "Independencia · Servicio automotriz",
            "preview_summary": "Abrir en Google Maps para ver ubicación, reseñas, fotos y cómo llegar.",
            "review_stars": "★★★★★",
            "maps_pill_label": "Google Maps",
        },
    },
    "parts": [
        {
            "title": "Frenos",
            "description": "Pastillas, discos, kits de embreagues y sensores para múltiples marcas.",
            "image": "/static/img/parts/frenos.webp?v=20260724-1",
            "whatsapp_message": "Hola, quiero consultar por repuestos de frenos.",
        },
        {
            "title": "Mantención",
            "description": "Filtros, lubricantes, bujías y kits de servicio.",
            "image": "/static/img/parts/mantencion.webp?v=20260724-1",
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
    "brands": [],
    "brands_featured": [
        {"name": "Hyundai", "image": "/static/img/brands/hyundai.svg"},
        {"name": "Kia", "image": "/static/img/brands/kia.svg"},
    ],


    "google_place": {
        "name": "Servicio Integral Automotriz HyH Spa",
        "rating": "5.0",
        "address": "Tte. Bisson 869, Independencia, Región Metropolitana",
        "phone": "+56 9 6847 3825",
        "maps_url": "https://maps.app.goo.gl/qwvGbr6ri1AMkWgG6",
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
            "title": "Presencia local en Independencia",
            "summary": "Consulta la ficha pública del negocio, su ubicación y la información visible para clientes en Google Maps.",
            "cta": "Explorar ficha",
        },
    ],
    "reviews": [
        {
            "author": "Johan Rodriguez",
            "rating": 5,
            "relative_time": "Hace un mes",
            "text": "Excelente servicio y atención impecables por parte de todo el equipo, muy amables y profesionales en todo momento. 100% recomendados si necesitas realizarle alguna reparación o mantención a tu Hyundai.",
        },
        {
            "author": "Francisco Salinas",
            "rating": 5,
            "relative_time": "Hace 2 meses",
            "text": "Realmente un excelente servicio, en mi caso la reparación se trataba de la correa de accesorios, algunas poleas y la bomba de agua. El auto ya no emite ningún sonido extraño y funciona perfectamente.",
        },
        {
            "author": "Gustavo Riveros",
            "rating": 5,
            "relative_time": "Hace 2 meses",
            "text": "Excelente la atención muy recomendable el trabajo fue realizado en corto plazo y con mucha dedicación. No dudaré en volver cuando lo necesite.",
        },
        {
            "author": "Ximena Tapia Figueroa",
            "rating": 5,
            "relative_time": "Hace 2 meses",
            "text": "Excelente servicio. Entregan un presupuesto claro y explican todo detalladamente en caso de requerir algún ítem adicional. Realizan un trabajo profesional. Totalmente recomendado.",
        },
        {
            "author": "Oty Muñoz",
            "rating": 5,
            "relative_time": "Hace 4 meses",
            "text": "¡Un 10 de 10 para Servicio Automotriz H&H! Llevé mi auto para revisión más mantención y la experiencia fue excepcional. Me mantuvieron informada en todo momento sobre el estado del vehículo.",
        },
        {
            "author": "Cristian Alfaro",
            "rating": 5,
            "relative_time": "Hace 6 meses",
            "text": "Después de pasar de taller en taller sin saber los mecánicos cuál era el problema que tenía mi auto, nadie me dio una solución. Luego de investigar llegué a Servicio Automotriz H&H y desde el primer momento quedé conforme.",
        },
        {
            "author": "Ignacio Hirschegger",
            "rating": 5,
            "relative_time": "Hace 7 meses",
            "text": "Muy satisfecho con la reparación de mi vehículo. Viajé desde Argentina exclusivamente para repararlo y superaron mis expectativas. Recomendado 100%.",
        },
        {
            "author": "Constanza Javiera Huechuqueo",
            "rating": 5,
            "relative_time": "Hace 8 meses",
            "text": "Llevo muchos años llevando mi vehículo a sus mantenciones y revisiones, y puedo decir con total confianza que son los únicos que han logrado mantenerlo en excelente estado. La atención es excepcional.",
        },
        {
            "author": "Alberto Stern",
            "rating": 5,
            "relative_time": "Hace 8 meses",
            "text": "Excelente taller, conocen cada detalle del vehículo, son especialistas en la marca, se dan el tiempo para explicar y conversar. El trabajo suele realizarse durante el mismo día y te mantienen informado de los avances.",
        },
        {
            "author": "Germán Cañizare",
            "rating": 5,
            "relative_time": "Hace un año",
            "text": "De las experiencias más recomendables en un taller mecánico. A pesar de viajar desde Argentina con ciertos temores, me di cuenta apenas les dejé el vehículo que son profesionales. Cumplieron con los tiempos y con lo pactado en el precio.",
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
        "title": "Repuestos y productos seleccionados para mantención, reparación y reposición.",
        "description": "Catálogo con repuestos originales, lubricantes, filtros, encendido, frenos y accesorios para consulta directa por WhatsApp.",
        "catalog_eyebrow": "Catálogo asistido",
        "catalog_title": "Productos y repuestos organizados para encontrar compatibilidad y disponibilidad más rápido.",
        "catalog_description": "Presentamos lubricantes, filtros, frenos, encendido y repuestos originales con fichas claras para consulta técnica y cotización.",
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
            "description": "Somos un taller automotriz especialistas en Hyundai y Kia orientado a seguridad, continuidad operativa y atención profesional, con una propuesta pensada para responder con rapidez y criterio técnico en cada servicio.",
        },
        "intro_title": "Soporte técnico para mantener cada unidad en ruta.",
        "intro_paragraphs": [
            "En Servicio Integral Automotriz HyH Spa entendemos que la movilidad y la seguridad del vehículo impactan directamente en la operación diaria de cada cliente. Por eso trabajamos con una atención técnica orientada a reducir tiempos muertos, ordenar diagnósticos y mantener cada unidad en condiciones confiables de funcionamiento.",
            "Contamos con infraestructura de taller, experiencia en diagnóstico avanzado y un equipo preparado para intervenir sistemas críticos con criterio, precisión y seguimiento. Desde mantenciones preventivas hasta revisión de frenos, suspensión, transmisión y escáner, abordamos cada servicio con foco en rendimiento, seguridad y continuidad operativa.",
            "Para clientes particulares, empresas y flotas, desarrollamos una atención cercana y organizada, con seguimiento técnico claro, respuesta rápida y una relación de trabajo pensada para dar respaldo real en el día a día.",
        ],
        "check_list": [
            "Especialistas en Hyundai y Kia con más de 20 años de experiencia",
            "Contamos con técnicos certificados por la marca",
            "Diagnóstico técnico preventivo y correctivo",
            "Seguimiento ordenado para particulares y empresas",
            "Continuidad operativa garantizada para flotas",
            "Transparencia en cada servicio", 
            "Información oportuna y seguimiento",
            "Garantía en nuestros trabajos",
            "Compromiso y atención personalizada",
        ],
        "team_image": "/static/img/about/team-hyh.webp",
        "team_alt": "Equipo técnico de Servicio Integral Automotriz HyH Spa",
        "team_caption": "Equipo técnico preparado para atención multimarca y soporte operativo.",
        "certifications": {
            "eyebrow": "Certificaciones",
            "title": "Respaldo y reconocimiento oficial de la marca",
            "description": "Formación y certificaciones directas de Hyundai que acreditan nuestro nivel técnico.",
            "prev_aria_label": "Ver certificación anterior",
            "next_aria_label": "Ver siguiente certificación",
            "cards": [
                {
                    "image": "/static/img/about/certifications/hyundai-world-skill-olympics-2019.webp",
                    "title": "Medalla · Hyundai World Skill Olympics 2019",
                    "description": "Distinción \"Superior Skills\" obtenida por una destacada participación en la Olimpiada Mundial de Habilidades Técnicas organizada por Hyundai Motor Company en Seúl, Corea, en 2019.",
                },
                {
                    "image": "/static/img/about/certifications/hyundai-expert-technician.webp",
                    "title": "Hyundai Certificate · Expert Technician",
                    "description": "Certificación Hyundai del programa New Technician Recognition Program, categoría Expert Technician.",
                },
                {
                    "image": "/static/img/about/certifications/hyundai-master-advisor.webp",
                    "title": "Hyundai Service Advisor Program · Master Advisor",
                    "description": "Certificación internacional Hyundai Service Advisor Program, título Master Advisor, otorgada por la División Internacional de Servicio de Hyundai Motor Company.",
                },
            ],
        },
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
                "Servicio Integral Automotriz HyH Spa busca convertirse en el soporte técnico que permita a cada cliente enfocarse en su operación mientras el taller resuelve.",
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
    SITE_NAME = _get_env("SITE_NAME", "HyH Spa")
    SITE_URL = _get_env("SITE_URL", "https://serviciohyh.cl")
    CONTACT_EMAIL = _get_env("CONTACT_EMAIL", "contacto@hyh-automotriz.cl")
    CONTACT_PHONE = _get_env("CONTACT_PHONE", "56 9 6847 3825")
    WHATSAPP_NUMBER = _get_env("WHATSAPP_NUMBER", "+56968473825")
    ADDRESS = _get_env("ADDRESS", "Av. Principal 1234, Santiago")
    BUSINESS_HOURS = _get_env("BUSINESS_HOURS", "Lun-Jue 08:30-13:00 y 14:00-18:00 | Vie 08:30-13:00 y 14:00-16:00")
    HOST = _get_env("HOST", "127.0.0.1")
    PORT = _get_int_env("PORT", 5000)
    GOOGLE_PLACES_API_KEY = _get_env("GOOGLE_PLACES_API_KEY")
    GOOGLE_PLACE_QUERY = _get_env("GOOGLE_PLACE_QUERY", "Servicio Integral Automotriz HyH Spa Tte Bisson 869 Independencia")
    GOOGLE_PLACE_ID = _get_env("GOOGLE_PLACE_ID")
    GOOGLE_PLACE_URL = _get_env(
        "GOOGLE_PLACE_URL",
        "https://maps.app.goo.gl/qwvGbr6ri1AMkWgG6",
    )
    GOOGLE_API_USER_AGENT = _get_env("GOOGLE_API_USER_AGENT", "HyH-Automotriz/1.0")
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
