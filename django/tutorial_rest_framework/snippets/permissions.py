from rest_framework import permissions

# Con este módulo validaremos que solo el usuario que creó el fragmento pueda actualizarlo y eliminarlo

class PropietarioOVisitante(permissions.BasePermission):
    """
    Esta clase, se encargará de validar si el objeto creador, que es una instancia de User, si creó el fragmento
    """

    def has_object_permission(self, request, view, obj):
        # Si la persona no creó el fragmento, le permitiremos solo lectura

        if request.method in permissions.SAFE_METHODS:
            return True

        # Solo el creador podrá tener permisos de escritura, por lo que procederemos a retornar esa validación, que de cumplirse, va ha permitir eliminar y actualizar
        return obj.creador == request.user