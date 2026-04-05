# GORGON EYE: Herramientas de Análisis Fotogramático 👁️🎞️

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

## ⚙️Flujo de trabajo básico:

   1. Extrae los fotogramas a intervalos regulares usando el script "Extractor".

   2. Ubica las imágenes resultantes en una única carpeta.

   3. Ejecuta el generador de dinamogramas o espectrogramas dentro de esa carpeta para componer la constelación fotogramática.

## 🚀 Instalación y Uso (Versión Python)

Si deseas utilizar la versión avanzada, clona este repositorio e instala las dependencias necesarias:

```bash
git clone [https://github.com/bhachero/gorgon-eye.git](https://github.com/bhachero/gorgon-eye.git)
cd gorgon-atlas
pip install -r requirements.txt
