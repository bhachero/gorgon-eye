@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul

echo ====================================================
echo   GENERADOR DE DINAMOGRAMAS (SERIE COMPLETA)
echo ====================================================

:: 1. CONFIGURACIÓN DE LA REJILLA (10x10 = 100 fotos por hoja)
set "COLUMNAS=10"
set "FILAS=10"
set "BORDE=2"
set "ANCHO_CELDA=1280"

:: 2. DETECCIÓN MULTIFORMATO
set "EXTS=*.jpg *.jpeg *.png *.webp *.bmp *.tiff"
set /a "COUNT=0"
for %%i in (%EXTS%) do (
    set "filename=%%i"
    :: Evitamos procesar resultados de ejecuciones anteriores
    if /i "!filename:~0,11!" neq "dinamorama_" set /a "COUNT+=1"
)

if %COUNT% EQU 0 (
    echo [!] ERROR: No se encontraron imagenes en esta carpeta.
    pause
    exit /b
)

echo [+] Imagenes detectadas: %COUNT%
echo [+] Se generaran aproximadamente !Math_Ceil! hojas... 

:: 3. CREACIÓN DE LISTA TEMPORAL (Blindada)
if exist lista_serie.txt del lista_serie.txt
for %%i in (%EXTS%) do (
    set "filename=%%i"
    if /i "!filename:~0,11!" neq "dinamograma_" (
        echo file '%%i'>>lista_serie.txt
    )
)

:: 4. EJECUCIÓN MAESTRA (Forzado de todos los frames)
:: Añadimos el filtro 'tile' con el parámetro de salida adecuado para series
echo [+] Tejiendo serie de dinamogramas... 

ffmpeg -hide_banner -loglevel error -f concat -safe 0 -i lista_serie.txt -vf "scale=%ANCHO_CELDA%:-1,tile=%COLUMNAS%x%FILAS%:padding=%BORDE%:color=black" -vsync 0 -q:v 3 "dinamograma_%%d.jpg"

:: 5. LIMPIEZA Y VERIFICACIÓN
if exist "dinamograma_1.jpg" (
    echo.
    echo [OK] PROCESO COMPLETADO.
    echo [OK] Se han procesado los %COUNT% frames correctamente.
    del lista_serie.txt
) else (
    echo.
    echo [!] ERROR: No se generaron archivos. Revisa los permisos de la carpeta.
)

pause
