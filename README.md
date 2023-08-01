# Controle continue de web scrapping 
## MEBENGA ATANGA STEPHANE
<hr />

## Technologies utilisées
>- Python 3.10


### Procédure d'Installation 
1. Installation des dépendances
> `pip install -r requirements.txt` <br/>

<br/>

### Description du projet
<hr />

Tout le code est contenu dans le notebook <b>main.ipynb<b>, ou alors si vous voulez exécuter le script en ligne de commande aller dans le dossier scripts.

Le script permet de de scrapper le site <a href='https://lnr.fr'>de la ligue nationale de rugby</a>. Nous récupérons la liste de tous les jours ayant une licence au top 14. Les données extrait sont enregistrés dans le fichier <em style="color:green">liste_joueurs_top_14.xlsx.</em>

Dans ce fichier vous pouvez remarque que certaines colonnes sont vides, il s'agit des pages qui ne conenaient pas les informations totales du joueurs. Les champs qui ont été crees sont les champs suivant:
- Nom et prenom
- Date de naissance
- Taille
- Poids
- Poste
- Club actuelle

On a au total <b>584 Enregistrements</b>.

