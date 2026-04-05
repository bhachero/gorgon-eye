#!/usr/bin/env python3
"""
GENERADOR DE DINAMOGRAMAS - Versión estable (múltiples páginas)
Crea mosaicos de 10x10 imágenes WebP/JPG, una página por cada bloque.
"""

import subprocess
import sys
import os
from pathlib import Path
import shutil
import math

# ============================================================
# CONFIGURACIÓN
# ============================================================
COLUMNAS = 10
FILAS = 10
PADDING = 2
ANCHO_CELDA = 1280
CALIDAD_WEBP = 100
# ============================================================

def verificar_ffmpeg():
    # Buscar ffmpeg en PATH o en la misma carpeta
    ffmpeg_path = shutil.which("ffmpeg")
    if ffmpeg_path is None:
        # También buscar en la carpeta del script
        local_ffmpeg = Path(sys.argv[0]).parent / "ffmpeg.exe" if os.name == 'nt' else Path(sys.argv[0]).parent / "ffmpeg"
        if local_ffmpeg.exists():
            return str(local_ffmpeg)
        print("[ERROR] No se encontró ffmpeg.")
        print("   Asegúrate de que ffmpeg esté en el PATH o en la misma carpeta que este script.")
        input("Presiona Enter para salir...")
        sys.exit(1)
    return ffmpeg_path

def obtener_imagenes():
    """Devuelve lista ordenada de imágenes .webp y .jpg, excluyendo dinamogramas previos."""
    imagenes = []
    for ext in ["*.webp", "*.jpg"]:
        imagenes.extend(Path(".").glob(ext))
    # Excluir archivos que empiecen con "dinamograma"
    imagenes = [img for img in imagenes if not img.name.startswith("dinamograma")]
    imagenes.sort()
    return imagenes

def generar_mosaico(imagenes, idx, salida):
    """Genera un mosaico con una lista de imágenes (máx COLUMNAS*FILAS)."""
    if not imagenes:
        return False
    # Crear archivo de lista temporal
    lista_temp = Path(f"_temp_dinamograma_{idx}.txt")
    with open(lista_temp, "w") as f:
        for img in imagenes:
            f.write(f"file '{img.resolve().as_posix()}'\n")
    
    filtro = f"scale={ANCHO_CELDA}:-1,tile={COLUMNAS}x{FILAS}:padding={PADDING}:color=black"
    comando = [
        ffmpeg_cmd, "-hide_banner", "-loglevel", "error",
        "-f", "concat", "-safe", "0", "-i", str(lista_temp),
        "-vf", filtro,
        "-c:v", "libwebp", "-quality", str(CALIDAD_WEBP),
        "-vsync", "0",
        "-y", str(salida)
    ]
    try:
        subprocess.run(comando, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"   [ERROR] Código {e.returncode}")
        return False
    finally:
        lista_temp.unlink()

def main():
    global ffmpeg_cmd
    # Cambiar al directorio del script
    script_dir = Path(sys.argv[0]).parent.resolve()
    os.chdir(script_dir)

    print("=" * 50)
    print("  GENERADOR DE DINAMOGRAMAS (WebP)")
    print(f"  Rejilla: {COLUMNAS} x {FILAS} = {COLUMNAS*FILAS} imágenes por hoja")
    print("=" * 50)

    # Verificar ffmpeg
    ffmpeg_cmd = verificar_ffmpeg()
    print(f"[+] FFmpeg encontrado: {ffmpeg_cmd}")

    # Buscar imágenes
    imagenes = obtener_imagenes()
    if not imagenes:
        print("[ERROR] No se encontraron imágenes .webp o .jpg en esta carpeta.")
        input("Presiona Enter para salir...")
        return

    total = len(imagenes)
    por_pagina = COLUMNAS * FILAS
    paginas = math.ceil(total / por_pagina)
    print(f"[+] Imágenes encontradas: {total}")
    print(f"[+] Se generarán {paginas} dinamograma(s)")

    for i in range(paginas):
        inicio = i * por_pagina
        fin = min(inicio + por_pagina, total)
        lote = imagenes[inicio:fin]
        nombre_salida = f"dinamograma_{i+1:03d}.webp"
        print(f"[+] Procesando página {i+1}/{paginas}: {nombre_salida} ({len(lote)} imágenes)...")
        if generar_mosaico(lote, i, Path(nombre_salida)):
            print(f"    ✓ Guardado: {nombre_salida}")
        else:
            print(f"    ✗ Error al generar {nombre_salida}")

    print("\n[OK] Proceso completado.")
    input("Presiona Enter para salir...")

if __name__ == "__main__":
    main()
