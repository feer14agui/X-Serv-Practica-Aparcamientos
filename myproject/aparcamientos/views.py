from django.shortcuts import render
from django.http import HttpResponse
from .models import Aparcamiento, Usuario, Fecha, Comentario
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import datetime
from django.shortcuts import redirect
from django.template.loader import get_template
from django.template import Context
from .parser import get_data
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from xml.sax import make_parser
#from xmlparser import myContentHandler
#from urlib.parse import unquote_plus

# Create your views here.
@csrf_exempt
#Lista de aparcamientos con la url
def lista_aparcamientos():
	#obtengo todos los aparcamientos
	aparcamientos = Aparcamiento.objects.all()

	#Creo la lista de aparcamientos
	Lista_Aparcamientos = "<ol>"
	for i in aparcamientos:
		Lista_Aparcamientos += i.Nombre
		Lista_Aparcamientos += '<li><a href="'  + i.Enlace + '">' + i.Enlace + '</a><br>'
		Lista_Aparcamientos += "<br>"

	Lista_Aparcamientos += "</ol>"
	return(Lista_Aparcamientos)

#Lista de aparcamientos sin la url
def lista_aparcamientos2():

	#obtengo todos los aparcamientos
	aparcamientos = Aparcamiento.objects.all()
	aparcamientos_ordenados = aparcamientos.order_by("-Num_Comentario")
	#Creo la lista de aparcamientos
	Lista_Aparcamientos2 = ''
	for i in aparcamientos_ordenados:
		Lista_Aparcamientos2 += '<li><a href="'  + i.Enlace + '">' + i.Nombre + '</a><br>'
		Lista_Aparcamientos2 += 'Dirección: ' + i.Clase_vial + ' ' + i.Nombre_via + '<br>'
		Lista_Aparcamientos2 += '<li><a href=http://localhost:1234/aparcamientos/'+ str(i.ident) + '>' + 'Más información</a><br>'
		Lista_Aparcamientos2 += "<br>"

	return(Lista_Aparcamientos2)

#menu para loguearse
def log ():
	salida = '<form action="" method="POST">'
	salida += 'Nombre de usuario<br><input type="text" name="Usuario"><br>'
	salida += 'Password<br><input type="password" name="Password">'
	salida += '<br><br><input type="submit" value="Entrar"><br><br>'
	salida += '</form>'

	return (salida)

def Lista_Usuarios():

	usuarios = Usuario.objects.all()
	Lista_Usuarios = 'Listado de páginas personales: <br><br>'
	for i in usuarios:
		Lista_Usuarios += i.Nombre + '<br>'
		if i.Titulo_pagina == '':
			Lista_Usuarios += 'Título: ' + i.Nombre + '<br>'
		else:
			Lista_Usuarios += 'Título: ' + i.Titulo_pagina + '<br>'
			Lista_Usuarios += '<li><a href=http://localhost:1234/'+ str(i.Nombre) + '>' + 'Más información</a><br>'
	Respuesta = Lista_Usuarios
	return(Respuesta)

def form_titulo():

	respuesta = '<br><br><form action="" method="POST">'
	respuesta += 'Titulo de página <br><input type="text" name="Titulo"><br>'
	respuesta += '<input type="submit" value="Entrar"><br><br>'
	respuesta += '</form>'
	return (respuesta)

def todos():

	respuesta = '<li><a href="/aparcamientos/"' + '>' + 'Todos</a><br>'

	return(respuesta)

def red_about():

	respuesta = '<li><a href="/about/"' + '>' + 'Ayuda</a><br>'

	return(respuesta)

def footer():

	url = 'http://datos.munimadrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?'
	url += 'vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=202584-0-aparcamientos-'
	url += 'residentes&mgmtid=e84276ac109d3410VgnVCM2000000c205a0aRCRD&preview=full'

	url2 = 'http://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=e84276ac109d3410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default'

	pie_pagina = '<html><body><p>Esta aplicación utiliza datos del portal de datos abiertos de la ciudad de Madrid. © Copyright'\
				+ '</p></body></html>'
	pie_pagina += '<a href="' + url + '">' + url + '</a><br><br>'
	pie_pagina += '<a href="' + url2 + '"> Descripcion</a>'

	#'<a href="'  + i.Enlace + '">' + i.Enlace + '</a>'

	return pie_pagina


