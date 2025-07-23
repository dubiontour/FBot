from sleeper import get_users, get_rosters, get_matchups, build_matchup_summary

WEEK = 1  # Kannst du variabel machen, wenn Saison läuft

if __name__ == "__main__":
    print("📡 FBot: Daten werden geladen...")

    users = get_users()
    rosters = get_rosters()
    matchups = get_matchups(WEEK)

    print(f"\n📊 Matchups – Week {WEEK}:\n")

    summary = build_matchup_summary(users, rosters, matchups)
    
    if summary:
        for line in summary:
            print("✅", line)
    else:
        print("⚠️  Keine Matchups gefunden – vielleicht ist noch keine Saison?")
