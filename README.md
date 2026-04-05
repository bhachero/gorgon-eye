# gorgon-eye

Suite de herramientas para la arqueología e investigación cinematográfica. Permite la extracción precisa de fotogramas y la generación de dinamogramas y espectrogramas visuales para el análisis métrico y estético del flujo fílmico. Ideal para el estudio de la evolución del montaje, el color y el movimiento en el tiempo.

Este repositorio contiene una suite de procesamiento de video diseñada para el análisis métrico y estético de materiales fílmicos. A través de la extracción de fotogramas y la creación de representaciones sintéticas (dinamogramas y espectrogramas), el software facilita el estudio del montaje, el color y el movimiento en la historia del cine.

🛠️ Componentes

    Extractor de Fotogramas: Descompone archivos de video en secuencias de imágenes de alta fidelidad para un análisis detallado cuadro por cuadro.

    Compositor de Dinamogramas: Genera una imagen única que comprime la evolución espacial de los fotogramas, permitiendo visualizar el ritmo visual y el flujo de la acción.

    Compositor de Espectrogramas: Crea una huella cromática y lumínica del video, extrayendo los valores de color predominantes para estudiar la paleta y la exposición a través del tiempo.


🚀 Instalación

Bash

# Clonar el repositorio
git clone https://github.com/tu-usuario/tu-proyecto.git

# Instalar dependencias (se recomienda usar un entorno virtual)
pip install -r requirements.txt


📋 Uso

Extracción de fotogramas

python extractor.py --input video.mp4 --output /frames

Generación de Dinamograma

python dinamograma.py --input /frames --mode horizontal

Generación de Espectrograma

python espectrograma.py --input /frames --type color


🏛️ Aplicaciones en Arqueología Cinematográfica

    Análisis del Montaje: Identificación de patrones de corte y duración de planos.

    Estudio del Color: Estudio de la degradación o el uso intencional de paletas en películas restauradas.

    Estudio de la Luz: Estudio de la iluminación y la dirección de fotografía.

    Huellas de Movimiento: Visualización de la puesta en escena y el movimiento de cámara mediante la superposición de datos.


📄 Licencia

Este proyecto está bajo la Licencia [MIT/GPL] - ver el archivo LICENSE para detalles.


⚠️ Estado del Proyecto

Este repositorio se encuentra en transición:

    Beta (Estable): Localizada en /v1-beta. Es la versión utilizada para generar todo el contenido visual y analítico de Gorgon Atlas (https://gorgon.lovable.app/). Recomendada para uso inmediato.

    Python Version (Alpha): Localizada en /v2-python. Una implementación más flexible y programática que se encuentra actualmente en fase de pruebas.
