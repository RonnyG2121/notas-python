# Contando hasta el 100 y escribiéndolo en un archivo
import os


def contar_en_archivo():
    ruta = "temas/manejo_de_archivos"

    if not os.path.exists(ruta):
        os.makedirs(ruta)
    else:
        os.chdir(ruta)
        with open("contando.txt", "w") as f:
            for i in range(1, 100 +1):
                f.write(f"{i},\n")




contar_en_archivo()