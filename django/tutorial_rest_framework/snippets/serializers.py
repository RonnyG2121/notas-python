from rest_framework import  serializers 
from snippets.models import Fragmento, seleccion_lenguajes, seleccion_estilos

# Serializando la clase fragmento, creando nuevos y actualizándolos

"""
class Serializador_fragmento(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titulo = serializers.CharField(required=False, allow_blank=True, max_length=150)
    codigo = serializers.CharField(style={'base_template': 'textarea.html'})
    lineas = serializers.BooleanField(required=False)
    lenguaje = serializers.ChoiceField(choices=seleccion_lenguajes, default='python')
    estilos = serializers.ChoiceField(choices=seleccion_estilos, default='friendly')

    def create(self, validated_data):
        "Este es un método que permite crear y retornar un fragmento de código pasándole los datos ya validados"
        return Fragmento.objects.create(**validated_data)

    def update(self, instance, validated_data):
        "Este método actualiza un fragmento pasándole dicho fragmento y los datos validados"

        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.codigo = validated_data.get('codigo', instance.codigo)
        instance.lineas = validated_data.get('lineas', instance.lineas)
        instance.lenguaje = validated_data.get('lenguaje', instance.lenguaje)
        instance.estilos = validated_data.get('estilos', instance.estilos)
        instance.save()
        return instance"""


# Simplificando con la clase meta y el ModelSerializer
# Esto lo que hace es obtener todos los campos que ya están definidos en el modelo y assí lo simplifica ya que no tiene que crearlos en el serializador, solo llamar al modelo y llamar a los campos en una lista llamada fields

class Serializador_fragmento(serializers.ModelSerializer):
    class Meta:
        model = Fragmento
        fields = ['id', 'titulo', 'codigo', 'lineas', 'lenguaje', 'estilos']