def logearse ():

	usuario = request.POST['Usuario']
	contraseña = request.POST['Password']
	return (True)

@csrf_exempt
def aparcamientos(request):

	pie_pagina = footer()
	imagen_principal = '<img src="/static/img/banner2.jpg"/>'
	Templates = get_template("hija.html")
	#Hago el formulario para firmar por distritos
	Formulario = "Filtrar por distritos:"
	Formulario += '<form action="" method="POST">'
	Formulario += 'Distrito: <input type="text" name="Distrito">'
	Formulario += "<br>"
	Formulario += '<input type="submit" value="Filtrar">'
	Formulario += "<br>"
	Formulario += "<br>"

	Lista = lista_aparcamientos ()

	#Si me llegan un POST, porque he enviado un distrito a filtrar
	if request.method == "POST":
		Distrito_filtrado = request.POST['Distrito']

		if Distrito_filtrado == '':
			Lista = ("No ha introducido ningún distrito, vuelva a intentarlo" + "<br>"  + Lista)
		else:
			aparcamientos = Aparcamiento.objects.all()
			Lista_Filtrada = ""
			for i in aparcamientos:
				if Distrito_filtrado == i.Distrito:
					Distrito = i.Distrito
					Lista_Filtrada += '<li>' + i.Nombre + '</li>'
					Lista_Filtrada += '<a href="'  + i.Enlace + '">' + i.Enlace + '</a>'
					Lista_Filtrada += "<br>"
					Lista_Filtrada += "<br>"

			#Si no hay ningun distrito con ese nombre
			if Lista_Filtrada == '':
				Lista = ("No hay ningún aparcamiento disponible en este distrito, vuelva a intentarlo" +"<br>" + Lista)
			else:
				Lista = "<br>Lista de aparcamientos en " + Distrito + "<br><br> "+ Lista_Filtrada

	c = Context({'Formulario': Formulario, 'Lista': Lista})#aqui tengo que meter las variables que qiero en la plantilla
	renderizado = Templates.render(c)
	return HttpResponse(renderizado)
	return HttpResponse(Formulario + Lista)

@csrf_exempt
def aparcamientos_id(request, recurso):

	Templates = get_template("hija.html")

	try:
		aparcamiento = Aparcamiento.objects.get(ident=recurso)

		Nombre = aparcamiento.Nombre
		Nombre_via = aparcamiento.Nombre_via
		Via = aparcamiento.Clase_vial
		Numero = aparcamiento.Numero
		Localidad = aparcamiento.Numero
		Provincia = aparcamiento.Provincia
		Cod_Postal = aparcamiento.Cod_Postal
		Barrio = aparcamiento.Barrio
		Distrito = aparcamiento.Distrito
		Coord_X = aparcamiento.Coord_X
		Coord_Y = aparcamiento.Coord_Y
		Enlace = aparcamiento.Enlace
		Descripcion = aparcamiento.Descripcion
		Accesibilidad = aparcamiento.Accesibilidad
		Telefono = aparcamiento.Telefono
		Email = aparcamiento.Email

		if Accesibilidad == 1:
			Acces = "Accesible"
		else:
			Acces = "No Accesible"

		Respuesta = "<p>Esta es la página con la información del aparcamiento " +'<a href="'  + Enlace + '">' + Nombre + '</a>' + "</br></p>"
		Respuesta += "Descripción: " + Descripcion + "<br>"
		Respuesta += "<br>"
		Respuesta += "Barrio: " + Barrio + "<br>"
		Respuesta += "<br>"
		Respuesta += "Distrito: " + Distrito + "<br>"
		Respuesta += "<br>"
		Respuesta += "Accesibilidad: " + Acces + "<br>"
		Respuesta += "<br>"
		Respuesta += "Telefono: " + Telefono + "<br>"
		Respuesta += "<br>"
		Respuesta += "Email: " + Email + "<br>"

		Formulario = "<br> Añade tu comentario "
		Formulario += '<form action="" method="POST">'
		Formulario += 'Comentario: <input type="text" name="Comentario">'
		Formulario += ""
		Formulario += '<input type="submit" value="Comentar">'
		Formulario += "<br>"
		Formulario += "<br>"

		Respuesta += Formulario

		if request.method == "POST":
			comentario = request.POST['Comentario']
			aparcamiento = Aparcamiento.objects.get(ident=recurso)
			aparcamiento.Num_Comentario = aparcamiento.Num_Comentario + 1

			aparcamiento.save()
			p = Comentario(Aparcamiento=aparcamiento, Texto=comentario)
			p.save()

		Lista_Comentarios = Comentario.objects.all()
		Respuesta += 'Comentarios: <br>'
		for i in Lista_Comentarios:
			if aparcamiento == i.Aparcamiento:
				Respuesta += i.Texto
				Respuesta += '<br><br>'
		c = Context({'Lista': Respuesta})#aqui tengo que meter las variables que qiero en la plantilla
		renderizado = Templates.render(c)
		return HttpResponse(renderizado)
		return HttpResponse(Respuesta)

	except ObjectDoesNotExist:
		return HttpResponse("Este identificador no corresponde con ningún aparcamiento")

