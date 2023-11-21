import requests, json
from src.business.player.player import Player
from src.dao.playerDAO import PlayerDAO

class AdminService:
    def __init__(self):
        pass

    def add_player(self, name, api_key):
        # Retrieve summoner data
        summoner_url = f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={api_key}'
        summoner_data = requests.get(summoner_url)
        
        if summoner_data.status_code != 200:
            return('Error occured, check your API key or API availabily')
        
        summoner_data = summoner_data.json
        puuid = summoner_data['puuid']
        level = summoner_data['summonerLevel']
        summonerId = summoner_data['id']

        # Retrieve league data
        league_url = f'https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summonerId}?api_key={api_key}'
        league_data = requests.get(league_url).json()

        is_ranked = False
        try :
            for queue in league_data:
                if queue['queueType'] == 'RANKED_SOLO_5x5':
                    league_data = queue
                    is_ranked = True
                    break
        except:
            return 'Player not found'

        if not is_ranked:
            return 'unranked'

        # Create new player object
        new_player = Player(
            name=league_data['summonerName'], 
            id=league_data['summonerId'], 
            puuid=puuid,
            rank=f"{league_data['tier']} {league_data['rank']}", 
            win=league_data['wins'],
            losses=league_data['losses'],
            level=level
        )
        
        matches_url = 'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/' + puuid +'/ids?type=ranked&start=0&count=20&api_key=' + api_key
        matches_id = requests.get(matches_url).json()

        print('Here are the infos that has been got :  \n')
        print(new_player, matches_id)

        PlayerDAO().add_player(new_player, matches_id)



