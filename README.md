# PO.GG
## Outil statistique d'analyse des parties de League of Legends 

![alt text](https://github.com/Krrcharles/Outil-statistique-d-analyse-des-parties-de-League-of-Legends/blob/main/src/graphical_assets/teemo(1).png)

## Présentation
League of Legends (LOL) est un jeu vidéo populaire dans le genre Multiplayer Online Battle Arena (MOBA), créé par Riot Games. Avec plus de 100 millions de joueurs actifs en 2022, LOL continue de croître en popularité. Pour maintenir cet intérêt, Riot innove constamment en introduisant de nouveaux champions et objets, ainsi qu'en ajustant l'équilibre du jeu à travers des mises à jour régulières. Ces évolutions rendent les outils d'analyse rapide et efficace particulièrement précieux pour les joueurs, afin de les guider dans leurs choix stratégiques.

Notre projet vise à développer une solution qui fournira aux joueurs des analyses essentielles et immédiates. Nous prévoyons d'utiliser l'ensemble des données historiques des parties pour effectuer ces analyses. La solution sera conçue avec une approche d'amélioration continue, en privilégiant une programmation bien documentée et orientée objet.

Riot Games offre une API accessible, permettant l'utilisation de leurs données pour de telles initiatives. Bien qu'une introduction au fonctionnement de l'API de LOL (https://developer.riotgames.com/) sera fournie, nous disposerons également d'un ensemble de données déjà collectées pour faciliter le démarrage du projet.



## Installation with docker (recommended)
Get the image      
```bash
docker pull krrcharles/po.gg:latest
```

Run the image
```bash
docker run krrcharles/po.gg
```

## Installation with local python environement

Clone this repository locally
```bash
git clone https://github.com/Krrcharles/Outil-statistique-d-analyse-des-parties-de-League-of-Legends.git 
```

Install required packages
```bash
pip install -r requirements.txt   
```

Run the app
```bash
python your\path\Outil-statistique-d-analyse-des-parties-de-League-of-Legends\__main__.py
```
