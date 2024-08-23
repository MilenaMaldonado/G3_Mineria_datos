***Blog de Artículos***
Blog de Artículos es una aplicación web desarrollada con Flask, spaCy y TextBlob. Permite visualizar y analizar artículos académicos, ofreciendo resúmenes automáticos, análisis de sentimientos y extracción de entidades clave.

- Contenido
- Descripción del Proyecto
- Estructura del Proyecto
- Requisitos
- Instalación
- Uso
- Dependencias

# Descripción del Proyecto
La aplicación web está construida utilizando Flask y proporciona una interfaz para explorar artículos académicos. Cada artículo puede ser visualizado en detalle, mostrando:

- Título
- Autores
- Año de publicación
- Texto completo
- Resumen generado
- Entidades clave extraídas
- Análisis de sentimientos
- El análisis de sentimientos evalúa la polaridad y subjetividad del texto del artículo, proporcionando una visión general del sentimiento expresado.

# Estructura del Proyecto
La estructura del proyecto es la siguiente:

**blog-articulos/**
│
├── static/
│   ├── css/
│   │   └── styles.css         # Archivo de estilos CSS personalizados
│   └── js/
│       └── scripts.js         # Archivo de scripts JavaScript personalizados
│
├── templates/
│   ├── index.html             # Plantilla para la página de inicio
│   └── view_article.html      # Plantilla para la página de detalles del artículo
│
├── main.py                    # Archivo principal de la aplicación Flask
├── requirements.txt           # Archivo de dependencias del proyecto
└── README.md                  # Este archivo

# Implementación

main.py: Archivo principal que contiene la lógica de la aplicación Flask. Aquí se definen las rutas para la página de inicio y los detalles del artículo, así como la lógica para el análisis de sentimientos y la extracción de entidades clave.

- static/:
css/styles.css: Contiene los estilos CSS personalizados para la aplicación.
js/scripts.js: Contiene los scripts JavaScript personalizados para la aplicación (si es necesario).
- templates/:
index.html: Plantilla que muestra una lista de artículos con un resumen breve. Incluye una barra de menú, una sección principal para los artículos y un pie de página.
view_article.html: Plantilla para mostrar el artículo completo, junto con el resumen, el análisis de sentimientos y las entidades clave en una barra lateral.

# Requisitos
Antes de ejecutar la aplicación, asegúrate de tener instalados los siguientes requisitos:

Python 3.7 o superior
pip (el gestor de paquetes de Python)
Instalación
Sigue estos pasos para configurar el proyecto en tu entorno local:

# Clona el repositorio:

git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
1. Crea un entorno virtual:

python -m venv venv
Activa el entorno virtual:

En Windows:
venv\Scripts\activate

En macOS/Linux:
source venv/bin/activate

2. Instala las dependencias:
pip install -r requirements.txt

3. Descarga el modelo de spaCy:
python -m spacy download en_core_web_sm

4. Ejecuta la aplicación:
python main.py

- La aplicación estará disponible en http://localhost:5000.

# Uso
Página de Inicio: Muestra una lista de artículos con un resumen breve.

Detalles del Artículo: Muestra el artículo completo con:

Un resumen en un recuadro separado
Entidades clave extraídas en un recuadro flotante
Análisis de sentimientos en un recuadro flotante
Análisis de Sentimientos: Evalúa el texto para determinar si es positivo, negativo o neutral, y proporciona información sobre la subjetividad del texto con una descripción textual.

# Dependencias
El proyecto utiliza las siguientes bibliotecas:

Flask: Para crear la aplicación web.
spaCy: Para el procesamiento del lenguaje natural y la extracción de entidades.
TextBlob: Para el análisis de sentimientos.
Summarizer: Para generar resúmenes de los textos.

Estas dependencias están listadas en requirements.txt:

makefile

Copiar código
Flask==2.2.3
spacy==3.5.1
textblob==0.15.3
summarizer==0.7.0