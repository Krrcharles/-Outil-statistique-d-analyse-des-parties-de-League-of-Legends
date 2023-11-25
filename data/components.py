def extract_participant_info(json_data) -> None :
    """ Obtenir les informations d'une partie à partir d'un JSON

    Parameters :
    
        json_data : JSON 

    Return :

        List
    """
    match_id = json_data["metadata"]["matchId"]
    info = json_data["info"]

    # Vérifie si json_data est un dictionnaire
    if not isinstance(json_data, dict):
        raise ValueError("json_data n'est pas un dictionnaire JSON valide")

    # Accéder aux informations spécifiques pour chaque participant
    participants = info.get("participants", [])

    # Créer une liste pour stocker les informations de tous les participants
    participants_info = []
    #participant_info.append(participants["metadata"])
    #participant_info.append(info["gameDuration"])
    

    for participant in participants:
        # Créer une liste avec les informations spécifiques pour ce participant
        participant_data = [
            participant["puuid"],
            match_id,
            info.get("gameDuration"),
            participant["teamId"],
            participant["totalDamageDealtToChampions"],
            participant["win"],
            participant["totalMinionsKilled"],
            participant["lane"],
            participant["role"],
            participant["championName"],
            participant["goldEarned"],
            participant["deaths"],
            participant["assists"],
            participant["kills"]
        ]

        # Étendre la liste d'informations à la liste des participants
        participants_info.append(participant_data)

    return participants_info