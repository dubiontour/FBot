import requests

LEAGUE_ID = "289646328504385536"
WEEK = 1  # Ändere das ggf. auf einen Spieltag mit echten Daten

def get_league():
    url = f"https://api.sleeper.app/v1/league/{LEAGUE_ID}"
    res = requests.get(url)
    res.raise_for_status()
    return res.json()

def get_users():
    url = f"https://api.sleeper.app/v1/league/{LEAGUE_ID}/users"
    res = requests.get(url)
    res.raise_for_status()
    return res.json()

def get_rosters():
    url = f"https://api.sleeper.app/v1/league/{LEAGUE_ID}/rosters"
    res = requests.get(url)
    res.raise_for_status()
    return res.json()

def get_matchups(week):
    url = f"https://api.sleeper.app/v1/league/{LEAGUE_ID}/matchups/{week}"
    res = requests.get(url)
    res.raise_for_status()
    return res.json()

if __name__ == "__main__":
    print("== LEAGUE INFO ==")
    print(get_league())
    
    print("\n== USERS ==")
    users = get_users()
    print(users[:2])  # gekürzt für Übersicht

    print("\n== ROSTERS ==")
    rosters = get_rosters()
    print(rosters[:2])

    print(f"\n== MATCHUPS (Week {WEEK}) ==")
    matchups = get_matchups(WEEK)
    print(matchups[:4])  # meist leer in der Offseason

def build_matchup_summary(users, rosters, matchups):
    # Mappe owner_id → display_name
    owner_map = {u['user_id']: u['display_name'] for u in users}

    # Mappe roster_id → owner_name
    roster_map = {
        r['roster_id']: owner_map.get(r['owner_id'], f"Unknown_{r['owner_id']}")
        for r in rosters
    }

    # Gruppiere Matchups nach matchup_id
    matchups_by_pair = {}
    for m in matchups:
        matchup_id = m['matchup_id']
        if matchup_id not in matchups_by_pair:
            matchups_by_pair[matchup_id] = []
        matchups_by_pair[matchup_id].append(m)

    # Baue schöne Übersicht
    results = []
    for matchup_id, entries in matchups_by_pair.items():
        if len(entries) != 2:
            continue  # bye week oder unvollständig
        team1, team2 = entries
        name1 = roster_map.get(team1['roster_id'], "Unknown")
        name2 = roster_map.get(team2['roster_id'], "Unknown")
        points1 = round(team1['points'], 2)
        points2 = round(team2['points'], 2)
        results.append(f"{name1} ({points1}) vs {name2} ({points2})")

    return results
    