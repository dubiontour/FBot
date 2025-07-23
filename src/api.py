from fastapi import FastAPI, HTTPException, Query
from config import LEAGUES
from sleeper import get_users, get_rosters, get_matchups, build_matchup_summary

app = FastAPI()

@app.get("/summary/{league}")
def summary(league: str, week: int = Query(1, ge=1, le=18)):
    league_id = LEAGUES.get(league)
    if not league_id:
        raise HTTPException(status_code=400, detail=f"Unbekannte Liga: {league}")

    try:
        users = get_users(league_id)
        rosters = get_rosters(league_id)
        matchups = get_matchups(league_id, week)
        summary = build_matchup_summary(users, rosters, matchups)
        return {
            "league": league,
            "week": week,
            "results": summary or ["Keine Matchups verfügbar"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Fehler beim Abrufen der Liga: {e}")