@csrf_exempt
def usuario(request, peticion):

	Templates = get_template("user.html")

	Titulo_Pagina = form_titulo()

	today = datetime.datetime.today()
	#Cuando me llega un POST al seleccionar un aparcamiento
	if request.method == "POST":
		key = request.body.decode('utf-8').split('=')[0]
		if key == 'Titulo':
			Titulo = request.POST[key]
			usuario = Usuario.objects.get(Nombre=peticion)
			usuario.Titulo_pagina = Titulo
			usuario.save()
		elif key == 'Seleccion':
			usuario = Usuario.objects.get(Nombre=peticion)
			nombre_aparcamiento = request.POST[key]
			lista_usuario = Fecha.objects.all()
			try:
				aparcamiento = Aparcamiento.objects.get(Nombre=nombre_aparcamiento)
				Encontrado = False
				for i in lista_usuario:
					#Si el aparcamiento ya lo tengo en la lista de seleccionados no lo añado
					if nombre_aparcamiento == i.Aparcamiento.Nombre:
						Encontrado = True

				if Encontrado == False:
					p = Fecha(Aparcamiento=aparcamiento, Usuario=usuario, Fecha=today)
					p.save()
			except ObjectDoesNotExist:
				return('')

	try:
		usuario = Usuario.objects.get(Nombre=peticion)
	#Si el usuario no tiene nombre de pagina
		if usuario.Titulo_pagina == ' ':
			Respuesta = 'Página principal de ' + usuario.Nombre + ': Página de ' + usuario.Nombre + '<br><br>'
		else:
			Respuesta = 'Página principal de ' + usuario.Nombre + ': ' + usuario.Titulo_pagina + '<br><br>'
	except ObjectDoesNotExist:
		Respuesta = 'No existe el usuario' + '<br>'

	Formulario = ''

	#Hago la lista de aparcamientos seleccionados por el usuario
	Respuesta += '<br> Lista de aparcamientos seleccionados por el Usuario ' + usuario.Nombre + '<br>'
	usuario = Usuario.objects.get(Nombre=peticion)
	lista_usuario = Fecha.objects.all()
	paginator = Paginator(lista_usuario,5)
	pag = request.GET.get('page')

	try:
		aparcamientos_selec = paginator.page(pag)
	except PageNotAnInteger:
		aparcamientos_selec = paginator.page(1)
	except:
		aparcamientos_selec = paginator.page(paginator.num_pages)
	for i in lista_usuario:
		Formulario += '<br>'
		Formulario += '<li><a href="'  + i.Aparcamiento.Enlace + '">' + i.Aparcamiento.Nombre + '</a><br>'
		Formulario += 'Dirección: ' + i.Aparcamiento.Clase_vial + ' ' + i.Aparcamiento.Nombre_via + '<br>'
		Formulario += 'Fecha: ' + str(i.Fecha) + '<br>'
		Formulario += '<li><a href=http://localhost:1234/aparcamientos/'+ str(i.Aparcamiento.ident) + '>' + 'Más información</a><br>'
	Respuesta += Formulario + '<br><br>'


	#Hago la lista de todos los aparcamientos para poder seleccionarlos
	Respuesta2 = 'Lista de aparcamientos <br><br>'
	aparcamientos = Aparcamiento.objects.all()
	Lista_Aparcamientos = ''
	Boton = ''
	for i in aparcamientos:
		Respuesta2 += i.Nombre
		Respuesta2 += "<br>"

		Respuesta2 += '<form action="" method="POST">'
		Respuesta2 += '<button type="submit" name="Seleccion" value="' + i.Nombre + '">Seleccion</button><br>'
		Respuesta2 += "<br>"

	c = Context({'Lista': Respuesta, 'Lista2': Respuesta2, 'Titulo_Pagina': Titulo_Pagina})#aqui tengo que meter las variables que qiero en la plantilla
	renderizado = Templates.render(c)
	return HttpResponse(renderizado)
	return HttpResponse(Respuesta)

