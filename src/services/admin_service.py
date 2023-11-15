import requests, json
from src.business.player.player import Player

class AdminService():
    def __init__(self):
        pass
    
    def add_player(self, name, api_key):
        summoner_url = 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + name + '?api_key=' + api_key
        summoner_data = requests.get(summoner_url).json()
        puuid = summoner_data['puuid']
        level = summoner_data['summonerLevel']
        summonerId = summoner_data['id']
        
        league_url = 'https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + summonerId + '?api_key=' + api_key
        league_data = requests.get(league_url).json()
        
        is_ranked = False
        for queue in league_data:
            if queue['queueType'] == 'RANKED_SOLO_5x5':
                league_data = queue
                is_ranked = True
                break
            
        if not is_ranked:
            return 'unranked'

  
        print(league_data)

