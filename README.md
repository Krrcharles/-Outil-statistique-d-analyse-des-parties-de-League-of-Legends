# PO.GG
## Statistical Analysis Tool for League of Legends Matches

![alt text](https://github.com/Krrcharles/Outil-statistique-d-analyse-des-parties-de-League-of-Legends/blob/main/src/graphical_assets/teemo(1).png)

## Présentation

League of Legends (LOL) is a popular video game in the Multiplayer Online Battle Arena (MOBA) genre, developed by Riot Games. With over 100 million active players in 2022, LOL's popularity continues to soar. To keep up with this interest, Riot consistently innovates by introducing new champions and items, as well as balancing the game through regular updates. These developments make quick and efficient analysis tools particularly valuable for players, aiding them in their strategic choices.

Our project aims to create a solution that will provide players with essential and immediate analyses. We plan to utilize a comprehensive historical dataset of game matches for these analyses. The solution is designed with a continuous improvement approach, emphasizing well-documented, object-oriented programming.

Riot Games offers an accessible API that allows the use of their data for such initiatives (https://developer.riotgames.com/)


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
