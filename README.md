# Taller Mecánico

Sitio web para taller mecánico con arquitectura Flask + Jinja, estructura DRY,
variables de entorno, múltiples páginas y medidas base de seguridad.

## Estructura

- `app/__init__.py`: fábrica de aplicación
- `app/core/`: configuración, headers y seguridad transversal
- `app/domain/`: contenido y datos del negocio
- `app/schemas/`: validación y normalización de entrada
- `app/services/`: lógica reutilizable
- `app/web/`: blueprint y rutas HTTP
- `app/templates/`: vistas Jinja
- `app/static/`: CSS y JavaScript
- `run.py`: entrypoint local
- `.env.example`: variables de entorno de referencia
- `Dockerfile`: despliegue con contenedor
- `docker-compose.yml`: ejecución local o VPS simple
- `gunicorn.conf.py`: proceso de aplicación para producción

## Ejecutar localmente

1. Crear entorno virtual
2. Instalar dependencias con `pip install -r requirements.txt`
3. Crear `.env` a partir de `.env.example`
4. Ejecutar `python3 run.py`
4. Abrir `http://127.0.0.1:5000`

## Seguridad aplicada

- CORS restringido a orígenes permitidos
- Content Security Policy
- `X-Frame-Options: DENY`
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy`
- validación y sanitización de entradas del formulario
- sin almacenamiento de datos del formulario
- cookies endurecidas y límite de payload
- `HSTS` en producción

## Producción

### Opción recomendada si tu hosting soporta Python

No necesitas Docker obligatoriamente. Puedes desplegar con:

- `gunicorn`
- proxy inverso `Nginx`
- variables de entorno del servidor

Eso suele ser lo más simple y con menos fricción operativa.

### Opción recomendada si usarás VPS o un proveedor basado en contenedores

Docker sí conviene cuando quieres:

- empaquetar dependencias de forma consistente
- mover el proyecto entre entornos sin diferencias
- simplificar despliegues en VPS

## Siguiente paso recomendado

Reemplazar imágenes genéricas por fotos reales del taller, agregar dominio,
configurar `.env` de producción y elegir el tipo de hosting final.