@csrf_exempt
def pag_ppal (request):

	Listado = Aparcamiento.objects.all()
	if len(Listado) == 0:
		get_data()

	Logout= '<li><a href=http://localhost:1234/>' + 'Logout</a><br>'
	pie_pagina = footer()
	imagen_principal = '<img src="/static/img/banner2.jpg"/>'
	Templates = get_template("index.html")

	#obtengo todos los aparcamientos
	Lista = lista_aparcamientos2()
	Log = log()
	Respuesta = Log + Lista
	Todos = todos()
	About = red_about()
	#Ahora quiero coger las paginas personales
	Usuarios = Lista_Usuarios()
	Respuesta = Log + Lista + Usuarios
	#Hagoel botón para que solo se vean los accesibles
	Boton = '<br><form action="" method="POST">'
	Boton += '<button type="submit" name="Accesibles" value= "Accesibles">Accesibles</button><br>'
	Boton += "<br>"

	Lista_Accesibles = ''
	if request.method == "POST":
		key = request.body.decode('utf-8').split('=')[0]
		value = request.body.decode('utf-8').split('=')[1]

		if key == 'Accesibles':
			print(value)
			Respuesta = Log + Usuarios + '<br>'
	#Ahora paso a hacer el listado de los aparcamientos accesibles
			aparcamientos_accesibles = Aparcamiento.objects.filter(Accesibilidad=1)
			if value == 'No':
				Lista_Accesibles += Lista
				Boton = '<br><form action="" method="POST">'
				Boton += '<button type="submit" name="Accesibles" value= "Accesibles">Accesibles</button><br>'
				Boton += "<br>"
			else:
				Boton = '<br><form action="" method="POST">'
				Boton += '<button type="submit" name="Accesibles" value= "No">Más comentados</button><br>'
				Boton += "<br>"
				#Si solo voy a mostrar los aparcamientos disponibles borro la lista y la hago con los accesibles
				Lista = 'Listado de los aparcamientos accesibles: '
				for i in aparcamientos_accesibles:
					Lista += '<li><a href="'  + i.Enlace + '">' + i.Nombre + '</a><br>'
					Lista += 'Dirección: ' + i.Clase_vial + ' ' + i.Nombre_via + '<br>'
					Lista += '<li><a href=http://localhost:1234/aparcamientos/'+ str(i.ident) + '>' + 'Más información</a><br>'
					Lista += "<br>"


		elif key == 'Usuario':
			user = request.POST['Usuario']
			contraseña = request.POST['Password']
			try:
				usuario = Usuario.objects.get(Nombre=user)
				print(user)
				print(contraseña)
				print(usuario.Contraseña)
				if contraseña == usuario.Contraseña:
					Log = 'Estas registrado como ' + usuario.Nombre + Logout
				else:
					Log = 'Contraseña incorrecta' + Log
			except ObjectDoesNotExist:

				Lista = ('<br>Este usuario no está registrado<br><br>') + Lista

		elif key == 'Todos':
			redirect(aparcamientos)

	Respuesta += Lista_Accesibles + Boton
	Respuesta += Todos
	Respuesta += About

	c = Context({'Log': Log, 'Lista': Lista, 'Usuarios': Usuarios,"Boton":Boton, 'footer': pie_pagina})#aqui tengo que meter las variables que qiero en la plantilla
	renderizado = Templates.render(c)
	return HttpResponse(renderizado)
	return HttpResponse(Respuesta)

