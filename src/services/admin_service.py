import requests
import json
import time
from src.business.player.player import Player
from src.business.participant.participant import Participant
from src.dao.playerDAO import PlayerDAO
from src.dao.participantDAO import ParticipantDAO
from data.components import extract_participant_info

class AdminService:
    def __init__(self):
        pass

    def add_player(self, name, api_key):
        # Retrieve summoner data from Riot API
        summoner_url = f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={api_key}'
        summoner_data = requests.get(summoner_url)
        
        # Check if the request was successful
        if summoner_data.status_code != 200:
            return 'Error occurred, check your API key or API availability'
        
        # Parse the JSON response
        summoner_data = summoner_data.json()
        puuid = summoner_data['puuid']
        level = summoner_data['summonerLevel']
        summonerId = summoner_data['id']

        # Retrieve league data for the summoner
        league_url = f'https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summonerId}?api_key={api_key}'
        league_data = requests.get(league_url).json()

        # Check if the player is ranked
        is_ranked = False
        try:
            for queue in league_data:
                if queue['queueType'] == 'RANKED_SOLO_5x5':
                    league_data = queue
                    is_ranked = True
                    break
        except:
            return 'Player not found'

        if not is_ranked:
            return 'Unranked'

        # Create a new player object with the retrieved data
        new_player = Player(
            name=league_data['summonerName'], 
            id=league_data['summonerId'], 
            puuid=puuid,
            rank=f"{league_data['tier']} {league_data['rank']}", 
            win=league_data['wins'],
            losses=league_data['losses'],
            level=level
        )
        
        # Retrieve the last 20 ranked match IDs
        matches_url = f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?type=ranked&start=0&count=20&api_key={api_key}'
        matches_id = requests.get(matches_url).json()

        print('Here are the infos that has been got:\n')
        print(new_player, matches_id)

        # Add the new player and their matches to the database
        PlayerDAO().add_player(new_player, matches_id)
        time.sleep(1)

        # Process each match and add participant data to the database
        for matchId in matches_id[:10]:
            match_url = f"https://europe.api.riotgames.com/lol/match/v5/matches/{matchId}?api_key={api_key}"
            match_data = requests.get(match_url).json()
            participants = extract_participant_info(match_data)

            for participant in participants:
                P = Participant(
                    id_game=participant[1],
                    puuid=participant[0],
                    teamID=participant[3],
                    totalDamageDealtToChampions=participant[4],
                    win=participant[5],
                    lane=participant[7],
                    role=participant[8],
                    totalMinionsKilled=participant[6],
                    championName=participant[9],
                    goldEarned=participant[10],
                    death=participant[11],
                    assists=participant[12],
                    kills=participant[13],
                    gameDuration=participant[2]
                )

                ParticipantDAO.add_participant(P)
