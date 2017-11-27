#! /usr/bin/python
# -*- coding: utf-8 -*-
# Albert Moreno
import requests
from bs4 import BeautifulSoup
import csv
c = csv.writer(open("noticiasMundo.csv", "wb"))

equipos = ["alaves","athletic-bilbao","atletico-madrid","betis","celta-vigo","deportivo-coruna","eibar","fc-barcelona","getafe","leganes","malaga","levante","real-madrid","rcd-espanyol","real-sociedad","sevilla","girona-fc","ud-las-palmas","valencia","villarreal"]


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
i =-1
for equipo in equipos:

	url = "http://www.mundodeportivo.com/futbol/" + equipo
	r = requests.get(url)
	soup = BeautifulSoup(r.content,"html.parser")

	table = soup.find("div","structure-global")

	links = table.find_all("article")
	i=i+1

	for link in links:
		lista = []

		#noticia = link.text+ " "
		#linknoticia = link.get("href")
		#lista.append(equipo)
		#lista.append(linknoticia)
		#lista.append(noticia.encode('utf-8'))
		imagen = link.find("img",itemprop="thumbnail")
		if imagen is None:
			print("lel")

		else:
			linknoticia = imagen.get("data-href")
			noticia = imagen.get("alt")
			linkImagen = imagen.get("data-src-md")

		equipo2 = link.find("a")

		equip = equipo2.get("title")

		lista.append("Mundo Deportivo")
		lista.append(nombre_equipos[i])
		lista.append(equip.encode('utf8'))
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