def about(request):

	pie_pagina = footer()

	Templates = get_template("ayuda.html")
	cuerpo =  u'<span>Práctica realizada por Fernando Aguilar Santos.</span><br><br>'
	cuerpo += u'<span>Funcionamiento:</span>'
	cuerpo += '<br><ul style="list-style-type: square">'
	cuerpo += u'<li>Página principal: muestra las 5 aparcamientos mas comentados y posteriormente un listado con las paginas personales. EL visitante se podra logear.</li>'
	cuerpo += u'<li>Pagina personal de usuario: muestra las aparcamientos seleccionados por el usuario. Además de un listado de los aparcamientos para poder seleccionarlos</li>'
	cuerpo += '<li>Aparcamientos: muestra todas los aparcamientos. Permite filtrarlos por distrito.</li>'
	cuerpo += u'<li>Aparcamiento: cada aparcamiento tiene su página con información y la posibilidad de añadir comentarios.</li>'
	cuerpo += u'<li>Además se permite modificar varios aspectos de la página web, como el estilo o el título de su página personal.</li></ul>'

	c = Context({'cuerpo': cuerpo, 'footer': pie_pagina})#aqui tengo que meter las variables que qiero en la plantilla
	renderizado = Templates.render(c)
	return HttpResponse(renderizado)

def XML (request,peticion):

	print(peticion)
	usuario = Usuario.objects.get(Nombre=peticion)
	lista_usuario = Fecha.objects.all()
	xml = "<?xml version='1.0' encoding='UTF-8' ?>"
	xml += "<data><usuario name='" + usuario.Nombre +"'>"
	for i in lista_usuario:
		if i.Usuario.Nombre == usuario.Nombre:
			aparcamiento = i.Aparcamiento
			#xml += "<aparcamiento>"
			xml += '<nombre name="' + aparcamiento.Nombre + '">'
			xml += '<address>' + aparcamiento.Clase_vial + ' ' + aparcamiento.Nombre_via + ' ' + str(aparcamiento.Numero) + '</address>'
			xml += '<Localidad>' + aparcamiento.Localidad + '</Localidad>'
			xml += '<Provincia>' + aparcamiento.Provincia + '</Provincia>'
			xml += '<Codigo-Postal>' + str(aparcamiento.Cod_Postal) + '</Codigo-Postal>'
			xml += '<Barrio>' + aparcamiento.Barrio + '</Barrio>'
			xml += '<Distrito>' + aparcamiento.Distrito + '</Distrito>'
			xml += '<CoordX>' + str(aparcamiento.Coord_X) + '</CoordX>'
			xml += '<CoordY>' + str(aparcamiento.Coord_Y) + '</CoordY>'
			#xml += '<Enlace>' + aparcamiento.Enlace + '</Enlace>'
			xml += '<Descripccion>' + aparcamiento.Descripcion + '</Descripccion>'
			xml += '<Accesibilidad>' + str(aparcamiento.Accesibilidad) + '</Accesibilidad>'
			xml += '</nombre>'
		else:
			xml +=''

	xml += '</usuario></data>'
	return HttpResponse(xml, content_type="text/xml")
