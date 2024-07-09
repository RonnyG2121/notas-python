from spellchecker.spellchecker import SpellChecker
import os

"""
texto = ["amour", "zueño", "autimovil", "calendirio"]
try:
    corrector = SpellChecker(language='es')
    for palabra in texto:
        print(f"Texto original: {palabra}")
        print(f"Texto corregido: {corrector.correction(palabra)}")

except Exception as e:
    print(e)


"""


def corregir_texto_archivo(archivo, idioma):
    """
    Esta función es capaz de leer un archivo y corregir el texto mal escrito.
    Recibe el archivo y luego lo procesa, para finalmente devolver la cadena corregida y reemplazar el texto que estaba mal escrito por el nuevo texto corregido.
    """

    corrector = SpellChecker(language=idioma)
    directorio_actual = os.getcwd()
    ruta = os.path.join(directorio_actual, archivo)

    if not os.path.exists(ruta):
        return False
    else:
        with open(ruta, "r", encoding="utf8") as archivo_abierto:
            contenido_original = archivo_abierto.read()

        palabras_originales = contenido_original.split()
        # print(palabras_originales)
        palabras_corregidas = [corrector.correction(palabra) for palabra in palabras_originales]
        # print(palabras_corregidas)
        contenido_corregido = ' '.join(palabras_corregidas)
        
        with open(ruta, "w", encoding="utf8") as archivo_abierto:
            archivo_abierto.write(contenido_corregido)

        return True

corregir_texto_archivo("prueba.txt", "es")