#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Albert Moreno
import requests
from bs4 import BeautifulSoup
import csv
c = csv.writer(open("plantillaequipo.csv", "wb"))
equipos = ["Barcelona","Valencia-Cf","Real-Madrid","Atletico-Madrid","Sevilla","Villarreal","Leganes","Betis","Real-Sociedad","Levante","Getafe","Girona-Fc","Celta","Athletic-Bilbao","Espanyol","Deportivo","Eibar","Ud-Palmas","Alaves","Malaga"]

for club in equipos:
	url = "http://www.resultados-futbol.com/" + club
	r = requests.get(url)
	soup = BeautifulSoup(r.content)

	table = soup.find("table","sdata_table")

	cabecera = [club]
	c.writerow(cabecera)

	tbody = table.find("tbody")


	trs = tbody.findAll("tr",itemprop="employee")
	for tr in trs:
		lista = []
		nombre = tr.find("span",itemprop="name")
		imagen = tr.find("img")
		edat = tr.find("b")
		print edat
		nacionalidad = tr.find("img",itemprop="image")

		lista.append(nombre.string.encode('utf8'))
		lista.append(imagen.get("src"))
		lista.append(edat.string.encode('utf8'))
		lista.append(nacionalidad.get("src"))
		
	#	datos = tr.findAll("td","dat")
		#print datos
		#datos2 = datos[2:]
		
		
		#for i in datos2:
			#lista.append(i.string.encode('utf8'))

		c.writerow(lista)
