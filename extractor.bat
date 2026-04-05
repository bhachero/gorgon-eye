@echo off
setlocal enabledelayedexpansion

:: Check for FFmpeg dependency
where ffmpeg >nul 2>&1 || (
    echo ERROR: ffmpeg not found in PATH.
    pause
    exit /b 1
)

:: 1. Create unique output directory
if not exist "FRAMES_GEN" mkdir "FRAMES_GEN"

echo [+] PROCESSING MEDIA FILES (MKV, AVI, M4V, MP4)...
echo [+] METHOD: SUSTAINED GAZE (1 FRAME / 5 SEC)

:: 2. Single-pass loop:
:: -r 1/5: Extract one frame every 5 seconds (respects long take duration).
:: -sn -dn -an: Ignore subtitles, data, and audio to prevent M4V crashes.
:: -analyzeduration/probesize: Force deep header analysis for complex containers.

for %%f in (*.mkv *.avi *.m4v *.mp4) do (
    echo [+] Extracting from: %%f
    ffmpeg -analyzeduration 100M -probesize 100M -i "%%f" -vf "fps=1/5,scale=720:-1" -q:v 2 -sn -dn -an "FRAMES_GEN\frame_%%04d.jpg"
)

echo.
echo [OK] PROCESS COMPLETED.
pause
