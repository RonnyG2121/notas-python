import click
import json_manajer


@click.group()
def cli():
    pass

@cli.command()
def muestrausuarios():
    data = json_manajer.leer_json()
    for usuario in data:
        print(f"{usuario['id']} - {usuario['nombre']} - {usuario['apellido']}")

@cli.command()
@click.option('--nombre', required=True, help="Estos son los nombre del usuario")
@click.option('--apellido', required=True, help="Apellido del usuario")
@click.pass_context
def nuevousuario(contexto, nombre, apellido):
    if not nombre or not apellido:
        contexto.fail('E nombre y el apellido son obligatorios')
    else:
        data = json_manajer.leer_json()
        nuevo_id = len(data) +1
        nuevo_registro = {'id': nuevo_id, 'nombre': nombre, 'apellido': apellido}
        data.append(nuevo_registro)
        json_manajer.escribir_json(data)
        print(f"El nuevo usuario con el ID: {nuevo_id}, se creó exitosamente")


@cli.command()
@click.argument('id', type=int)
def getusuario(id):
    data = json_manajer.leer_json()
    usuario = next((x for x in data if x['id'] == id), None)
    if usuario is None:
        print("Este usuario no existe")
    else:
        print(f"Usuario {usuario['id']} Con el nombre: {usuario['nombre']} Y el apellido: {usuario['apellido']}")

@cli.command()
@click.argument('id', type=int)
@click.option('--nombre', default=None)
@click.option('--apellido', default=None)
def actualizausuario(id, nombre, apellido):
    data = json_manajer.leer_json()
    for usuario in data:
        if usuario['id'] == id:
            if nombre is not None:
                usuario['nombre'] = nombre
            if usuario['apellido'] is not None:
                usuario['apellido'] = apellido
            print(f"El usuario con el id {usuario['id']} se actualizó correctamente")
            break
    json_manajer.escribir_json(data)



@cli.command()
@click.argument('id', type=int)
def eliusuario(id):
    data = json_manajer.leer_json()
    usuario = next((x for x in data if x['id'] == id), None)
    if usuario is None:
        print("Este usuario no existe")
    else:
        data.remove(usuario)
        json_manajer.escribir_json(data)
        print(f"El usuario con el ID {usuario['id']}, se eliminó satisfactoriamente")



if __name__ == "__main__":
    cli()