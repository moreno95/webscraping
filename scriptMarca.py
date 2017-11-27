#! /usr/bin/python
# -*- coding: utf-8 -*-
# Author: Albert Moreno
import requests
from bs4 import BeautifulSoup
import csv
c = csv.writer(open("noticiasMarca.csv", "wb"))

equipos = ["alaves.html","athletic.html","atletico.html","betis.html","celta.html","deportivo.html","eibar.html","barcelona.html","getafe.html","leganes.html","malaga.html","levante.html","real-madrid.html","espanyol.html","real-sociedad.html","sevilla.html","girona.html","las-palmas.html","valencia.html","villarreal.html"]
nombre_equipos = ["alaves","athletic","atletico","betis","celta","deportivo","eibar","barcelona","getafe","leganes","malaga","levante","real madrid","espanyol","real sociedad","sevilla","girona","las palmas","valencia","villarreal"]


listaCabecera = []

listaCabecera.append("diario")
listaCabecera.append("equipo")
listaCabecera.append("equipo2")
listaCabecera.append("linknoticia")
listaCabecera.append("linkimagen")
listaCabecera.append("noticia")

c.writerow(listaCabecera)


#Se busca por articulos para poder cojer el titulo de la noticia que puede ser de un equipo diferente
i = -1
for equipo in equipos:

	url = "http://www.marca.com/futbol/" + equipo
	r = requests.get(url)
	soup = BeautifulSoup(r.content,"html.parser")

	#table = soup.find("div","structure-global")

	links = soup.find_all("article")
	i = i+1

	for link in links:
		lista = []

		#noticia = link.text+ " "
		#linknoticia = link.get("href")
		#lista.append(equipo)
		#lista.append(linknoticia)
		#lista.append(noticia.encode('utf-8'))
		imagen = link.find("img",itemprop="contentUrl")
		noticia = link.find("a", itemprop="url")
		equipo2 = link.find("span")

		if imagen is None:
			print("lel")

		else:
			linknoticia = noticia.get("href")
			noticia = noticia.get("title")
			linkImagen = imagen.get("src")
			equipo2text = equipo2.text

		

		lista.append("Marca")
		lista.append(nombre_equipos[i])
		lista.append(equipo2text.encode('utf8'))
		lista.append(linknoticia)
		lista.append(linkImagen)
		lista.append(noticia.encode('utf8'))



		#	datos = tr.findAll("td","dat")
		#print datos
		#datos2 = datos[2:]
			
			
		#for i in datos2:
			#lista.append(i.string.encode('utf8'))
		#if noticia.isspace() or linknoticia is None :
		#	print("LEl")
		#else:
		c.writerow(lista)
	
		#print "<a href='%s'>%s</a>" %(link.get("href"), link.text)
