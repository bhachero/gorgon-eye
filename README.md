# GORGON EYE: Herramientas de Análisis Fotogramático 👁️

Repositorio oficial de los scripts metodológicos desarrollados para el proyecto **GORGON Atlas**, dedicado a la extracción programática de fotogramas y la generación de instrumentos analíticos originales: el **dinamograma fílmico** y el **espectrograma**.

Esta metodología dialoga con la tradición iconológica de Aby Warburg y la filosofía de la imagen dialéctica de Walter Benjamin, trasladando esa herencia visual y espectral al análisis contemporáneo de la imagen en movimiento.

## 📁 Estructura del Repositorio

Para facilitar su adopción tanto por investigadores de Humanidades Digitales sin experiencia en programación como por usuarios avanzados, las herramientas se dividen en dos enfoques:

* **`/v1_Windows_BAT`**: Scripts ejecutables nativos para Windows (`.bat`). Constituyen la versión más accesible de la metodología. No requieren instalación de entornos virtuales; basta con hacer doble clic para ejecutar las extracciones y generar las rejillas visuales.
* **`/v2_Python_Scripts`**: Scripts avanzados en Python (`.py`). Ofrecen mayor flexibilidad, manejo de conversiones cruzadas (ej. WebP) y control sobre el *padding* y la normalización de la relación de aspecto.
* **`/examples`**: Galería de dinamogramas y espectrogramas generados con estas herramientas.

## ⚙️ Requisitos del Sistema

El motor algorítmico que procesa y teje las imágenes en todos los scripts es **FFmpeg**.

1. **FFmpeg**: Es obligatorio tenerlo instalado en el sistema y configurado en el `PATH` (o colocar el ejecutable `ffmpeg.exe` en la misma carpeta que los scripts `.bat`).
2. **Python 3.8 o superior** *(Requerido únicamente para usar los scripts de la carpeta `/v2_Python_Scripts`)*.

## 🎞️ Flujo de trabajo básico

El sistema está diseñado para que los scripts "viajen" según la etapa del proceso en la que te encuentres:

  1.  Extracción: 📸
        Coloca el script extractor.bat en la carpeta donde tienes tu vídeo.
        Haz doble clic. El script creará automáticamente una carpeta llamada FRAMES_GEN donde se guardarán todos los fotogramas extraídos (uno cada 5 segundos).

  2.  Preparación del Corpus: 📂
        Entra en la carpeta FRAMES_GEN.
        Copia o mueve los scripts generadores (generate_dinamogram.bat o generate_espectrogram.bat) dentro de esta carpeta, mezclados con las imágenes.

  3.  Tejido de la Constelación: 🕸️
        Ejecuta el generador elegido desde dentro de FRAMES_GEN.
        El script detectará automáticamente todos los frames y creará el dinamograma (en varias hojas secuenciales) o el espectrograma (en una sola imagen condensada).

## 🚀 Instalación y Uso (Versión Python)

Si deseas utilizar la versión avanzada para mayor control de formatos y metadatos, clona el repositorio e instala las dependencias:
Bash

git clone https://github.com/bhachero/gorgon-eye.git
cd gorgon-eye
pip install -r requirements.txt

Condición de uso: Recuerda que tanto para la versión .bat como para la de Python, es imprescindible tener FFmpeg instalado en el sistema o el archivo ffmpeg.exe presente en la carpeta de ejecución.
