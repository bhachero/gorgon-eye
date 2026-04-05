# GORGON EYE: Herramientas de Análisis Fotogramático 👁️

Repositorio oficial de los scripts metodológicos desarrollados para el proyecto **GORGON Atlas**, dedicado a la extracción programática de fotogramas y la generación de instrumentos analíticos originales: el **dinamograma fílmico** y el **espectrograma**.

Esta metodología dialoga con la tradición iconológica de Aby Warburg y la filosofía de la imagen dialéctica de Walter Benjamin, trasladando esa herencia visual y espectral al análisis contemporáneo de la imagen en movimiento.

---

## 🖼️ Resultados: La Constelación Fotogramática

Los scripts permiten generar representaciones que operan en dos escalas: la macroscópica (espectrograma) y la analítica (dinamograma).

| Proyecto | Espectrograma (Condensación Cromática) | Dinamograma (Análisis del Gesto) |
| :--- | :--- | :--- |
| **Exile** | ![Espectrograma Exile](examples/exile_espectrogram.webp) | ![Dinamograma Exile](examples/exile_dinamogram_1.webp) |
| **Reality 20** | ![Espectrograma Reality](examples/reality_20_espectrogram.webp) | ![Dinamograma Reality](examples/reality_20_dinamogram_1.webp) |
| **Caudillo** | *-* | ![Dinamograma Caudillo](examples/caudillo_dinamogram_1.webp) |

---

## 🎞️ Flujo de trabajo básico

El sistema está diseñado para que los scripts "viajen" según la etapa del proceso en la que te encuentres:

1. **Extracción:** 📸
   - Coloca el script `extractor.bat` en la carpeta donde tienes tu vídeo.
   - Haz doble clic. El script creará automáticamente una carpeta llamada **`FRAMES_GEN`** donde se guardarán todos los fotogramas extraídos (uno cada 5 segundos por defecto).

2. **Preparación del Corpus:** 📂
   - Entra en la carpeta **`FRAMES_GEN`**.
   - **Copia o mueve** los scripts generadores (`generate_dinamogram.bat` o `generate_espectrogram.bat`) **dentro** de esta carpeta, junto a las imágenes.

3. **Tejido de la Constelación:** 🕸️
   - Ejecuta el generador elegido desde dentro de **`FRAMES_GEN`**.
   - El script detectará automáticamente todos los frames y creará el **dinamograma** (en varias hojas secuenciales) o el **espectrograma** (en una sola imagen condensada).

---

## 📁 Estructura del Repositorio

* **`/v1_Windows_BAT`**: Scripts ejecutables nativos para Windows (`.bat`). La versión más accesible: doble clic y listo.
* **`/v2_Python_Scripts`**: Scripts avanzados (`.py`). Ofrecen mayor flexibilidad, manejo de formatos como WebP y control sobre la normalización de aspecto.
* **`/examples`**: Galería de resultados obtenidos.

---

## ⚙️ Requisitos del Sistema

El motor de procesado en todos los scripts es **FFmpeg**.

1. **FFmpeg**: Es obligatorio tenerlo instalado en el sistema y configurado en el `PATH` (o colocar el ejecutable `ffmpeg.exe` en la misma carpeta que los scripts).
2. **Python 3.8+** *(Solo para la carpeta `/v2_Python_Scripts`)*.

## 🚀 Instalación (Versión Python)

```bash
git clone [https://github.com/bhachero/gorgon-eye.git](https://github.com/bhachero/gorgon-eye.git)
cd gorgon-eye
pip install -r requirements.txt
