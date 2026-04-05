#!/usr/bin/env python3
"""
EXTRACTOR SOSTENIDO - AUTO (Doble clic)
Busca automáticamente vídeos o DVD en la misma carpeta que el script
y extrae 1 fotograma cada 5 segundos en una subcarpeta "FRAMES_GEN".
Genera imágenes en formato WebP (mejor compresión que JPG).
"""

import subprocess
import sys
import os
from pathlib import Path
import shutil

# ============================================================
# CONFIGURACIÓN (puedes cambiar estos valores directamente aquí)
# ============================================================
INTERVALO_SEGUNDOS = 5       # segundos entre fotogramas
ESCALA_ANCHO = 720           # ancho de salida en píxeles (alto automático)
CALIDAD_WEBP = 100            # calidad WebP (0-100, 100 es máxima)
CARPETA_SALIDA = "FRAMES_GEN"
# ============================================================

def verificar_ffmpeg():
    if shutil.which("ffmpeg") is None:
        input("[ERROR] No se encontró ffmpeg. Instálalo desde https://ffmpeg.org/ y reinicia. Presiona Enter para salir.")
        sys.exit(1)

def buscar_videos(directorio):
    """Busca archivos de vídeo en el directorio (no recursivo)."""
    extensiones = [".mp4", ".mkv", ".avi", ".m4v", ".webm", ".mov", ".MP4", ".MKV", ".AVI"]
    videos = []
    for ext in extensiones:
        videos.extend(directorio.glob(f"*{ext}"))
    return sorted(videos)

def buscar_dvd(directorio):
    """Busca si existe una carpeta VIDEO_TS o video_ts en el directorio."""
    for dvd_path in [directorio / "VIDEO_TS", directorio / "video_ts"]:
        if dvd_path.is_dir() and list(dvd_path.glob("VTS_*.VOB")):
            return dvd_path
    return None

def procesar_video(entrada, salida_carpeta):
    nombre_sin_ext = entrada.stem
    salida_frames = Path(salida_carpeta) / nombre_sin_ext
    salida_frames.mkdir(parents=True, exist_ok=True)
    plantilla = salida_frames / "frame_%04d.webp"

    fps = f"1/{INTERVALO_SEGUNDOS}"
    filtro = f"fps={fps},scale={ESCALA_ANCHO}:-1"

    comando = [
        "ffmpeg",
        "-analyzeduration", "100M",
        "-probesize", "100M",
        "-i", str(entrada),
        "-vf", filtro,
        "-c:v", "libwebp",
        "-quality", str(CALIDAD_WEBP),
        "-sn", "-dn", "-an",
        "-y",
        str(plantilla)
    ]
    print(f"[+] Extrayendo: {entrada.name} -> {salida_frames}")
    subprocess.run(comando, check=True, stderr=None)
    print(f"    ✓ {len(list(salida_frames.glob('*.webp')))} fotogramas guardados")

def procesar_dvd(dvd_path, salida_carpeta):
    salida_frames = Path(salida_carpeta) / "frames"
    salida_frames.mkdir(parents=True, exist_ok=True)

    # Encontrar título más grande
    titulos = {}
    for vob in dvd_path.glob("VTS_??_?.VOB"):
        partes = vob.stem.split("_")
        if len(partes) >= 2:
            titulo = partes[1]
            titulos[titulo] = titulos.get(titulo, 0) + vob.stat().st_size

    if not titulos:
        print("[ERROR] No se encontraron VOB válidos en VIDEO_TS.")
        return

    titulo_principal = max(titulos, key=titulos.get)
    print(f"[+] DVD detectado: título principal VTS_{titulo_principal} ({titulos[titulo_principal]/1e6:.1f} MB)")

    partes = sorted(dvd_path.glob(f"VTS_{titulo_principal}_?.VOB"))
    # Crear archivo de lista temporal
    lista_temp = Path("_temp_concat.txt")
    with open(lista_temp, "w") as f:
        for parte in partes:
            ruta = parte.resolve().as_posix()
            f.write(f"file '{ruta}'\n")

    plantilla = salida_frames / "frame_%04d.webp"
    fps = f"1/{INTERVALO_SEGUNDOS}"
    filtro = f"fps={fps},scale={ESCALA_ANCHO}:-1"

    comando = [
        "ffmpeg",
        "-analyzeduration", "100M",
        "-probesize", "100M",
        "-f", "concat",
        "-safe", "0",
        "-i", str(lista_temp),
        "-vf", filtro,
        "-c:v", "libwebp",
        "-quality", str(CALIDAD_WEBP),
        "-sn", "-dn", "-an",
        "-y",
        str(plantilla)
    ]
    print(f"[+] Extrayendo fotogramas del DVD...")
    subprocess.run(comando, check=True)
    lista_temp.unlink()
    print(f"    ✓ {len(list(salida_frames.glob('*.webp')))} fotogramas guardados en {salida_frames}")

def main():
    # Cambiar al directorio donde está este script
    script_dir = Path(sys.argv[0]).parent.resolve()
    os.chdir(script_dir)

    print("=" * 50)
    print("  EXTRACTOR SOSTENIDO - Modo automático (WebP)")
    print(f"  Intervalo: {INTERVALO_SEGUNDOS} segundos")
    print(f"  Escala: {ESCALA_ANCHO} píxeles de ancho")
    print(f"  Calidad WebP: {CALIDAD_WEBP} (0-100)")
    print("=" * 50)

    verificar_ffmpeg()

    # 1. Buscar DVD
    dvd_path = buscar_dvd(script_dir)
    if dvd_path:
        procesar_dvd(dvd_path, CARPETA_SALIDA)
        print("\n[OK] Extracción completada.")
        input("Presiona Enter para salir...")
        return

    # 2. Buscar vídeos sueltos
    videos = buscar_videos(script_dir)
    if not videos:
        print("[ERROR] No se encontraron vídeos (.mp4, .mkv, .avi, etc.) ni carpeta VIDEO_TS en esta carpeta.")
        input("Presiona Enter para salir...")
        sys.exit(1)

    print(f"[+] Se encontraron {len(videos)} vídeo(s).")
    for video in videos:
        procesar_video(video, CARPETA_SALIDA)

    print("\n[OK] Extracción completada.")
    input("Presiona Enter para salir...")

if __name__ == "__main__":
    main()
