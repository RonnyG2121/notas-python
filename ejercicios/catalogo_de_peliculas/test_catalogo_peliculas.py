from domain.peliculas import Pelicula
from servicios.catalogo_pelicula import Catalogo_peliculas as cp



opcion = None
while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar Película')
        print('2. Listar Películas')
        print('3. Eliminar catálogo películas')
        print('4. Salir')
        opcion = int(input('Escribe tu opción (1-4): '))
        if opcion == 1:
            nombre_pelicula = input('Proporciona el nombre de la película: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_Pelicula(pelicula)
        elif opcion == 2:
            cp.listar_Peliculas()
        elif opcion == 3:
            cp.eliminar_Pelicula()
    except Exception as e:
        print(f'Ocurrió un error {e}')
        opcion = None
else:
    print('Salimos del programa...')
