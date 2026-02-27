
import datetime
import markdownify
import pathlib
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

def convertidor():
    actual = pathlib.Path.cwd()
    carpeta_destino = actual / "conversiones_md"
    
    # Asegurarse que la carpeta de destino exista
    carpeta_destino.mkdir(exist_ok=True)

    tiempoActual = datetime.datetime.now()
    for nombre_directorios, _, archivos in os.walk(actual):
        for archivo in archivos:
            if archivo.endswith(".html"):
                ruta_origen = pathlib.Path(nombre_directorios) / archivo
                
                # Leer el contenido del archivo HTML
                with open(ruta_origen, "r", encoding="utf-8") as f:
                    contenido_html = f.read()

                # Convertir HTML a Markdown
                contenido_md = markdownify.markdownify(contenido_html, heading_style="ATX")

                # Guardar el archivo convertido en Markdown
                ruta_md = carpeta_destino / (archivo.replace(".html", ".md"))
                with open(ruta_md, "w", encoding="utf-8") as f_md:
                    f_md.write(contenido_md)

                print(f"Convertido: {archivo} -> {ruta_md.name}")

    tiempo_futuro = datetime.datetime.now()
    print(f"Tiempo total transcurrido: \n{tiempo_futuro - tiempoActual}")

convertidor()
