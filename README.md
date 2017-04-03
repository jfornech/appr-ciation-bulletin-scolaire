# Appréciation bulletin scolaire
Voici un petit programme GTK3/Python qui génère rapidement des appréciations pour les bulletins scolaires. C'est une version de test pour l'instant.
(https://cloud.githubusercontent.com/assets/17165459/24595602/5f456abc-1838-11e7-9048-fddfc7859676.png)

## Description des fichiers
bulletin : fichier éxécutable linux

main.py : fichier source python 

main.o : fichier main.py compilé avec Cython

et pour finit le fichier glade, si mon interface ne vous plait pas.

## Todo
- ajouter le nom de l'élève automatiquement 
- tester plus intelligement les choix et afficher une ponctuation plus cohérente afin ne plus avoir ce genre de chose ",,,."
- ajouter une zone d'appréciation personnalisable et sauvegardable
- revoir les critères de choix travail, investissement et comportement
- bloquer certaines checkbox en fonction des choix réalisés. Par exemple si "Excellent trimestre" est coché, il faudra griser les checkboxs du type "Ne fait aucun effort", "perturbe la classe", "N'en fout pas une ramée" , heu ... non ça je n'ai pas osé le mettre. Et et pourtant ça me démange chaque trimestre.
- corriger les "fote" d'orthographe ;-)

## Licence
GPL 3.0
Jean-François Ornech


