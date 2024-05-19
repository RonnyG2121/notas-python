from flask import Flask, render_template, url_for, request
from werkzeug.utils import redirect
from flask_migrate import Migrate
from database import db, asc
from forms import FormularioPersona
from models import Persona


app = Flask(__name__)

#Configurando el token del formulario
app.config['SECRET_KEY'] = '2DFFRTGY&Twf43543WSFH'

# Base de datos
USER_DB = 'postgres'
PASS_DB = 'kitsune1234'
URL_DB = 'localhost'
NAME_DB = 'sap_db_flask'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Migraciones
migrate = Migrate()
migrate.init_app(app, db)

# Routes
@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    personas_totales = Persona.query.count()
    personas = Persona.query.order_by(asc(Persona.id)).all()
    app.logger.debug(f"Lista de personas: {personas}.")
    app.logger.debug(f"Número de personas totales: {personas_totales}.")
    return render_template("index.html", personas=personas, personas_totales=personas_totales)

@app.route('/ver_persona/<int:id>')
def ver_persona(id):
    persona = Persona.query.get_or_404(id)
    app.logger.debug(f'Esta es la persona {persona}')

    return render_template('ver_detalles.html',
                           persona=persona)

@app.route('/agregar', methods=['GET','POST'])
def agregar() :
    persona = Persona()
    formulario = FormularioPersona(obj=persona)

    if request.method == 'POST':
        if formulario.validate_on_submit():
            formulario.populate_obj(persona)

            app.logger.debug(f'Persona a insertar: {persona}')

            #Guardando el registro en la db
            try:
                db.session.add(persona)
                db.session.commit()
            except Exception as e:
                app.logger.debug(f'Erro: {str(e)}')

            return redirect(url_for('index'))

    return render_template('agregar.html',
                           formulario = formulario)

@app.route('/editar_persona/<int:id>', methods=['GET','POST'])
def editar_persona(id) :
    persona = Persona.query.get_or_404(id)
    formulario = FormularioPersona(obj=persona)

    if request.method == 'POST':
        if formulario.validate_on_submit():
            formulario.populate_obj(persona)

            app.logger.debug(f'Persona a actualizar: {persona}')

            #Guardando el registro en la db
            try:
                db.session.commit()
            except Exception as e:
                app.logger.debug(f'Erro: {str(e)}')

            return redirect(url_for('index'))

    return render_template('editar_persona.html',
                           formulario= formulario)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    persona = Persona.query.get_or_404(id)
    app.logger.debug(f'Persona a eliminar: {persona}')
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
