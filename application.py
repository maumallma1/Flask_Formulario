from pydoc import render_doc
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")#el render permite traer un link de html, o un templete

@app.route("/login", methods=["POST"])
def login():
	name = request.form.get("nombre") 
	nation = request.form.get("nacionalidad")
	depart = request.form.get("departamento")
	distrit = request.form.get("distrito")
	occup = request.form.get("ocupacion")
	prefer = request.form.get("preferencias")
	email = request.form.get("correo")
	password = request.form.get("contraseña")
	born = request.form.get("nacimiento")
	return render_template("session.html", nation=nation, name=name, depart = depart, 
		distrit=distrit, occup=occup, prefer=prefer, email=email, password=password, born=born)
@app.route("/users")
def names():
	#Consultar una base de datos para users
	name_list = ["Baki", "Olivia", "Yujiro"]
	return render_template("list.html", nombres=name_list,)

@app.route("/")#es para guardar ese /algo, y ponerlo
def session():#aqui en name
    return render_template("session.html", name=name,nation=nation, depart = depart, 
		distrit=distrit, occup=occup, prefer=prefer, email=email, password=password, born=born) #eso es para conectar nuestra variable de html al argumento de la funcion en flask


