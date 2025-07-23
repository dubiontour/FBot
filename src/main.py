from config import LEAGUES
from sleeper import get_league, get_users, get_rosters, get_matchups, build_matchup_summary

WEEK = 1  # Kannst du auch aus der API ermitteln, wenn gewünscht

if __name__ == "__main__":
    for name, league_id in LEAGUES.items():
        if not league_id:
            print(f"⚠️  League ID für {name} fehlt in der .env-Datei")
            continue

        print(f"\n📊 {name} – Week {WEEK}")
        try:
            users = get_users(league_id)
            rosters = get_rosters(league_id)
            matchups = get_matchups(league_id, WEEK)
            summary = build_matchup_summary(users, rosters, matchups)

            if summary:
                for line in summary:
                    print("✅", line)
            else:
                print("⚠️  Keine Matchups gefunden.")
        except Exception as e:
            print(f"❌ Fehler beim Abrufen von {name}: {e}")
