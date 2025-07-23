import requests

def get_league(league_id):
    url = f"https://api.sleeper.app/v1/league/{league_id}"
    res = requests.get(url)
    res.raise_for_status()
    return res.json()

def get_users(league_id):
    url = f"https://api.sleeper.app/v1/league/{league_id}/users"
    res = requests.get(url)
    res.raise_for_status()
    return res.json()

def get_rosters(league_id):
    url = f"https://api.sleeper.app/v1/league/{league_id}/rosters"
    res = requests.get(url)
    res.raise_for_status()
    return res.json()

def get_matchups(league_id, week):
    url = f"https://api.sleeper.app/v1/league/{league_id}/matchups/{week}"
    res = requests.get(url)
    res.raise_for_status()
    return res.json()

def build_matchup_summary(users, rosters, matchups):
    owner_map = {u['user_id']: u['display_name'] for u in users}
    roster_map = {
        r['roster_id']: owner_map.get(r['owner_id'], f"Unknown_{r['owner_id']}")
        for r in rosters
    }

    matchups_by_pair = {}
    for m in matchups:
        matchup_id = m['matchup_id']
        matchups_by_pair.setdefault(matchup_id, []).append(m)

    results = []
    for entries in matchups_by_pair.values():
        if len(entries) != 2:
            continue
        team1, team2 = entries
        name1 = roster_map.get(team1['roster_id'], "Unknown")
        name2 = roster_map.get(team2['roster_id'], "Unknown")
        points1 = round(team1['points'], 2)
        points2 = round(team2['points'], 2)
        results.append(f"{name1} ({points1}) vs {name2} ({points2})")
    return results
