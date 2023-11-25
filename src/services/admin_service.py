"""
Module docstring: This module provides services related to administration functions
in the application, specifically managing players by interacting with Riot's API.
"""

import time
import requests
from src.business.player.player import Player
from src.business.participant.participant import Participant
from src.dao.playerDAO import PlayerDAO
from src.dao.participantDAO import ParticipantDAO
from data.components import extract_participant_info

class AdminService:
    """Class handling administrative services such as adding new players."""

    def __init__(self):
        pass

    def add_player(self, name, api_key):
        """
        Adds a player to the database using their name and API key.
        Retrieves player and match data from Riot's API.
        """
        # Define API URLs
        summoner_url = (f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
                        f'{name}?api_key={api_key}')
        league_url_template = ('https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/'
                                '{}?api_key={}')

        # Retrieve summoner data
        summoner_data = requests.get(summoner_url, timeout=5)
        if summoner_data.status_code != 200:
            return 'Error: Check your API key or API availability'
        summoner_data = summoner_data.json()
        # Extract relevant data
        puuid = summoner_data['puuid']
        level = summoner_data['summonerLevel']
        summoner_id = summoner_data['id']

        # Retrieve league data
        league_url = league_url_template.format(summoner_id, api_key)
        league_data = requests.get(league_url, timeout=5).json()

        is_ranked = False
        try:
            for queue in league_data:
                if queue['queueType'] == 'RANKED_SOLO_5x5':
                    league_data = queue
                    is_ranked = True
                    break
        except Exception as e:
            return f'Player not found: {e}'

        if not is_ranked:
            return 'Unranked'

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
        
        # Retrieve match IDs
        matches_url = (f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/'
                       f'{puuid}/ids?type=ranked&start=0&count=20&api_key={api_key}')
        matches_id = requests.get(matches_url, timeout=5).json()

        print('Retrieved player and match information:\n')
        print(new_player, matches_id)

        PlayerDAO().add_player(new_player, matches_id)
        time.sleep(1)

        # Process and store participant data
        for match_id in matches_id[:10]:
            match_url = (f"https://europe.api.riotgames.com/lol/match/v5/matches/"
                         f"{match_id}?api_key={api_key}")
            match_data = requests.get(match_url, timeout=5).json()
            participants = extract_participant_info(match_data)

            for participant in participants:
                participant_instance = Participant(
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

                ParticipantDAO.add_participant(participant_instance)
