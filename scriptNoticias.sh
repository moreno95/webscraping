#!/bin/bash



#curl http://ec2-35-158-169-229.eu-central-1.compute.amazonaws.com:8983/solr/scout/update?commit=true -H "Content-Type: text/xml" --data-binary '<delete><query>*:*</query></delete>'


./scriptMundo.py

./scriptMarca.py

../Solr/solr-7.0.1/bin/post -c scout ../subir/noticiasMundo.csv 

../Solr/solr-7.0.1/bin/post -c scout ../subir/noticiasMarca.csv 

