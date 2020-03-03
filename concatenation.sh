#!bin/bash
# programme pour concaténer les fichiers textes de forme 1-1.txt,1-2.txt etc... d'un répertoire
# dans la concaténation finale, les fichiers de base sont délimités par des balises, avec pour identifiant le numéro du fichier, par exemple : 1-20,3-45...
# prend en arguments :
# - le répertoire contenant les fichiers à concaténer
# - le chemin et début du nom du fichier de concaténation, par exemple ./CONCAT/contexte
# Camille REY
identifiant=1
for fichier in $(ls $1 )
do
       # enlever le fichier s'il existe déjà
       echo "<commentaire=$identifiant>" >> $2.txt
              #extraction du contenu du fichier et écriture
       cat $1$fichier | tr "[A-Z]" "[a-z]" >> $2.txt
              #fermeture balise
       echo "</commentaire>" >> $2.txt
       identifiant=$((identifiant+1))
done
