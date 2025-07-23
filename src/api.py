from fastapi import FastAPI
from sleeper import get_users, get_rosters, get_matchups, build_matchup_summary
from config import LEAGUES

app = FastAPI()

@app.get("/")
def root():
    return {"status": "FBot API ist aktiv."}

@app.get("/summary/{league}")
def summary(league: str, week: int = 1):
    league_id = LEAGUES.get(league)
    if not league_id:
        return {"error": f"Keine League-ID für {league} gefunden."}
    try:
        users = get_users(league_id)
        rosters = get_rosters(league_id)
        matchups = get_matchups(league_id, week)
        result = build_matchup_summary(users, rosters, matchups)
        return {"matchups": result}
    except Exception as e:
        return {"error": str(e)}