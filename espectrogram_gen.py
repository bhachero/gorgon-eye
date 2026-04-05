#!/usr/bin/env python3
"""
GENERADOR DE ESPECTROGRAMA - Versión corregida (mosaico cuadrado automático)
Basado en la lógica del .bat original pero con soporte WebP y cálculo inteligente de rejilla.
"""

import subprocess
import sys
import os
from pathlib import Path
import shutil
import math

# ============================================================
# CONFIGURACIÓN (ajusta estos valores según necesites)
# ============================================================
MAX_FRAMES = 400        # Máximo de frames a incluir (si hay más, se muestrea)
TAMANO_CELDA = 300      # Tamaño de cada celda en píxeles (cuadrada)
PADDING = 4             # Píxeles entre celdas
MARGEN = 15             # Margen exterior
CALIDAD_WEBP = 85       # Calidad de salida (0-100)
FORZAR_CUADRADO = True  # Si True, el mosaico será cuadrado (mismo nº columnas y filas)
COLUMNAS_FIJO = None    # Si quieres fijar un número de columnas (ej. 30), ponlo aquí, y FORZAR_CUADRADO se ignora
# ============================================================

def verificar_ffmpeg():
    if shutil.which("ffmpeg") is None:
        input("[ERROR] No se encontró ffmpeg. Instálalo desde https://ffmpeg.org/")
        sys.exit(1)

def obtener_imagenes():
    """Busca imágenes .webp o .jpg, excluyendo el propio espectrograma."""
    imagenes = list(Path(".").glob("*.webp")) + list(Path(".").glob("*.jpg"))
    imagenes = [img for img in imagenes if img.name != "espectrograma.webp" and img.name != "espectrograma.jpg"]
    imagenes.sort()
    return imagenes

def main():
    script_dir = Path(sys.argv[0]).parent.resolve()
    os.chdir(script_dir)
    print("=" * 60)
    print("  GENERADOR DE ESPECTROGRAMA (con rejilla cuadrada automática)")
    print("=" * 60)
    verificar_ffmpeg()

    # 1. Obtener todas las imágenes
    todas = obtener_imagenes()
    total = len(todas)
    if total == 0:
        print("[ERROR] No se encontraron imágenes .webp o .jpg en esta carpeta.")
        input("Presiona Enter para salir...")
        return
    print(f"[+] Total imágenes encontradas: {total}")

    # 2. Muestreo (exactamente como en el .bat original)
    if total > MAX_FRAMES:
        skip = total // MAX_FRAMES
        if skip < 1:
            skip = 1
        imagenes = todas[::skip]
        print(f"[+] Muestreo: 1 cada {skip} imágenes -> {len(imagenes)} imágenes")
    else:
        imagenes = todas
        print(f"[+] Sin muestreo: se usarán todas")

    num_imagenes = len(imagenes)
    print(f"[+] Imágenes a procesar: {num_imagenes}")

# 3. Determinar dimensiones del mosaico CORREGIDO
    num_imagenes = len(imagenes)
    
    if COLUMNAS_FIJO is not None:
        cols = COLUMNAS_FIJO
        rows = math.ceil(num_imagenes / cols)
        print(f"[+] Modo fijo: {cols} columnas x {rows} filas")
    elif FORZAR_CUADRADO:
        # Calculamos el ancho necesario para que sea lo más cuadrado posible
        cols = math.ceil(math.sqrt(num_imagenes))
        # Calculamos las filas estrictamente necesarias para ese ancho
        rows = math.ceil(num_imagenes / cols)
        print(f"[+] Modo cuadrado optimizado: {cols} x {rows} (ajustado a {num_imagenes} imágenes)")
    else:
        cols = 30
        rows = math.ceil(num_imagenes / cols)
        print(f"[+] Modo original: {cols} x {rows}")

    # 4. Crear lista temporal para ffmpeg
    lista_temp = Path("_temp_lista.txt")
    with open(lista_temp, "w") as f:
        for img in imagenes:
            f.write(f"file '{img.resolve().as_posix()}'\n")

    # 5. Construir el filtro (idéntico al .bat pero con WebP)
    filtro = (
        f"scale={TAMANO_CELDA}:{TAMANO_CELDA}:force_original_aspect_ratio=decrease,"
        f"pad={TAMANO_CELDA}:{TAMANO_CELDA}:(ow-iw)/2:(oh-ih)/2:color=black,"
        f"tile={cols}x{rows}:padding={PADDING}:margin={MARGEN}:color=black"
    )

    comando = [
        "ffmpeg", "-hide_banner", "-loglevel", "error",
        "-f", "concat", "-safe", "0", "-i", str(lista_temp),
        "-vf", filtro,
        "-c:v", "libwebp", "-quality", str(CALIDAD_WEBP),
        "-frames:v", "1",
        "-y", "espectrograma.webp"
    ]

    print("[+] Generando espectrograma... (puede tomar unos segundos)")
    try:
        subprocess.run(comando, check=True)
        print(f"[OK] Espectrograma guardado como espectrograma.webp")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Falló ffmpeg: {e}")
    finally:
        lista_temp.unlink()

    input("\nPresiona Enter para salir...")

if __name__ == "__main__":
    main()
